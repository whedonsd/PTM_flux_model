"""
build_edges.py

Detect adjacency between histone modification states and build validated edge lists.
"""

from itertools import combinations
from parse_nodes import parse_modifications

INPUT_FILE = "data/nodes.txt"
OUTPUT_FILE = "data/validated_edges.txt"


def is_adjacent(node1: str, node2: str) -> bool:
    """
    Check if two nodes differ by exactly one modification.
    
    Args:
        node1 (str), node2 (str): Node labels.
    
    Returns:
        bool: True if adjacent, False otherwise.
    """
    mods1 = parse_modifications(node1)
    mods2 = parse_modifications(node2)
    difference = mods1.symmetric_difference(mods2)
    return len(difference) == 1


def validate_edges(edges: list) -> set:
    """
    Validate edges by removing self-loops and duplicates.
    
    Args:
        edges (list): List of (source, target) tuples.
    
    Returns:
        set: Validated edges.
    """
    validated = set()
    for source, target in edges:
        if source == target:
            continue  # Skip self-loops
        if (target, source) in validated:
            continue  # Skip duplicate bidirectional edge
        validated.add((source, target))
    return validated


def main():
    # Load nodes
    with open(INPUT_FILE, "r") as file:
        nodes = [line.strip() for line in file if line.strip()]

    # Detect edges
    raw_edges = []
    for node1, node2 in combinations(nodes, 2):
        if is_adjacent(node1, node2):
            raw_edges.append((node1, node2))

    # Validate edges
    edges = validate_edges(raw_edges)

    # Save to file
    with open(OUTPUT_FILE, "w") as f:
        for src, tgt in edges:
            f.write(f"{src}\t{tgt}\n")

    print(f"Validated edges written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
