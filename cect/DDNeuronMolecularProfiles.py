# -*- coding: utf-8 -*-

############################################################

#    DD Neuron Molecular Profiles
#    Based on Smith et al. (2024) research paper
#    Defines molecular subclasses for DD-class motor neurons
#    based on combinatorial Hox gene expression codes

############################################################

from typing import Dict, List
from cect import print_


class DDMolecularProfile:
    """
    Represents the molecular profile of a DD neuron based on Hox gene expression.

    Based on Figure 3C from Smith et al. (2024), the six DD neurons can be
    divided into four distinct molecular subclasses based on their combinatorial
    Hox gene expression codes.
    """

    def __init__(self, neuron_name: str, hox_genes: List[str], subclass: int):
        """
        Initialize a DD neuron molecular profile.

        Args:
            neuron_name: Name of the DD neuron (e.g., "DD1")
            hox_genes: List of Hox genes expressed in this neuron
            subclass: Subclass number (1-4) based on molecular identity
        """
        self.neuron_name = neuron_name
        self.hox_genes = sorted(hox_genes)  # Sort for consistency
        self.subclass = subclass

    def __repr__(self):
        return f"DDMolecularProfile(neuron={self.neuron_name}, subclass={self.subclass}, hox_genes={self.hox_genes})"

    def to_dict(self):
        """Convert the profile to a dictionary format."""
        return {
            "neuron_name": self.neuron_name,
            "hox_genes": self.hox_genes,
            "subclass": self.subclass,
        }


# Define the molecular profiles for each DD neuron based on Smith et al. (2024)
# Figure 3C data:
# - Subclass 1: DD1 (lin-39)
# - Subclass 2: DD2, DD3 (lin-39, mab-5)
# - Subclass 3: DD4, DD5 (lin-39, mab-5, egl-5)
# - Subclass 4: DD6 (egl-5)

DD_MOLECULAR_PROFILES: Dict[str, DDMolecularProfile] = {
    "DD1": DDMolecularProfile("DD1", ["lin-39"], 1),
    "DD2": DDMolecularProfile("DD2", ["lin-39", "mab-5"], 2),
    "DD3": DDMolecularProfile("DD3", ["lin-39", "mab-5"], 2),
    "DD4": DDMolecularProfile("DD4", ["lin-39", "mab-5", "egl-5"], 3),
    "DD5": DDMolecularProfile("DD5", ["lin-39", "mab-5", "egl-5"], 3),
    "DD6": DDMolecularProfile("DD6", ["egl-5"], 4),
}


def get_dd_molecular_profile(neuron_name: str) -> DDMolecularProfile:
    """
    Get the molecular profile for a specific DD neuron.

    Args:
        neuron_name: Name of the DD neuron (e.g., "DD1")

    Returns:
        DDMolecularProfile object containing the Hox gene expression data

    Raises:
        KeyError: If the neuron name is not a DD1-DD6 neuron
    """
    if neuron_name not in DD_MOLECULAR_PROFILES:
        raise KeyError(
            f"No molecular profile found for neuron '{neuron_name}'. "
            f"Valid neurons are: {list(DD_MOLECULAR_PROFILES.keys())}"
        )
    return DD_MOLECULAR_PROFILES[neuron_name]


def get_neurons_by_subclass(subclass: int) -> List[str]:
    """
    Get all DD neurons belonging to a specific molecular subclass.

    Args:
        subclass: Subclass number (1-4)

    Returns:
        List of neuron names in the specified subclass
    """
    return [
        neuron
        for neuron, profile in DD_MOLECULAR_PROFILES.items()
        if profile.subclass == subclass
    ]


def get_neurons_by_hox_gene(hox_gene: str) -> List[str]:
    """
    Get all DD neurons that express a specific Hox gene.

    Args:
        hox_gene: Name of the Hox gene (e.g., "lin-39", "mab-5", "egl-5")

    Returns:
        List of neuron names that express the specified Hox gene
    """
    return [
        neuron
        for neuron, profile in DD_MOLECULAR_PROFILES.items()
        if hox_gene in profile.hox_genes
    ]


def get_dd_subclass_summary() -> Dict[int, Dict[str, any]]:
    """
    Get a summary of all DD subclasses with their neurons and Hox genes.

    Returns:
        Dictionary mapping subclass numbers to their neurons and Hox genes
    """
    summary = {}
    for subclass in range(1, 5):
        neurons = get_neurons_by_subclass(subclass)
        if neurons:
            # Get Hox genes from first neuron in subclass (all in same subclass have same genes)
            hox_genes = DD_MOLECULAR_PROFILES[neurons[0]].hox_genes
            summary[subclass] = {"neurons": neurons, "hox_genes": hox_genes}
    return summary


def export_to_dict() -> Dict[str, Dict[str, any]]:
    """
    Export all DD molecular profiles to a dictionary format suitable for integration
    with the OpenWorm connectome.

    Returns:
        Dictionary mapping neuron names to their molecular profiles
    """
    return {
        neuron: profile.to_dict() for neuron, profile in DD_MOLECULAR_PROFILES.items()
    }


def print_summary():
    """Print a formatted summary of DD neuron molecular profiles."""
    print_("\n" + "=" * 70)
    print_("DD Neuron Molecular Subclasses (Smith et al. 2024)")
    print_("=" * 70)

    summary = get_dd_subclass_summary()
    for subclass in sorted(summary.keys()):
        info = summary[subclass]
        print_(f"\nSubclass {subclass}:")
        print_(f"  Neurons: {', '.join(info['neurons'])}")
        print_(f"  Hox genes: {', '.join(info['hox_genes'])}")

    print_("\n" + "=" * 70)
    print_("Individual Neuron Profiles:")
    print_("=" * 70)
    for neuron in sorted(DD_MOLECULAR_PROFILES.keys()):
        profile = DD_MOLECULAR_PROFILES[neuron]
        print_(
            f"{neuron}: Subclass {profile.subclass}, Hox genes: {', '.join(profile.hox_genes)}"
        )

    print_("\n" + "=" * 70)


if __name__ == "__main__":
    # Print summary when run as a script
    print_summary()

    # Example usage
    print_("\nExample queries:")
    print_("=" * 70)

    # Get profile for a specific neuron
    dd4_profile = get_dd_molecular_profile("DD4")
    print_(f"\nDD4 molecular profile: {dd4_profile}")

    # Get neurons by subclass
    subclass_3 = get_neurons_by_subclass(3)
    print_(f"\nNeurons in subclass 3: {subclass_3}")

    # Get neurons expressing lin-39
    lin39_neurons = get_neurons_by_hox_gene("lin-39")
    print_(f"\nNeurons expressing lin-39: {lin39_neurons}")

    # Export to dict format
    print_("\nExport format for OpenWorm integration:")
    import json

    exported = export_to_dict()
    print_(json.dumps(exported, indent=2))
