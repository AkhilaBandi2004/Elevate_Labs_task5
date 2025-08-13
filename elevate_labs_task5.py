import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Define the file path ---
file_name = 'health_data.csv'


# --- 2. Load and Clean the Data from the file ---
column_names = ['Duration', 'Date', 'Pulse', 'Maxpulse', 'Calories']
try:
    health_df = pd.read_csv(file_name, header=None, names=column_names)
    print(f"Successfully loaded data from {file_name}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    print("Please make sure the CSV file is in the same directory as the script.")
    # Exit the script if the file doesn't exist.
    exit()

print("\n--- Initial Data (First 5 Rows) ---")
print(health_df.head())
print("\n" + "="*40 + "\n")

# --- Data Cleaning Steps ---
duration_mode = health_df['Duration'].mode()[0]
health_df.loc[health_df.Duration == 450, 'Duration'] = duration_mode
health_df.dropna(subset=['Date'], inplace=True)
health_df['Date'] = health_df['Date'].astype(str).str.replace("'", "")
health_df['Date'] = pd.to_datetime(health_df['Date'], format='%Y/%m/%d')
mean_calories = health_df['Calories'].mean()
health_df['Calories'].fillna(mean_calories, inplace=True)
health_df.drop_duplicates(inplace=True)
health_df.reset_index(drop=True, inplace=True)

print("--- Cleaned Data (First 5 Rows) ---")
print(health_df.head())
print("\n" + "="*40 + "\n")


# --- 3. Analyze Data ---
health_df = health_df.sort_values(by='Date')
avg_calories_by_duration = health_df.groupby('Duration')['Calories'].mean()
print("--- Average Calories Burned by Workout Duration ---")
print(avg_calories_by_duration)
print("\n" + "="*40 + "\n")


# --- 4. Visualize Results ---
print("Generating Line Plot: Calories Burned in December 2020...")
plt.figure(figsize=(12, 6))
plt.plot(health_df['Date'], health_df['Calories'], marker='o', linestyle='-', color='teal')
plt.title('Calories Burned Over Time (Dec 2020)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Calories Burned', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print("\nGenerating Bar Chart: Average Calories by Workout Duration...")
plt.figure(figsize=(10, 6))
avg_calories_by_duration.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Average Calories Burned per Workout Duration', fontsize=16)
plt.xlabel('Workout Duration (Minutes)', fontsize=12)
plt.ylabel('Average Calories Burned', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()