"""
flux_solver.py

Infer probable flux between histone states based on changes in abundance.
Uses linear programming (minimizing total flux) subject to conservation of weight.
"""

import numpy as np
from scipy.optimize import linprog
import pandas as pd

NODES_FILE = "data/abundances.csv"
EDGES_FILE = "data/validated_edges.txt"
OUTPUT_FILE = "data/fluxes.csv"


def load_data():
    """Load node abundances and edges."""
    nodes_df = pd.read_csv(NODES_FILE)  # Node_ID, t0, t1
    edges = []
    with open(EDGES_FILE, "r") as f:
        for line in f:
            src, tgt = line.strip().split("\t")
            edges.append((src, tgt))
    return nodes_df, edges


def build_flux_system(nodes_df, edges):
    """
    Build the conservation equations for flux inference.
    
    Args:
        nodes_df (pd.DataFrame): Node abundances with t0, t1.
        edges (list): List of (source, target) edges.
    
    Returns:
        (A_eq, b_eq, edge_list): Coefficient matrix, RHS vector, and edge index.
    """
    node_list = list(nodes_df["Node_ID"])
    node_index = {node: i for i, node in enumerate(node_list)}
    delta_x = nodes_df["t1"] - nodes_df["t0"]

    num_nodes = len(node_list)
    num_edges = len(edges)

    A_eq = np.zeros((num_nodes, num_edges))
    b_eq = delta_x.to_numpy()

    for j, (src, tgt) in enumerate(edges):
        A_eq[node_index[src], j] -= 1  # Outgoing flux
        A_eq[node_index[tgt], j] += 1  # Incoming flux

    return A_eq, b_eq, edges


def solve_flux(A_eq, b_eq, edges):
    """Solve for fluxes using linear programming."""
    c = np.ones(len(edges))  # Objective: minimize total flux
    bounds = [(0, None) for _ in edges]  # Flux must be non-negative

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

    if not result.success:
        raise RuntimeError(f"Flux optimization failed: {result.message}")

    fluxes = {edges[i]: result.x[i] for i in range(len(edges))}
    return fluxes


def main():
    nodes_df, edges = load_data()
    A_eq, b_eq, edge_list = build_flux_system(nodes_df, edges)
    fluxes = solve_flux(A_eq, b_eq, edge_list)

    # Save output
    flux_df = pd.DataFrame(
        [(src, tgt, flux) for (src, tgt), flux in fluxes.items()],
        columns=["source", "target", "flux"]
    )
    flux_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Flux results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
