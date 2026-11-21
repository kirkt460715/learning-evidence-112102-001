import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'assignment')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_task_versions_and_independent_checks_remain_distinct(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        revisions = {row['revision'] for row in data['catalogs']['tasks']}
        self.assertEqual(revisions, {'r1', 'r2'})
        checks = [row for row in data['records'] if row['kind'] == 'check']
        self.assertEqual({row['status'] for row in checks}, {'pending', 'not-scheduled', 'failed'})
        self.assertTrue(all(row['help_removed'] for row in checks))
        work = [row for row in data['records'] if row['kind'] == 'work']
        self.assertTrue(any(row['help'] == 'worked-example' for row in work))

if __name__ == '__main__':
    unittest.main()
