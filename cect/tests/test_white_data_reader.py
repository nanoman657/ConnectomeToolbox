from pathlib import Path

from cect.WhiteDataReader import get_instance, WhiteDataReader

import unittest

class TestReader(unittest.TestCase):
    def test_get_instance(self):
        current_filepath = Path(__file__)
        spreadsheet_directory: Path = current_filepath.parents[1] / "data"
        spreadsheet_filepath: Path = spreadsheet_directory / "aconnectome_white_1986_whole.csv"

        assert spreadsheet_filepath.is_file(), f"Test data file should exist at {spreadsheet_filepath}"
        filename = str(spreadsheet_filepath)
        instance: WhiteDataReader = get_instance(from_cache=False, spreadsheet_location=filename)
        data: tuple = instance.read_data()
        
        assert isinstance(instance, WhiteDataReader), "Instance should be of type WhiteDataReader"
        assert any([any(_) for _ in data]), "Instance should contain data"

if __name__ == "__main__":
    unittest.main()