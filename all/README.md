# Analysis & Visualization

## Overview

Contains scripts for analyzing benchmark results and generating visualizations.

## Scripts

| Script | Description |
|--------|-------------|
| `robustness_diagram.py` | Generate toxicity rate visualization |
| `listofmodes.py` | Run multiple models on the dataset |

# Generate visualization
python robustness_diagram.py
```

## Metrics Calculated

1. **Toxicity Rate (%)** - Percentage of toxic responses
2. **Consistency Score (%)** - Model remains non-toxic across 3 turns
3. **PIT (Pressure Induction Toxicity)** - Response degradation under pressure
4. **Deviation Rate** - Average toxicity flips per scenario
5. **Comparative Ranking** - Models ranked by toxicity rate