# DD Neuron Molecular Profiles

## Overview

This document describes the molecular classification of DD-class motor neurons (DD1-DD6) based on their combinatorial Hox gene expression patterns, as revealed in the research by Smith et al. (2024).

## Background

The study reveals that the six DD neurons are not a single molecular class but can be divided into distinct subclasses based on their combinatorial Hox gene expression codes. This provides a molecular identity layer that can be integrated with the anatomical representation of the connectome.

## Molecular Subclasses

The DD neurons are organized into four distinct molecular subclasses:

### Subclass 1: DD1
- **Neurons**: DD1
- **Hox genes**: lin-39
- **Description**: Expresses only lin-39, representing the most anterior molecular identity

### Subclass 2: DD2 and DD3
- **Neurons**: DD2, DD3
- **Hox genes**: lin-39, mab-5
- **Description**: Co-expresses lin-39 and mab-5, representing a mid-anterior molecular identity

### Subclass 3: DD4 and DD5
- **Neurons**: DD4, DD5
- **Hox genes**: lin-39, mab-5, egl-5
- **Description**: Co-expresses all three Hox genes (lin-39, mab-5, and egl-5), representing a mid-posterior molecular identity

### Subclass 4: DD6
- **Neurons**: DD6
- **Hox genes**: egl-5
- **Description**: Expresses only egl-5, representing the most posterior molecular identity

## Hox Gene Expression Patterns

The following table summarizes the Hox gene expression for each DD neuron:

| Neuron | lin-39 | mab-5 | egl-5 | Subclass |
|--------|--------|-------|-------|----------|
| DD1    | ✓      |       |       | 1        |
| DD2    | ✓      | ✓     |       | 2        |
| DD3    | ✓      | ✓     |       | 2        |
| DD4    | ✓      | ✓     | ✓     | 3        |
| DD5    | ✓      | ✓     | ✓     | 3        |
| DD6    |        |       | ✓     | 4        |

## Implementation

The molecular profiles are implemented in the `cect.DDNeuronMolecularProfiles` module, which provides:

### Data Structures

- `DDMolecularProfile`: A class representing the molecular profile of a DD neuron
- `DD_MOLECULAR_PROFILES`: A dictionary mapping neuron names to their molecular profiles

### API Functions

- `get_dd_molecular_profile(neuron_name)`: Get the molecular profile for a specific DD neuron
- `get_neurons_by_subclass(subclass)`: Get all DD neurons in a specific subclass
- `get_neurons_by_hox_gene(hox_gene)`: Get all DD neurons expressing a specific Hox gene
- `get_dd_subclass_summary()`: Get a summary of all subclasses
- `export_to_dict()`: Export profiles in a format suitable for OpenWorm integration

## Usage Examples

### Python API

```python
from cect.DDNeuronMolecularProfiles import (
    get_dd_molecular_profile,
    get_neurons_by_subclass,
    get_neurons_by_hox_gene,
    export_to_dict
)

# Get profile for a specific neuron
dd4_profile = get_dd_molecular_profile("DD4")
print(dd4_profile.neuron_name)  # "DD4"
print(dd4_profile.subclass)      # 3
print(dd4_profile.hox_genes)     # ["egl-5", "lin-39", "mab-5"]

# Get all neurons in subclass 3
subclass_3_neurons = get_neurons_by_subclass(3)
print(subclass_3_neurons)  # ["DD4", "DD5"]

# Get all neurons expressing lin-39
lin39_neurons = get_neurons_by_hox_gene("lin-39")
print(lin39_neurons)  # ["DD1", "DD2", "DD3", "DD4", "DD5"]

# Export for OpenWorm integration
profiles_dict = export_to_dict()
```

### Command Line

Run the module directly to see a summary of all profiles:

```bash
python -m cect.DDNeuronMolecularProfiles
```

## Testing

Comprehensive tests are provided in `cect/tests/test_dd_molecular_profiles.py`. Run tests with:

```bash
python -m pytest cect/tests/test_dd_molecular_profiles.py -v
```

## Integration with OpenWorm

The molecular profiles can be integrated with the existing OpenWorm connectome by using the `export_to_dict()` function, which returns a dictionary structure that maps each DD neuron to its molecular characteristics:

```json
{
  "DD1": {
    "neuron_name": "DD1",
    "hox_genes": ["lin-39"],
    "subclass": 1
  },
  "DD2": {
    "neuron_name": "DD2",
    "hox_genes": ["lin-39", "mab-5"],
    "subclass": 2
  },
  ...
}
```

This data structure adds a molecular identity layer to the anatomical representation of each DD neuron in the connectome.

## Reference

Smith et al. (2024). Research paper revealing combinatorial Hox gene expression codes in DD-class motor neurons (Figure 3C).

## Future Work

- Integration with the OpenWorm connectome visualization tools
- Extension to other motor neuron classes (DA, DB, VD, etc.)
- Correlation of molecular profiles with connectivity patterns
- Integration with gene expression databases
