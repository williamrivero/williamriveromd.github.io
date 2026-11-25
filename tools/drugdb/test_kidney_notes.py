"""Copy to tools/drugdb/test_kidney_notes.py; current generator, no network."""
import datetime as dt
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
import generate_drug_pages as pages

class KidneyNotesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.ctx=pages.Ctx(ROOT/'data/drugs',dt.date(2026,11,25))
    def render(self,status):
        s={'review_status':status,'special_populations':{'renal':['Kidney sentinel <claim> [[TESTSRC]]']},'sources':[{'id':'TESTSRC','url':'https://pubmed.ncbi.nlm.nih.gov/1/','citation':'Fixture source'}]}
        with patch.object(self.ctx,'summary',side_effect=lambda slug:s if slug=='metolazone' else None):
            return pages.page_for('metolazone',self.ctx.generics['metolazone'],self.ctx)[0]
    def test_approved_notes_render_as_referenced_considerations(self):
        h=self.render('approved');start=h.index('id="kidney-dosing"');end=h.index('</section>',start);kidney=h[start:end]
        self.assertIn('Referenced kidney considerations',kidney)
        self.assertIn('Kidney sentinel &lt;claim&gt;',kidney)
        self.assertNotIn('[[TESTSRC]]',h)
        self.assertIn('href="https://pubmed.ncbi.nlm.nih.gov/1/"',h)
    def test_pending_notes_never_render(self):
        h=self.render('pending');self.assertNotIn('Kidney sentinel',h);self.assertNotIn('Referenced kidney considerations',h)

if __name__=='__main__':unittest.main()
