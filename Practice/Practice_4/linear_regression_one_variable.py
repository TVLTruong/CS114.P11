import pandas as pd
import numpy as np
import sys
from decimal import Decimal, getcontext

# Set precision for Decimal
getcontext().prec = 28

# Read data from stdin using pandas
data = pd.read_csv(sys.stdin, header=None, names=['x', 'y'], dtype={'x': np.float64, 'y': np.float64})

# Convert to Decimal for high precision calculations
data['x'] = data['x'].apply(Decimal)
data['y'] = data['y'].apply(Decimal)

# Calculate necessary sums
n = Decimal(len(data))
sum_x = data['x'].sum()
sum_y = data['y'].sum()
sum_x2 = (data['x'] ** 2).sum()
sum_xy = (data['x'] * data['y']).sum()

# Calculate coefficients a and b
a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - a * sum_x) / n

# Print coefficients a and b
print(f"{a} {b}")
