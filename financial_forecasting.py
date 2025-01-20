import numpy as np
import matplotlib.pyplot as plt

# Variables
product_price_i = 3000  # Initial price of your product
Xi = 2000  # Initial market size
X2i = 500000  # Initial revenue from targeted advertising
growth_rate = 0.08  # Annual growth rate
costs = 4800000  # Annual costs of investment and maintenance
years = np.arange(2025, 2050, 1)  # Time period of 10 years

# Sales forecast function
def X(t):
    return Xi * (1 + growth_rate)**t

# Product price function
def product_price(t):
    return product_price_i * (1 + growth_rate)**t

# Advertising revenue function
def X2(t):
    return X2i * (1 + growth_rate)**t

# Profit function
def y(t):
    return (X(t) * product_price(t) + X2(t)) - costs

# Calculate profits for each year
profits = y(years)

# Plot the profits over time
plt.plot(years, profits)
plt.xlabel('Years')
plt.ylabel('Profit')
plt.title('Profit over time')
plt.show()