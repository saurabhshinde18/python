import numpy as np
import matplotlib.pyplot as plt

# Sample data: average sales in different regions (in $1000s)
regions = ['North', 'South', 'East', 'West']
avg_sales = [25, 30, 22, 27]  # Average sales in $1000s
std_dev = [3, 4, 2.5, 3.5]    # Standard deviation in $1000s

# Plotting
x_pos = np.arange(len(regions))

plt.figure(figsize=(8, 6))
bars = plt.bar(x_pos, avg_sales, yerr=std_dev, capsize=10, color='skyblue', edgecolor='black',
               error_kw=dict(elinewidth=2, ecolor='gray'))

# Customizing
plt.xticks(x_pos, regions)
plt.title("Average Monthly Sales by Region with Error Bars")
plt.ylabel("Sales ($1000s)")
plt.xlabel("Region")
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Adding data labels
for bar, value in zip(bars, avg_sales):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{value}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
