"""Explicit reference additions must never fabricate Philippine registrations."""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(Path(__file__).parent))
spec=importlib.util.spec_from_file_location('drug_pages',ROOT/'generate_drug_pages.py')
gen=importlib.util.module_from_spec(spec);sys.modules[spec.name]=gen;spec.loader.exec_module(gen)
class AdditionalMonographsTests(unittest.TestCase):
    def context(self,enabled=True,existing=False,url='https://example.org/source'):
        tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup);p=Path(tmp.name)
        (p/'generics.json').write_text(json.dumps({'test':{'name':'Existing','ingredients':['test']}} if existing else {}))
        (p/'additional_monographs.json').write_text(json.dumps({'test':{'enabled':enabled,'name':'Test medicine','ingredients':['test'],'search_brands':['Testbrand'],'source_url':url}}))
        return gen.Ctx(p,dt.date(2026,11,25))
    def test_reference_has_search_brand_but_no_registry_rows(self):
        ctx=self.context();self.assertEqual(ctx.generics['test']['products'],0)
        self.assertFalse(ctx.by_slug.get('test'));self.assertFalse(ctx.products)
        entry,_=gen.index_entry('test',ctx.generics['test'],ctx)
        self.assertIn('Testbrand',entry['b'])
    def test_existing_registry_generic_wins(self):
        ctx=self.context(existing=True);self.assertEqual(ctx.generics['test']['name'],'Existing')
    def test_disabled_or_unsafe_reference_not_added(self):
        for kwargs in ({'enabled':False},{'url':'javascript:alert(1)'}):
            with self.subTest(kwargs=kwargs):self.assertNotIn('test',self.context(**kwargs).generics)
    def test_zero_record_message_does_not_claim_unregistered(self):
        html=gen.render_products('test',{'name':'Test'},[],dt.date(2026,11,25))
        self.assertIn('does not establish that the medicine is unregistered',html)
        self.assertNotIn('0 products registered',html)
if __name__=='__main__':unittest.main()
