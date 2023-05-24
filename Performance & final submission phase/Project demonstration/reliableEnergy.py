"""
A Reliable Energy Consumption Analysis System For Energy-Efficient Appliances
"""

import pandas as pd

def load_data(file_path):
    """
    Load energy consumption data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pandas.DataFrame: Loaded data as a DataFrame.
    """
    data = pd.read_csv(file_path)
    return data

def analyze_energy_consumption(data):
    """
    Analyze energy consumption data for energy-efficient appliances.
    
    Args:
        data (pandas.DataFrame): Energy consumption data.
    """
    # Perform data analysis here
    # Calculate average energy consumption, identify peak usage, etc.
    # You can use pandas methods like groupby, mean, max, etc.
    # Example:
    avg_consumption = data.groupby('appliance')['energy_consumption'].mean()
    peak_usage = data.groupby('appliance')['energy_consumption'].max()
    
    # Display analysis results
    print("Average Energy Consumption:")
    print(avg_consumption)
    print("\nPeak Usage:")
    print(peak_usage)

def main():
    # Step 1: Load data
    file_path = "energy_consumption_data.csv"
    data = load_data(file_path)
    
    # Step 2: Analyze energy consumption
    analyze_energy_consumption(data)

# Run the main function
if __name__ == "__main__":
    main()
