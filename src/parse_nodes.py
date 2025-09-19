"""
parse_nodes.py

Utility functions to parse histone modification state strings into sets of modifications.
Example:
    "T22phos K23me1 K27me2" -> {"T22phos", "K23me1", "K27me2"}
"""

def parse_modifications(node_str: str) -> set:
    """
    Parse a node string into a set of modification tokens.
    
    Args:
        node_str (str): Node label, e.g. "T22phos K23me1 K27me2".
    
    Returns:
        set: A set of modifications, e.g. {"T22phos", "K23me1", "K27me2"}.
    """
    if not node_str or node_str.strip() == "":
        return set()
    return {tok for tok in node_str.split(" ") if tok}


if __name__ == "__main__":
    # Example usage
    test_nodes = [
        "H3K9me1",
        "H3K9me2 H3K14ac",
        "",
    ]
    for node in test_nodes:
        print(f"{node} -> {parse_modifications(node)}")
