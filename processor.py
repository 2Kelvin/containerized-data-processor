import pandas as pd
import os

def process_data(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    try:
        # Load the CSV
        df = pd.read_csv(input_file)
        
        # Perform some basic processing
        # This assumes your CSV has a column you want to describe/summarize
        summary = df.describe()
        row_count = len(df)
        
        # Write results to a file
        with open(output_file, 'w') as f:
            f.write("--- Data Processing Report ---\n")
            f.write(f"Total Rows Processed: {row_count}\n\n")
            f.write("Summary Statistics:\n")
            f.write(summary.to_string())
            
        print(f"Success! Results saved to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Standard paths for the script to look for inside its environment
    IN_PATH = "input.csv"
    OUT_PATH = "output.txt"
    
    process_data(IN_PATH, OUT_PATH)