"""Regression: offline downloads include only valid generated HTML filenames."""
import builtins,sys,tempfile,types,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
import generate_drug_pages as pages

class OfflineManifestTests(unittest.TestCase):
    def test_duplicate_copies_never_opened_and_valid_pages_retained(self):
        with tempfile.TemporaryDirectory()as td:
            root=Path(td);out=root/'drugs';out.mkdir()
            invalid=set();expected=set()
            for sub in ['', 'category','supplements']:
                d=out/sub;d.mkdir(exist_ok=True)
                for stem in ['valid-drug','a1','index','offline']:
                    f=d/(stem+'.html');f.write_text('<html>valid</html>')
                    if sub:expected.add('/drugs/'+sub+'/' if stem=='index' else '/drugs/'+sub+'/'+stem)
                    elif stem not in ['index','offline']:expected.add('/drugs/'+stem)
                for stem in ['blumea-balsamifera-l 2','valid-drug 3','BadSlug','-bad','copy_2']:
                    f=d/(stem+'.html');f.write_text('user copy');invalid.add(f)
            sdata=root/'data/drugs/supplements';sdata.mkdir(parents=True)
            for stem in ['0','a','c','z']:
                (sdata/(stem+'.json')).write_text('{}');expected.add('/data/drugs/supplements/'+stem+'.json')
            for stem in ['c 2','z 3','_pages','_report']:
                f=sdata/(stem+'.json');f.write_text('user copy');invalid.add(f)
            real_open=builtins.open;opened=[]
            def guarded(file,*args,**kwargs):
                f=Path(file);self.assertNotIn(f,invalid,'non-generated copy must not be opened');opened.append(f);return real_open(file,*args,**kwargs)
            with patch.object(pages,'REPO',root),patch('builtins.open',side_effect=guarded):manifest=pages.offline_manifest(out)
            self.assertEqual({r[0]for r in manifest['pages']},expected)
            self.assertFalse(invalid&set(opened));self.assertTrue(all(f.read_text()=='user copy'for f in invalid))
if __name__=='__main__':unittest.main()
