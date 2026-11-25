"""Copy to tools/drugdb/test_dailymed_safety.py after applying importer.patch."""
import copy
import importlib.util
import sys
import unittest
from pathlib import Path

import fetch_dailymed_pins as spl

PIN=dict(set_id='pin',slug='test',verify_text=['TEST DRUG'],application='NDA000001',brand='TEST',generic='test',substances=['TEST'],routes=['ORAL'],manufacturer='TEST',reason='fixture')
def fixture(warning=True):
    safety='''<component><section><code code="34071-1"/><text>Original warning must remain.</text></section></component>
    <component><section><code code="42232-9"/><title>PRECAUTIONS</title><component><section><code code="34072-9"/><title>General</title><text>Distinct clinically relevant precaution must remain.</text></section></component></section></component>''' if warning else ''
    return ('''<document xmlns="urn:hl7-org:v3"><id root="doc"/><setId root="pin"/><versionNumber value="1"/><effectiveTime value="20261125"/><title>TEST DRUG</title><approval><id extension="NDA000001"/></approval>
    <component><section><code code="34067-9"/><text>TEST DRUG is indicated for a specific disease in an appropriately selected patient population.</text></section></component>
    <component><section><code code="34068-7"/><text>Individualize treatment for the patient's condition and use the product-specific administration instructions.</text></section></component>
    <component><section><code code="34070-3"/><text>Known hypersensitivity.</text></section></component>'''+safety+'</document>').encode()

class SafetyTests(unittest.TestCase):
    def test_legacy_warnings_and_precautions_both_survive(self):
        rec=spl.parse_spl(fixture(),PIN,{'ingredients':['test']})
        text=rec['sections']['warnings_and_cautions']
        self.assertIn('Original warning must remain.',text)
        self.assertIn('Distinct clinically relevant precaution must remain.',text)
    def test_missing_warning_fails_closed(self):
        with self.assertRaisesRegex(ValueError,'warnings_and_cautions'):
            spl.parse_spl(fixture(False),PIN,{'ingredients':['test']})

class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.rec={'slug':'test','name':'Test','label':{'set_id':'pin','effective_time':'20261125','brand_name':'TEST','application_number':'NDA000001'},'source':{'dailymed_url':'https://example.test/label'},'sections':{'warnings':'retained'}}
        self.doc={'added':[],'changed':[],'removed':[]}
    def test_new_and_changed_pins_logged(self):
        spl.reconcile_changes(self.doc,None,self.rec)
        self.assertEqual(self.doc['added'][0]['slug'],'test')
        self.doc={'added':[],'changed':[],'removed':[]};old=copy.deepcopy(self.rec);old['label']['effective_time']='20250101'
        spl.reconcile_changes(self.doc,old,self.rec)
        self.assertEqual(self.doc['changed'][0]['previous']['effective_time'],'20250101')
    def test_restored_unchanged_pin_removes_false_removal(self):
        self.doc['removed']=[{'slug':'test','previous':{'set_id':'pin','effective_time':'20261125'}}]
        spl.reconcile_changes(self.doc,None,self.rec)
        self.assertEqual(self.doc,{'added':[],'changed':[],'removed':[]})
    def test_existing_added_uses_final_pin_metadata(self):
        self.doc['added']=[{'slug':'test','set_id':'temporary-openfda'}]
        spl.reconcile_changes(self.doc,None,self.rec)
        self.assertEqual(self.doc['added'][0]['set_id'],'pin')
    def test_unchanged_pin_does_not_create_review_item(self):
        spl.reconcile_changes(self.doc,copy.deepcopy(self.rec),self.rec)
        self.assertFalse(any(self.doc.values()))

if __name__=='__main__':unittest.main()
