import pandas as pd
import matplotlib.pyplot as plt

def process_and_visualize(file_name):
    try:
        # 1. Load the data using Pandas
        # This treats the CSV file like a spreadsheet table
        df = pd.read_csv(file_name)

        # 2. Basic Data Analysis (Print to terminal)
        print("--- Data Summary ---")
        print(df.describe()) # Shows mean, min, max, etc.
        print("\n--- Top 3 Records ---")
        print(df.head(3))

        # 3. Create the Visualization
        # Assuming the CSV has columns 'Name' and 'Value'
        plt.figure(figsize=(10, 6))
        plt.bar(df['Name'], df['Value'], color='skyblue', edgecolor='navy')
        
        plt.xlabel('Category Name')
        plt.ylabel('Numerical Value')
        plt.title('Data Distribution from CSV Source')
        plt.xticks(rotation=45) # Rotates labels if they are long
        
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # To run this, you must have a file named 'data.csv' in the same folder
    process_and_visualize('data.csv')
