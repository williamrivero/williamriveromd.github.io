"""No network: DPD water ingredient matches must preserve named formulation identity."""
import importlib.util,sys,unittest
from pathlib import Path
import fetch_eu_smpc as eu

class WaterDPDTests(unittest.TestCase):
    def fixture(self,ingredients):
        dpd=eu.DPD.__new__(eu.DPD)
        dpd.drugs={'117':{'brand':'BACTERIOSTATIC WATER','din':'00038202'},'31491':{'brand':'STERILE WATER FOR INJECTION','din':'02142546'},'999':{'brand':'Sterile Water for Injection USP','din':'99999999'}}
        dpd.ings={c:([ingredients[0]] if 'sterile' in ingredients[0].lower() else ['WATER'])for c in dpd.drugs};dpd.comp={};dpd.route={c:['intravenous']for c in dpd.drugs}
        words={w for i in eu.expand_ingredients(tuple(ingredients))for w in eu.ing_tokens(i)if w not in eu.SALT_WORDS};dpd.by_word={w:set(dpd.drugs)for w in words}
        return dpd
    def test_plain_or_sterile_query_excludes_bacteriostatic_before_two_hit_cap(self):
        for query in ['water for injection',' Sterile  Water for Injection ']:
            with self.subTest(query=query):
                hits=self.fixture([query]).find([query],{})
                self.assertEqual(len(hits),2);self.assertEqual({x['din']for x in hits},{'02142546','99999999'})
                self.assertFalse(any('bacteriostatic'in x['product'].lower()for x in hits))
    def test_other_water_query_keeps_existing_selection(self):
        hits=self.fixture(['water']).find(['water'],{})
        self.assertEqual(len(hits),2);self.assertEqual(hits[0]['din'],'00038202')
if __name__=='__main__':unittest.main()
