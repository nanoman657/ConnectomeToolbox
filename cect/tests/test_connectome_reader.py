from cect import print_
import unittest
from cect.ConnectomeReader import check_cells
from cect.Cells import PREFERRED_HERM_NEURON_NAMES


class TestConnectomeReader(unittest.TestCase):
    def test_conn_info(self):
        from cect.ConnectomeReader import ConnectionInfo, load_connection_info

        ci = ConnectionInfo("precell", "postcell", 66, "sy", "sc")

        str1 = str(ci)
        print_("Created: %s" % str1)

        d = ci.to_dict()

        print_("Dict version: %s" % d)

        ci2 = load_connection_info(d)

        str2 = str(ci2)
        print_("Reloaded: %s" % str2)

        assert str1 == str2


class TestCheckCells(unittest.TestCase):
    def test_should_group_muscle_cells(self):
        cells_input = ("MDL01",)

        cells_processed = check_cells(cells_input)

        in_preferred_output = cells_processed[0]
        not_in_preferred_output = cells_processed[1]
        missing_preferred_output = cells_processed[2]
        muscles_output = cells_processed[3]

        muscles_output_expected = list(cells_input)
        assert not in_preferred_output, "Cells included unexpectedly in 'in_preferred'"
        assert (
            missing_preferred_output == PREFERRED_HERM_NEURON_NAMES
        ), "Not all preferred herm neuron names missing"
        assert (
            not not_in_preferred_output
        ), "Cells included unexpectedly in 'not_in_preferred'"
        assert (
            muscles_output == muscles_output_expected
        ), "Input muscle cells are not all grouped together"


if __name__ == "__main__":
    unittest.main()
