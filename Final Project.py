import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set a modern theme for the plots
sns.set_theme(style="whitegrid", palette="Set2", context="talk")

# Load the dataset from the 'Data' sheet of the Excel file
df = pd.read_excel(r"C:\Users\zaaaa\OneDrive\Υπολογιστής\New folder\Python Projects\Final Project\Filtered_Walmart_Sales_Data.xlsx", sheet_name='Data')

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# --- 1. Line Chart: Weekly Sales Over Time ---
# Group data by date and sum the weekly sales to get total sales per week
df_line = df.groupby('Date', as_index=False)['Weekly_Sales'].sum()

plt.figure(figsize=(14, 6))
sns.lineplot(data=df_line, x='Date', y='Weekly_Sales', linewidth=2.5, errorbar=None)
plt.title('Weekly Sales Over Time', fontsize=18, weight='bold')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Total Weekly Sales', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout() # Adjust plot to ensure everything fits without overlapping
plt.savefig('python_line_chart.png', dpi=300) # Save the figure
plt.show()


# --- 2. Bar Chart: Average Weekly Sales by Category ---
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Sales_Category', y='Weekly_Sales', estimator='mean', edgecolor='black')
plt.title('Average Weekly Sales by Category', fontsize=18, weight='bold')
plt.xlabel('Sales_Category', fontsize=14)
plt.ylabel('Average Weekly Sales', fontsize=14)
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig('python_bar_chart.png', dpi=300)
plt.show()


# --- 3. Histogram: Distribution of Weekly Sales by Category ---
plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x='Weekly_Sales',
    hue='Sales_Category', # Color bars based on the sales category
    bins=20,              # Group sales into 20 bins
    multiple='stack',     # Stack bars for 'High' and 'Low' categories
    alpha=0.7,
    edgecolor='black',
    legend=True
)
plt.title('Distribution of Weekly Sales by Category', fontsize=18, weight='bold')
plt.xlabel('Weekly Sales', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tight_layout()
plt.savefig('python_histogram.png', dpi=300)
plt.show()
