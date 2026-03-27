import pandas as pd
import os

def get_grade(score):
    """Helper function to assign letter grades based on score."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

def process_data(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    try:
        # Load the CSV
        df = pd.read_csv(input_file)
        
        # Assign Grades
        df['grade'] = df['score'].apply(get_grade)
        
        # 1. Sort by score (Highest to Lowest)
        sorted_df = df[['id', 'name', 'score', 'grade']].sort_values(by='score', ascending=False)
        
        # 2. Calculate the total mean score
        mean_score = df['score'].mean()
        
        # Write results to the specified output path
        with open(output_file, 'w') as f:
            f.write("-" * 40 + "\n\n")
            f.write("Leaderboard: Highest to Lowest\n\n")
            f.write(sorted_df.to_string(index=False, justify='center', col_space=10))
            f.write("\n\n" + "-" * 40 + "\n\n")
            f.write(f"The total mean score is: {mean_score:.2f}\n")
            
        print(f"Success! Results saved to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    IN_PATH = os.path.join("data-files", "input.csv") # # fetch the input csv file to be processed in mounted data-files folder
    OUT_PATH = os.path.join("data-files", "output.txt") # place the processed output.txt file in data-files folder
    
    process_data(IN_PATH, OUT_PATH)