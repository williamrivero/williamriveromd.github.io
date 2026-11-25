"""Exact nitrate identity migration and historical-hub safety regressions."""
import copy
import datetime as dt
import json
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
import generate_drug_pages as pages
import repair_isosorbide_registry as migration

def fixture():
    rows=[]
    for name,count in [('Isosorbide Mononitrate',33),('Isosorbide Dinitrate',26)]:
        for n in range(count):rows.append({'registration_number':name+str(n),'generic_name':name,'generic_slug':'isosorbide','ingredients':['isosorbide'],'brand_name':'Fixture','dosage_strength_form':'20 mg Tablet','pharmacologic_category':'Anti-angina','dispensing':'Rx','vat_exempt':True})
    g={'isosorbide':{'products':59},'isosorbide-5-mononitrate':{'products':7},'isosorbide-mononitrte':{'products':1}}
    return [rows,g,{}, {},{'entries':{'isosorbide':{'note':'old mixed list'}}}]

class MigrationTests(unittest.TestCase):
    def test_exact_split_preserves_raw_fields_and_counts(self):
        docs=fixture();rows,g,a,m,i,report=migration.transform(*docs)
        self.assertEqual(report['new_counts'],{'isosorbide-mononitrate':33,'isosorbide-dinitrate':26})
        self.assertEqual(report['canonical_mononitrate_products'],41)
        self.assertEqual(g['isosorbide']['products'],0)
        for old,new in zip(docs[0],rows):
            self.assertEqual({k:v for k,v in old.items()if k not in ['ingredients','generic_slug']},{k:v for k,v in new.items()if k not in ['ingredients','generic_slug']})
        self.assertNotIn('isosorbide',a);self.assertNotIn('isosorbide',i['entries'])
    def test_unknown_ingredient_or_repeat_rejected(self):
        docs=fixture();docs[0][0]['generic_name']='Isosorbide unknown'
        with self.assertRaises(ValueError):migration.transform(*docs)
        result=migration.transform(*fixture())
        with self.assertRaises(ValueError):migration.transform(*result[:5])
    def test_historical_hub_is_not_a_drug_or_dosing_page(self):
        with tempfile.TemporaryDirectory() as temp:
            d=Path(temp);g={'isosorbide':{'name':'Historical nitrate heading','ingredients':[]},'isosorbide-5-mononitrate':{'name':'Mononitrate','ingredients':['isosorbide mononitrate']},'isosorbide-dinitrate':{'name':'Dinitrate','ingredients':['isosorbide dinitrate']}}
            (d/'generics.json').write_text(json.dumps(g));hub=migration.transform(*fixture())[3];(d/'additional_monographs.json').write_text(json.dumps(hub))
            ctx=pages.Ctx(d,dt.date(2026,11,25));html,_,_=pages.page_for('isosorbide',g['isosorbide'],ctx)
            self.assertIn('CollectionPage',html);self.assertIn('noindex, follow',html)
            self.assertNotIn('"@type": "Drug"',html);self.assertNotIn('kidney-dosing',html)
            self.assertIn('isosorbide-5-mononitrate.html',html);self.assertIn('isosorbide-dinitrate.html',html)
            self.assertNotIn('Department of Health source',html)
if __name__=='__main__':unittest.main()
