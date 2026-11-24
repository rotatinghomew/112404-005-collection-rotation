from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from museum_workbench.inputs import read_table


class MaterialTests(unittest.TestCase):
    def test_tables_have_rows_and_uniform_record_fields(self):
        paths = sorted((ROOT / 'data').glob('*.csv'))
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            with self.subTest(table=path.name):
                rows = read_table(path)
                self.assertTrue(rows)
                self.assertTrue(all(all(isinstance(v, str) for v in row.values()) for row in rows))
                self.assertEqual(set(rows[0]), set(rows[-1]))
                self.assertTrue(all(any(value.strip() for value in row.values()) for row in rows))

    def test_scenario_materials_have_resolvable_business_references(self):
        works = read_table(ROOT / "data/works.csv")
        rotations = read_table(ROOT / "data/rotation_windows.csv")
        environment = read_table(ROOT / "data/environment.csv")
        self.assertTrue({row["work_id"] for row in rotations} <= {row["work_id"] for row in works})
        self.assertTrue(any(row["device_state"] == "offline" and not row["lux_hours"] for row in environment))
        self.assertTrue(all(int(row["max_display_days"]) > 0 for row in works))

    def test_dates_and_identifiers_remain_strings(self):
        for path in (ROOT / 'data').glob('*.csv'):
            rows = read_table(path)
            self.assertTrue(all(isinstance(value, str) for row in rows for value in row.values()))


if __name__ == '__main__':
    unittest.main()
