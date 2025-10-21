# -*- coding: utf-8 -*-

"""
Tests for DD Neuron Molecular Profiles
Based on Smith et al. (2024) research paper
"""

import unittest
from cect.DDNeuronMolecularProfiles import (
    DDMolecularProfile,
    DD_MOLECULAR_PROFILES,
    get_dd_molecular_profile,
    get_neurons_by_subclass,
    get_neurons_by_hox_gene,
    get_dd_subclass_summary,
    export_to_dict,
)


class TestDDMolecularProfiles(unittest.TestCase):
    """Test suite for DD neuron molecular profiles."""

    def test_all_dd_neurons_have_profiles(self):
        """Test that all DD neurons (DD1-DD6) have molecular profiles defined."""
        expected_neurons = ["DD1", "DD2", "DD3", "DD4", "DD5", "DD6"]
        for neuron in expected_neurons:
            self.assertIn(neuron, DD_MOLECULAR_PROFILES)

    def test_dd1_profile(self):
        """Test DD1 molecular profile (Subclass 1)."""
        profile = get_dd_molecular_profile("DD1")
        self.assertEqual(profile.neuron_name, "DD1")
        self.assertEqual(profile.subclass, 1)
        self.assertEqual(profile.hox_genes, ["lin-39"])

    def test_dd2_profile(self):
        """Test DD2 molecular profile (Subclass 2)."""
        profile = get_dd_molecular_profile("DD2")
        self.assertEqual(profile.neuron_name, "DD2")
        self.assertEqual(profile.subclass, 2)
        self.assertEqual(sorted(profile.hox_genes), ["lin-39", "mab-5"])

    def test_dd3_profile(self):
        """Test DD3 molecular profile (Subclass 2)."""
        profile = get_dd_molecular_profile("DD3")
        self.assertEqual(profile.neuron_name, "DD3")
        self.assertEqual(profile.subclass, 2)
        self.assertEqual(sorted(profile.hox_genes), ["lin-39", "mab-5"])

    def test_dd4_profile(self):
        """Test DD4 molecular profile (Subclass 3)."""
        profile = get_dd_molecular_profile("DD4")
        self.assertEqual(profile.neuron_name, "DD4")
        self.assertEqual(profile.subclass, 3)
        self.assertEqual(sorted(profile.hox_genes), ["egl-5", "lin-39", "mab-5"])

    def test_dd5_profile(self):
        """Test DD5 molecular profile (Subclass 3)."""
        profile = get_dd_molecular_profile("DD5")
        self.assertEqual(profile.neuron_name, "DD5")
        self.assertEqual(profile.subclass, 3)
        self.assertEqual(sorted(profile.hox_genes), ["egl-5", "lin-39", "mab-5"])

    def test_dd6_profile(self):
        """Test DD6 molecular profile (Subclass 4)."""
        profile = get_dd_molecular_profile("DD6")
        self.assertEqual(profile.neuron_name, "DD6")
        self.assertEqual(profile.subclass, 4)
        self.assertEqual(profile.hox_genes, ["egl-5"])

    def test_invalid_neuron_raises_error(self):
        """Test that requesting an invalid neuron raises KeyError."""
        with self.assertRaises(KeyError):
            get_dd_molecular_profile("DD7")
        with self.assertRaises(KeyError):
            get_dd_molecular_profile("DA1")

    def test_subclass_1_neurons(self):
        """Test that Subclass 1 contains only DD1."""
        neurons = get_neurons_by_subclass(1)
        self.assertEqual(sorted(neurons), ["DD1"])

    def test_subclass_2_neurons(self):
        """Test that Subclass 2 contains DD2 and DD3."""
        neurons = get_neurons_by_subclass(2)
        self.assertEqual(sorted(neurons), ["DD2", "DD3"])

    def test_subclass_3_neurons(self):
        """Test that Subclass 3 contains DD4 and DD5."""
        neurons = get_neurons_by_subclass(3)
        self.assertEqual(sorted(neurons), ["DD4", "DD5"])

    def test_subclass_4_neurons(self):
        """Test that Subclass 4 contains only DD6."""
        neurons = get_neurons_by_subclass(4)
        self.assertEqual(sorted(neurons), ["DD6"])

    def test_lin39_expressing_neurons(self):
        """Test neurons expressing lin-39 Hox gene."""
        neurons = get_neurons_by_hox_gene("lin-39")
        self.assertEqual(sorted(neurons), ["DD1", "DD2", "DD3", "DD4", "DD5"])

    def test_mab5_expressing_neurons(self):
        """Test neurons expressing mab-5 Hox gene."""
        neurons = get_neurons_by_hox_gene("mab-5")
        self.assertEqual(sorted(neurons), ["DD2", "DD3", "DD4", "DD5"])

    def test_egl5_expressing_neurons(self):
        """Test neurons expressing egl-5 Hox gene."""
        neurons = get_neurons_by_hox_gene("egl-5")
        self.assertEqual(sorted(neurons), ["DD4", "DD5", "DD6"])

    def test_nonexistent_hox_gene(self):
        """Test querying for a non-existent Hox gene returns empty list."""
        neurons = get_neurons_by_hox_gene("nonexistent-gene")
        self.assertEqual(neurons, [])

    def test_subclass_summary(self):
        """Test that subclass summary contains all 4 subclasses."""
        summary = get_dd_subclass_summary()
        self.assertEqual(len(summary), 4)
        for subclass in range(1, 5):
            self.assertIn(subclass, summary)
            self.assertIn("neurons", summary[subclass])
            self.assertIn("hox_genes", summary[subclass])

    def test_export_to_dict_format(self):
        """Test that export_to_dict returns properly formatted data."""
        exported = export_to_dict()
        self.assertEqual(len(exported), 6)  # All 6 DD neurons

        # Check structure for DD1
        self.assertIn("DD1", exported)
        dd1_data = exported["DD1"]
        self.assertEqual(dd1_data["neuron_name"], "DD1")
        self.assertEqual(dd1_data["subclass"], 1)
        self.assertEqual(dd1_data["hox_genes"], ["lin-39"])

        # Check structure for DD4
        self.assertIn("DD4", exported)
        dd4_data = exported["DD4"]
        self.assertEqual(dd4_data["neuron_name"], "DD4")
        self.assertEqual(dd4_data["subclass"], 3)
        self.assertEqual(sorted(dd4_data["hox_genes"]), ["egl-5", "lin-39", "mab-5"])

    def test_profile_to_dict(self):
        """Test DDMolecularProfile.to_dict() method."""
        profile = DDMolecularProfile("DD1", ["lin-39"], 1)
        profile_dict = profile.to_dict()

        self.assertEqual(profile_dict["neuron_name"], "DD1")
        self.assertEqual(profile_dict["hox_genes"], ["lin-39"])
        self.assertEqual(profile_dict["subclass"], 1)

    def test_four_distinct_subclasses(self):
        """Test that there are exactly 4 distinct molecular subclasses."""
        subclasses = set(profile.subclass for profile in DD_MOLECULAR_PROFILES.values())
        self.assertEqual(len(subclasses), 4)
        self.assertEqual(subclasses, {1, 2, 3, 4})

    def test_hox_gene_combinations_unique_to_subclasses(self):
        """Test that each subclass has a unique Hox gene combination."""
        subclass_hox_patterns = {}
        for profile in DD_MOLECULAR_PROFILES.values():
            hox_pattern = tuple(sorted(profile.hox_genes))
            if profile.subclass not in subclass_hox_patterns:
                subclass_hox_patterns[profile.subclass] = hox_pattern
            else:
                # All neurons in same subclass should have same Hox pattern
                self.assertEqual(subclass_hox_patterns[profile.subclass], hox_pattern)

        # All 4 subclasses should have different Hox patterns
        self.assertEqual(len(set(subclass_hox_patterns.values())), 4)


if __name__ == "__main__":
    unittest.main()
