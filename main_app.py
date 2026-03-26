import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return None

def show_visual(df):
    plt.figure(figsize=(8, 5))
    plt.bar(df['Name'], df['Value'], color='teal')
    plt.title("Data Visualization")
    plt.ylabel("Scores")
    plt.show()

def run_search(df):
    query = input("\nEnter name to search: ")
    result = df[df['Name'].str.contains(query, case=False, na=False)]
    if not result.empty:
        print("\n--- Results Found ---")
        print(result.to_string(index=False))
    else:
        print("No matches found.")

def main():
    file_name = 'data.csv'
    df = load_data(file_name)
    
    if df is None:
        return

    while True:
        print("\n===== DATA DASHBOARD MENU =====")
        print("1. View Raw Data")
        print("2. Search for Entry")
        print("3. Generate Visual Chart")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            print("\n", df)
        elif choice == '2':
            run_search(df)
        elif choice == '3':
            show_visual(df)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
