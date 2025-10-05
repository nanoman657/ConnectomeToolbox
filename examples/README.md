# ConnectomeToolbox Examples

This directory contains example scripts demonstrating how to use the ConnectomeToolbox.

## DD Molecular Integration Example

**File:** `dd_molecular_integration_example.py`

This example demonstrates how to integrate DD neuron molecular profiles with the OpenWorm connectome. It shows how to:

- Query molecular profiles for individual DD neurons
- Find neurons by molecular subclass
- Find neurons by Hox gene expression
- Export molecular profiles for connectome integration
- Perform analytical queries on the molecular data

### Running the Example

```bash
python examples/dd_molecular_integration_example.py
```

### What the Example Shows

The script demonstrates:

1. **Basic Usage**: How to retrieve molecular profiles and query by subclass or Hox gene
2. **Connectome Integration**: How to add molecular identity to anatomical neuron representations
3. **Analytical Queries**: How to analyze molecular subclass composition and gene co-expression
4. **Research Applications**: Potential use cases for the molecular profile data

### Output

The example outputs:
- Molecular profiles for individual DD neurons
- Neurons grouped by molecular subclass
- Hox gene expression patterns
- Enhanced neuron representations with molecular identity
- Analysis of unique molecular signatures

## Adding New Examples

When adding new examples:
1. Create a descriptive filename following the pattern `<topic>_example.py`
2. Add documentation at the top of the file explaining what the example demonstrates
3. Update this README with information about the new example
4. Ensure the example runs without errors
5. Format code with `ruff format` and check with `ruff check`
