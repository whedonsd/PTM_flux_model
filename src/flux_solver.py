import numpy as np
from scipy.optimize import linprog

# Define observed changes in node abundances
Delta_x = [ #these values should be derived from the difference between two adjacent columns for rows in abundances.csv that contain a shared string element (e.g. H3K9me1 (+1%), H3K9me2+K14ac+K27me2 (-1%), H3K9me2+K27me2 (-1%))
]
  
# Define the flux coefficients in conservation equations
A_eq = [ 
]
  
# Right-hand side: observed changes
b_eq = Delta_x

# Bounds for fluxes (non-negative)
bounds = [(0, None) for _ in range()]

# Solve for fluxes using linear programming
result = linprog(c=[], A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Output the fluxes
print("Fluxes:", result.x)
