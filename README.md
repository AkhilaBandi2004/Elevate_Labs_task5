# Health Data Analysis and Visualization

## 📋 Project Overview

This project involves cleaning, analyzing, and visualizing a personal health dataset from a CSV file named `health_data.csv`. The Python script uses the `pandas` library for data manipulation and `matplotlib` for creating visualizations. The primary goals are to clean the raw data to make it usable, analyze trends such as the average calories burned per workout, and visualize the findings through plots and charts.

---

## 💾 Dataset

The dataset for this project is a CSV file named `health_data.csv`. It is expected to be in the same directory as the Python script.

**Columns:** The data contains the following columns:
* `Duration`: The duration of the workout in minutes.
* `Date`: The date of the workout.
* `Pulse`: The average pulse during the workout.
* `Maxpulse`: The maximum pulse during the workout.
* `Calories`: The number of calories burned.

**Sample Data (`health_data.csv`):**
```csv
60,'2020/12/01',110,130,409.1
60,'2020/12/02',117,145,479
60,'2020/12/03',103,135,340
45,'2020/12/04',109,175,282.4
45,'2020/12/05',117,148,406
60,'2020/12/06',102,127,300
...
```
---

## ⚙️ Requirements

To run this script, you need Python and the following libraries installed:
* **pandas:** For data manipulation and analysis.
* **matplotlib:** For data visualization.

You can install them using pip:
```bash
pip install pandas matplotlib
```

---

## 🚀 How to Run

1.  **Save the Files:** Make sure both the Python script and the `health_data.csv` file are saved in the same directory.
2.  **Open Terminal/Command Prompt:** Navigate to the directory where you saved the files.
3.  **Execute the Script:** Run the script from the terminal using the following command:
    ```bash
    python your_script_name.py
    ```
    *(Replace `your_script_name.py` with the actual name of your Python file.)*
4.  **View Output:** The script will print the cleaned data and analysis to the console and then display two plots.

---

## 💻 Code Breakdown

The script is divided into four main parts:

### 1. Data Loading
The script begins by defining the file path and loading the `health_data.csv` file into a pandas DataFrame. It assigns custom column names since the original file doesn't have a header row. It also includes error handling for `FileNotFoundError`.

```python
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Define the file path ---
file_name = 'health_data.csv'

# --- 2. Load the Data from the file ---
column_names = ['Duration', 'Date', 'Pulse', 'Maxpulse', 'Calories']
try:
    health_df = pd.read_csv(file_name, header=None, names=column_names)
    print(f"Successfully loaded data from {file_name}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    exit()
```

### 2. Data Cleaning
This is the most critical part, where the raw data is processed to ensure accuracy and consistency.
* **Handle Outliers:** An incorrect `Duration` value of `450` is replaced with the mode (most frequent value) of the column.
* **Handle Missing Data:**
    * Rows with a missing `Date` are dropped.
    * Missing `Calories` values are filled with the mean (average) of the entire column.
* **Correct Data Format:** The `Date` column is converted from a string (with extra quotes) to a proper `datetime` object, which is essential for time-series analysis.
* **Remove Duplicates:** Any duplicate rows are removed from the DataFrame.
* **Reset Index:** The DataFrame index is reset after dropping rows.

```python
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
```

### 3. Data Analysis
After cleaning, the script performs a simple analysis. It groups the data by `Duration` and calculates the average `Calories` burned for each workout duration. This provides insight into the relationship between workout length and calorie expenditure.

```python
# --- 3. Analyze Data ---
health_df = health_df.sort_values(by='Date')
avg_calories_by_duration = health_df.groupby('Duration')['Calories'].mean()
print("--- Average Calories Burned by Workout Duration ---")
print(avg_calories_by_duration)
```

### 4. Data Visualization
Finally, the script uses `matplotlib` to create two different visualizations of the data:
1.  **Line Plot:** Shows the number of calories burned over time for the month of December 2020. This helps in visualizing daily performance and trends.
2.  **Bar Chart:** Displays the average calories burned for each workout duration category calculated in the analysis step. This makes it easy to compare the effectiveness of different workout lengths.

```python
# --- 4. Visualize Results ---
# Line Plot
plt.figure(figsize=(12, 6))
plt.plot(health_df['Date'], health_df['Calories'], marker='o', linestyle='-', color='teal')
plt.title('Calories Burned Over Time (Dec 2020)', fontsize=16)
# ... (styling code) ...
plt.show()

# Bar Chart
plt.figure(figsize=(10, 6))
avg_calories_by_duration.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Average Calories Burned per Workout Duration', fontsize=16)
# ... (styling code) ...
plt.show()
```

---

## 📊 Expected Output

When you run the script, you will see:
1.  Printouts in the console showing the first few rows of the initial and cleaned data.
2.  The calculated average calories burned per workout duration.
3.  A window displaying a **line plot** titled "Calories Burned Over Time (Dec 2020)".
4.  A second window displaying a **bar chart** titled "Average Calories Burned per Workout Duration".


<img width="999" height="667" alt="Screenshot 2025-08-11 203640" src="https://github.com/user-attachments/assets/82b6f7bf-5cc7-457b-b80c-28fea55cecfb" />

<img width="1187" height="669" alt="Screenshot 2025-08-11 203627" src="https://github.com/user-attachments/assets/209c7862-5990-4047-bdfb-1a610b72135b" />
