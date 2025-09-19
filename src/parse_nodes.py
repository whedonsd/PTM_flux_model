"""
parse_nodes.py

Utility functions to parse histone modification state strings into sets of modifications.
Example:
    "H3K9me1 + H3K14ac" -> {"H3K9me1", "H3K14ac"}
"""

def parse_modifications(node_str: str) -> set:
    """
    Parse a node string into a set of modification tokens.
    
    Args:
        node_str (str): Node label, e.g. "H3K9me1 + H3K14ac".
    
    Returns:
        set: A set of modifications, e.g. {"H3K9me1", "H3K14ac"}.
    """
    if not node_str or node_str.strip() == "":
        return set()
    return set(node_str.split(" "))


if __name__ == "__main__":
    # Example usage
    test_nodes = [
        "H3K9me1",
        "H3K9me2 + H3K14ac",
        "",
    ]
    for node in test_nodes:
        print(f"{node} -> {parse_modifications(node)}")
