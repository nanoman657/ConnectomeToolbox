import pytest

from cect import print_
import unittest
import pdb
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


class TestCheckCells:
    @pytest.mark.parametrize(
        "cells_input,muscle_cells_expected,error_msg",
        [
            (
                ("MDL01",),
                [
                    "MDL01",
                ],
                "Single muscle cell was not grouped with muscle cell group.",
            ),
            (
                ("MDL01", "MDR01"),
                ["MDL01", "MDR01"],
                "Both muscles cells were not grouped with muscle cell group.",
            ),
        ],
    )
    def test_should_group_muscle_cells(
        self, cells_input: tuple, muscle_cells_expected: list, error_msg: str
    ):
        cells_processed = check_cells(cells_input)
        in_preferred_output = cells_processed[0]
        not_in_preferred_output = cells_processed[1]
        missing_preferred_output = cells_processed[2]
        muscle_cells = cells_processed[3]

        assert not in_preferred_output, "Cells included unexpectedly in 'in_preferred'"
        assert (
            missing_preferred_output == PREFERRED_HERM_NEURON_NAMES
        ), "Not all preferred herm neuron names missing"
        assert (
            not not_in_preferred_output
        ), "Cells included unexpectedly in 'not_in_preferred'"
        assert (
            muscle_cells == muscle_cells_expected
        ), "Input muscle cells are not all grouped together"

    @pytest.mark.parametrize(
        "cells_input,preferred_cells_expected,error_msg",
        [
            (
                    ("MDL01",),
                    [],
                    "Cell 'MDL01' grouped incorrectly with preferred cell group.",
            ),
            (
                    ("MDL01", "ADAL"),
                    ["ADAL"],
                    "Preferred cells not calculated correctly.",
            ),
            (
                    ("ADAL",),
                    ["ADAL",],
                    "'ADAL' not grouped in 'in_preferred'.",
            ),
        ],
    )
    def test_should_group_preferred_cells(
            self, cells_input: tuple, preferred_cells_expected: list, error_msg: str
    ):
        cells_processed = check_cells(cells_input)
        in_preferred_output = cells_processed[0]
        not_in_preferred_output = cells_processed[1]
        missing_preferred_output = cells_processed[2]
        muscle_cells = cells_processed[3]

        assert in_preferred_output == preferred_cells_expected, "Cells included unexpectedly in 'in_preferred'"
        assert (
                len(missing_preferred_output) == len(PREFERRED_HERM_NEURON_NAMES) - len(preferred_cells_expected)
        ), "Not all preferred herm neuron names missing"
        assert (
            not not_in_preferred_output
        ), "Cells included unexpectedly in 'not_in_preferred'"

if __name__ == "__main__":
    unittest.main()
