#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example script demonstrating integration of DD neuron molecular profiles
with the OpenWorm connectome.

This script shows how to use the DD molecular profiles to add a molecular
identity layer to the anatomical representation of DD neurons in the connectome.
"""

from cect.DDNeuronMolecularProfiles import (
    DD_MOLECULAR_PROFILES,
    get_dd_molecular_profile,
    get_neurons_by_subclass,
    get_neurons_by_hox_gene,
    get_dd_subclass_summary,
    export_to_dict,
)
from cect import print_


def demonstrate_basic_usage():
    """Demonstrate basic usage of the DD molecular profiles API."""
    print_("\n" + "=" * 80)
    print_("BASIC USAGE EXAMPLES")
    print_("=" * 80)

    # Example 1: Get profile for a specific neuron
    print_("\n1. Getting molecular profile for a specific DD neuron:")
    dd4_profile = get_dd_molecular_profile("DD4")
    print_("   DD4 molecular profile:")
    print_(f"   - Neuron: {dd4_profile.neuron_name}")
    print_(f"   - Subclass: {dd4_profile.subclass}")
    print_(f"   - Hox genes: {', '.join(dd4_profile.hox_genes)}")

    # Example 2: Query by subclass
    print_("\n2. Getting all neurons in molecular subclass 2:")
    subclass_2 = get_neurons_by_subclass(2)
    print_(f"   Neurons in subclass 2: {', '.join(subclass_2)}")
    for neuron in subclass_2:
        profile = get_dd_molecular_profile(neuron)
        print_(f"   - {neuron}: Hox genes = {', '.join(profile.hox_genes)}")

    # Example 3: Query by Hox gene
    print_("\n3. Getting all neurons expressing mab-5:")
    mab5_neurons = get_neurons_by_hox_gene("mab-5")
    print_(f"   Neurons expressing mab-5: {', '.join(mab5_neurons)}")


def demonstrate_connectome_integration():
    """Demonstrate how to integrate molecular profiles with connectome data."""
    print_("\n" + "=" * 80)
    print_("CONNECTOME INTEGRATION EXAMPLE")
    print_("=" * 80)

    print_("\n1. Export molecular profiles for connectome integration:")
    profiles_dict = export_to_dict()

    print_("\n   Example: Enhanced neuron representation with molecular identity")
    for neuron_name in ["DD1", "DD2", "DD4", "DD6"]:
        profile = profiles_dict[neuron_name]
        print_(f"\n   {neuron_name}:")
        print_("     - Anatomical class: DD-class motor neuron")
        print_(f"     - Molecular subclass: {profile['subclass']}")
        print_(f"     - Hox gene expression: {', '.join(profile['hox_genes'])}")
        print_("     - Location: Ventral cord")


def demonstrate_analysis_queries():
    """Demonstrate analytical queries using molecular profiles."""
    print_("\n" + "=" * 80)
    print_("ANALYTICAL QUERIES")
    print_("=" * 80)

    # Analysis 1: Compare subclasses
    print_("\n1. Molecular subclass composition:")
    summary = get_dd_subclass_summary()
    for subclass in sorted(summary.keys()):
        info = summary[subclass]
        print_(f"   Subclass {subclass}:")
        print_(f"     - Number of neurons: {len(info['neurons'])}")
        print_(f"     - Neurons: {', '.join(info['neurons'])}")
        print_(f"     - Hox genes: {', '.join(info['hox_genes'])}")

    # Analysis 2: Hox gene co-expression patterns
    print_("\n2. Hox gene co-expression analysis:")
    hox_genes = ["lin-39", "mab-5", "egl-5"]
    for gene in hox_genes:
        neurons = get_neurons_by_hox_gene(gene)
        print_(f"   {gene}: expressed in {len(neurons)} neurons ({', '.join(neurons)})")

    # Analysis 3: Identify unique molecular signatures
    print_("\n3. Unique molecular signatures:")
    signatures = {}
    for neuron, profile in DD_MOLECULAR_PROFILES.items():
        signature = tuple(sorted(profile.hox_genes))
        if signature not in signatures:
            signatures[signature] = []
        signatures[signature].append(neuron)

    print_(f"   Found {len(signatures)} unique Hox gene combinations:")
    for i, (signature, neurons) in enumerate(sorted(signatures.items()), 1):
        print_(f"   {i}. {' + '.join(signature)}: {', '.join(sorted(neurons))}")


def demonstrate_research_applications():
    """Demonstrate potential research applications."""
    print_("\n" + "=" * 80)
    print_("RESEARCH APPLICATIONS")
    print_("=" * 80)

    print_(
        """
1. Correlation with connectivity patterns:
   - Compare synaptic connectivity between neurons in the same molecular subclass
   - Investigate whether molecular identity predicts connectivity patterns
   
2. Functional analysis:
   - Map behavioral functions to molecular subclasses
   - Investigate role of Hox genes in motor circuit organization
   
3. Developmental studies:
   - Trace how molecular identity relates to developmental lineage
   - Study how Hox gene expression establishes motor neuron diversity
   
4. Comparative analysis:
   - Extend molecular classification to other motor neuron classes (DA, DB, VD)
   - Compare molecular organization across different neuron types
   
5. Predictive modeling:
   - Use molecular profiles to predict neuron properties
   - Build models integrating molecular and connectivity data
"""
    )


def main():
    """Main demonstration function."""
    print_("\n" + "=" * 80)
    print_("DD NEURON MOLECULAR PROFILES - INTEGRATION DEMONSTRATION")
    print_("Based on Smith et al. (2024)")
    print_("=" * 80)

    # Run demonstrations
    demonstrate_basic_usage()
    demonstrate_connectome_integration()
    demonstrate_analysis_queries()
    demonstrate_research_applications()

    print_("\n" + "=" * 80)
    print_("SUMMARY")
    print_("=" * 80)
    print_(
        """
This example demonstrates how DD neuron molecular profiles can be integrated
with the OpenWorm connectome to add a molecular identity layer to anatomical
representations. The implementation provides:

- 4 distinct molecular subclasses based on Hox gene expression
- Comprehensive API for querying molecular profiles
- Integration-ready data structures
- Support for analytical and research applications

The molecular profiles enable researchers to:
- Correlate molecular identity with connectivity patterns
- Investigate functional specialization within motor neuron classes
- Study the role of developmental gene expression in circuit organization
- Build predictive models integrating multiple data modalities
"""
    )


if __name__ == "__main__":
    main()
