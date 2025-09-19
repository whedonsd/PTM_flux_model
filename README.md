# Histone PTM Flux Model

A Python toolkit for representing histone post-translational modification (PTM) states as a graph, detecting adjacency between states, and inferring probable **fluxes** (transitions) between them from observed changes in abundance over time.

---

## 🚀 Project Goals

1. **Nodes**: Represent histone PTM states as nodes in a graph.
   - Each node corresponds to a unique string (e.g., `H3K9me1 + H3K14ac`).
   - Each node carries **abundance values** at multiple time points.

2. **Edges**: Automatically detect edges between nodes that differ by exactly **one modification**.
   - Example: `H3K9me1` ↔ `H3K9me2`.
   - Must also handle adjacency between modified and unmodified states (e.g., `K9me1` ↔ `""`).

3. **Flux Inference**: Estimate probable fluxes between nodes.
   - Based on observed changes in node abundances (`t0 → t1`).
   - Modeled as a **sparse system of linear equations** with conservation of weight.
   - Solved using **linear programming**.

4. **Scalability**: Handle 150–300 nodes with thousands of edges.
   - Exploit sparsity for performance.
   - Export intermediate results for manual inspection.

---

## 📂 Repository Structure

PTM-flux-model/
  - │
  - ├── data/
  - │   ├── nodes.txt              # exported list of histone states from R
  - │   └── abundances.csv         # abundances for each state at t0, t1, t2...
  - │
  - ├── src/
  - │   ├── parse_nodes.py         # parse node strings into modifications
  - │   ├── build_edges.py         # adjacency detection + edge validation
  - │   ├── flux_solver.py         # linear programming to infer fluxes
  - │   └── visualize_graph.py     # (optional) plotting with NetworkX
  - │
  - ├── tests/
  - │   ├── test_parse_nodes.py
  - │   ├── test_build_edges.py
  - │   └── test_flux_solver.py
  - │
  - ├── notebooks/
  - │   └── exploratory.ipynb      # Jupyter notebook for manual inspection
  - │
  - └── README.md                  # project description, goals, usage


---

## 🛠 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/PTM-flux-model.git
cd PTM-flux-model
pip install -r requirements.txt
