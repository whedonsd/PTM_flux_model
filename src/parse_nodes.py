from itertools import combinations

# Load nodes from a text file
with open("nodes.txt", "r") as file:
    nodes = [line.strip() for line in file]

# Function to split node string into modifications
def parse_modifications(node):
    return set(node.split(" + "))

# Function to check if two nodes differ by a single modification
def is_adjacent(node1, node2):
    mods1 = parse_modifications(node1)
    mods2 = parse_modifications(node2)
    difference = mods1.symmetric_difference(mods2)
    return len(difference) == 1

# Identify edges between adjacent nodes
edges = []
for node1, node2 in combinations(nodes, 2):  # Pairwise comparison
    if is_adjacent(node1, node2):
        edges.append((node1, node2))

# Print edges
print("Detected edges:")
for edge in edges:
    print(f"{edge[0]} -> {edge[1]}")

# Optional: Save edges to a file
with open("edges.txt", "w") as f:
    for edge in edges:
        f.write(f"{edge[0]}\t{edge[1]}\n")

