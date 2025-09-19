# Function to check if two nodes differ by a single modification
def is_adjacent(node1, node2):
    mods1 = parse_modifications(node1)
    mods2 = parse_modifications(node2)
    difference = mods1.symmetric_difference(mods2)  # Check differing elements
    return len(difference) == 1

# Edge validation function
def validate_edges(edges):
    validated_edges = set()
    for edge in edges:
        source, target = edge
        
        # Self-loop check
        if source == target:
            print(f"Skipping self-loop: {source}")
            continue
        
        # Ensuring uniqueness and directionality (optional)
        if (target, source) in validated_edges:  # Avoid duplicate bidirectional edges
            print(f"Skipping duplicate edge: {source} -> {target}")
            continue
        
        # Add the validated edge
        validated_edges.add((source, target))
    
    return validated_edges

# Identify edges between adjacent nodes
edges = []
for node1, node2 in combinations(nodes, 2):  # Pairwise comparison
    if is_adjacent(node1, node2):
        edges.append((node1, node2))

# Validate edges to remove self-loops, duplicates
validated_edges = validate_edges(edges)

# Print validated edges
print("\nValidated edges:")
for edge in validated_edges:
    print(f"{edge[0]} -> {edge[1]}")

# Optional: Save edges to a file
with open("validated_edges.txt", "w") as f:
    for edge in validated_edges:
        f.write(f"{edge[0]}\t{edge[1]}\n")
