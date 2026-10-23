import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import summarize_project


class SummarizeProjectTests(unittest.TestCase):
    def test_returns_project_name(self):
        self.assertEqual(summarize_project("Civic Helper"), "Project ready: Civic Helper")

    def test_trims_whitespace(self):
        self.assertEqual(summarize_project("  Demo  "), "Project ready: Demo")

    def test_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            summarize_project("  ")


if __name__ == "__main__":
    unittest.main()
