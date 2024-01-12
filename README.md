# Trail Navigator : Guides User traveling from one state to another with Approx Distance and Path 

## Overview

This Python script implements Dijkstra's algorithm to find the shortest path between two nodes in a graph. The graph is represented using edge information provided in a CSV file. Node names are also read from a separate CSV file for better readability.

## Features

- **Dijkstra's Algorithm:** Finds the shortest path and distance between two nodes in the graph.
- **CSV Input:** Reads edge information and node names from CSV files.
- **User Interaction:** Takes user input for starting and destination states.

## Prerequisites

- Python 3.x
- CSV file containing edge information (`edges.csv`).
- CSV file containing node names (`id.csv`).

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/dijkstras-shortest-path.git
   cd dijkstras-shortest-path
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python dijkstra_shortest_path.py
   ```

## Usage

1. Provide the file paths for the edge and node name CSV files.
2. Enter the starting and destination states when prompted.
3. View the shortest distance and path between the selected states.

## File Structure

- `dijkstra_shortest_path.py`: Main Python script implementing Dijkstra's algorithm.
- `edges.csv`: CSV file containing edge information (u, v, w).
- `id.csv`: CSV file containing node names.

## Contributing

Contributions are welcome! Please follow the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Heapq Documentation](https://docs.python.org/3/library/heapq.html)
- [CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Contributor Guidelines](CONTRIBUTING.md)