import pandas as pd

def search_data(file_name):
    try:
        # Load the CSV
        df = pd.read_csv(file_name)
        
        print("--- Data Search Tool ---")
        query = input("Enter the Name you want to find: ").strip()

        # Filter the DataFrame
        # This looks for any row where the 'Name' column matches the user's input
        result = df[df['Name'].str.contains(query, case=False, na=False)]

        if not result.empty:
            print("\nMatch found:")
            print(result.to_string(index=False))
        else:
            print(f"\nNo results found for '{query}'.")

    except FileNotFoundError:
        print("Error: data.csv not found. Please create it first.")

if __name__ == "__main__":
    search_data('data.csv')
