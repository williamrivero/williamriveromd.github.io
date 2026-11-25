"""Offline regression for both approved evidence schemas. Copy to tools/drugdb/ after applying patch."""
import datetime as dt
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
import generate_drug_pages as pages

class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.ctx=pages.Ctx(ROOT/'data/drugs',dt.date(2026,11,25))
    def render(self,status='approved',url='https://pubmed.ncbi.nlm.nih.gov/1/',source_ids=None,evidence=None):
        s={'review_status':status,'evidence':evidence if evidence is not None else [{'title':'Evidence <heading>','paragraphs':[{'text':'TEST <claim>','source_ids':['r'] if source_ids is None else source_ids}]}],
           'sources':[{'id':'r','url':url,'short':'Trial'}]}
        with patch.object(self.ctx,'summary',side_effect=lambda slug:s if slug=='metolazone' else None):
            return pages.page_for('metolazone',self.ctx.generics['metolazone'],self.ctx)[0]
    def test_approved_cited_list_renders_with_escaping(self):
        h=self.render();self.assertIn('TEST &lt;claim&gt;',h);self.assertIn('Evidence &lt;heading&gt;',h)
        self.assertIn('href="https://pubmed.ncbi.nlm.nih.gov/1/"',h);self.assertEqual(h.count('id="evidence"'),1)
    def test_pending_does_not_render(self):self.assertNotIn('TEST &lt;claim&gt;',self.render(status='pending'))
    def test_uncited_or_unknown_source_does_not_render(self):
        for ids in [[],['unknown']]:
            with self.subTest(ids=ids):self.assertNotIn('TEST &lt;claim&gt;',self.render(source_ids=ids))
    def test_unsafe_or_non_http_source_does_not_render(self):
        for url in ['javascript:alert(1)','data:text/plain,test','/relative','mailto:test@example.com','']:
            with self.subTest(url=url):self.assertNotIn('TEST &lt;claim&gt;',self.render(url=url))
    def test_existing_dict_table_still_renders(self):
        h=self.render(evidence={'title':'Existing evidence table','rows':[{'study':'Study sentinel','findings':'Table findings'}]})
        self.assertIn('Existing evidence table',h);self.assertIn('Table findings',h);self.assertEqual(h.count('id="evidence"'),1)
    def test_non_mapping_list_members_do_not_render(self):
        self.assertNotIn('TEST &lt;claim&gt;',self.render(evidence=[None,'invalid',{'paragraphs':[None,'invalid',{'text':'TEST <claim>','source_ids':[]}]}]))

if __name__=='__main__':unittest.main()
