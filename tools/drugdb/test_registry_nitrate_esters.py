"""Regression test: distinct nitrate esters survive registry normalization."""
import importlib.util
import unittest
from pathlib import Path
import build_registry as registry

class NitrateEsterTests(unittest.TestCase):
    def test_distinct_nitrate_esters_are_preserved(self):
        self.assertEqual(registry.ingredients_of('Isosorbide Mononitrate'),['isosorbide mononitrate'])
        self.assertEqual(registry.ingredients_of('Isosorbide Dinitrate'),['isosorbide dinitrate'])
        self.assertNotEqual(registry.slug_of(registry.ingredients_of('Isosorbide Mononitrate')),registry.slug_of(registry.ingredients_of('Isosorbide Dinitrate')))
    def test_numbered_mononitrate_retains_existing_identity(self):
        self.assertEqual(registry.ingredients_of('Isosorbide 5-mononitrate'),['isosorbide 5-mononitrate'])
    def test_unrelated_salt_normalization_unchanged(self):
        for name,expected in [('Thiamine mononitrate','thiamine'),('Miconazole nitrate','miconazole'),('Metoprolol tartrate','metoprolol'),('Hydralazine hydrochloride','hydralazine'),('Potassium nitrate','potassium nitrate')]:
            with self.subTest(name=name):self.assertEqual(registry.base_ingredient(name),expected)
    def test_fixed_combination_keeps_exact_nitrate_identity(self):
        self.assertEqual(registry.ingredients_of('Hydralazine hydrochloride + Isosorbide dinitrate'),['hydralazine','isosorbide dinitrate'])

if __name__=='__main__':unittest.main()
