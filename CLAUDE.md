# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a NetworkX training project focused on graph analysis and event processing. The project demonstrates graph theory concepts using NetworkX library with interactive Marimo notebooks for visualization and analysis.

## Development Environment

- **Package Manager**: UV (uses `uv.lock` and `pyproject.toml`)
- **Python Version**: >=3.13
- **Interactive Notebooks**: Marimo framework for reactive notebooks

## Key Dependencies

- `networkx`: Core graph analysis library
- `marimo`: Interactive notebook framework
- `matplotlib`: Graph visualization
- `pandas`: Data manipulation for event processing
- `numpy`: Numerical operations
- `faker`: Test data generation
## Common Commands

```bash
# Install dependencies
uv sync

# Run notebooks in edit mode
marimo edit nx.py                   # Basic NetworkX graph operations
marimo edit event_processing.py     # Event chain analysis with graphs

# Run standalone Python scripts
python local/graph_components.py   # Graph connectivity analysis
```

## Project Structure

### Core Files
- `nx.py`: Basic NetworkX tutorial showing graph creation, visualization, and component analysis
- `event_processing.py`: Complex event chain analysis using graphs to model relationships
- `local/graph_components.py`: Standalone script demonstrating disconnected graph detection

### Data Files
- `scenarios/`: Event log data files (TSV format)
  - `real_event_log.tsv`: Main event data for processing
  - `aggregated.tsv`, `event_types.tsv`, `ideal_event_log.tsv`: Additional event datasets

### Generated Files
- `local/`: Contains HTML exports and Jupyter notebook versions
- `layouts/`: Presentation slides configuration

## Architecture

### Event Processing System
The `event_processing.py` implements a sophisticated event chain analysis:

1. **Event Dataclass** (`event_processing.py:45`): Represents individual events with date, ID, parent_id, who, and event type
2. **Chain Dataclass** (`event_processing.py:124`): Represents event chains with start/end events and parent relationships
3. **Graph Construction** (`event_processing.py:180`): Creates NetworkX DiGraph from event chains
4. **Path Analysis** (`event_processing.py:272`): Analyzes paths from roots to leaves, handling islands and disconnected components

### Graph Analysis Patterns
- Uses `nx.weakly_connected_components()` to find disconnected graph parts
- Implements DFS traversal with `nx.dfs_successors()`
- Categorizes nodes as: roots (no parents), leaves (no children), islands (isolated)
- Visualizes graphs using various layout algorithms (`draw_planar`, `draw_shell`)

## Key Concepts Demonstrated

1. **Graph Connectivity**: Both basic and weakly connected components
2. **Event Chain Modeling**: Converting temporal event data into graph structures
3. **Path Analysis**: Finding all paths between nodes, identifying root-to-leaf traversals
4. **Graph Visualization**: Multiple layout strategies for different graph types

## Development Notes

- Marimo notebooks use reactive cell execution - changes propagate automatically
- Event processing handles missing parent IDs and data type coercion
- Graph visualization adapts to different graph sizes and structures
- The project emphasizes both educational examples and practical event analysis
