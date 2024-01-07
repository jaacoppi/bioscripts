import os
import pandas as pd
from glob import glob

# Get a list of all output files in the current directory with a .tsv extension
output_files = glob('*.tsv')

# Read input.bed file
input_bed_path = 'input.bed'
input_bed_df = pd.read_csv(input_bed_path, sep='\t', header=None, names=['Chrom', 'Start', 'End', 'Gene'])

# Initialize empty lists to store values for the final output
final_data = []

# Loop through each line in the input.bed file
# index + row = kökkö, mutta chatGPT ei osannut parempaa
for index, row in input_bed_df.iterrows():
    end = row{0]

    # Initialize lists to store values for the current line in input.bed
    min_values = []
    max_values = []
    avg_values = []
    median_values = []

    # Loop through each output file and find matching lines
    for output_file in output_files:
        df = pd.read_csv(output_file, sep='\t', names=['Chrom', 'Start', 'End', 'Gene'])

        # Find matching line based on the first 4 columns
        print("Searching for " + str(end) + ".")
        print("asdf")
        print(df['Gene'])
        print("asdf")
        match = df[df['End'] == end]
        exit(0)

        if not match.empty:
            print("MATCH at " + end)
            exit(0)

            # Append values to the lists
            min_values.append(match['Min'].values[0])
            max_values.append(match['Max'].values[0])
            avg_values.append(match['Avg'].values[0])
            median_values.append(match['Median'].values[0])
            # Calculate aggregated values for the current line in input.bed
            final_data.append([gene, chrom, start, end, min(min_values), max(max_values), sum(avg_values) / len(avg_values), sorted(median_values)[len(median_values)/2]])

# Create the final output dataframe
final_output_df = pd.DataFrame(final_data, columns=['Gene', 'Chrom', 'Start', 'End', 'samples_Min', 'samples_Max', 'samples_Avg', 'samples_Median'])

# Save the result to a new file called ristiintaulukointi.tsv
output_file_path = 'ristiintaulukointi.tsv'
final_output_df.to_csv(output_file_path, sep='\t', index=False)

print(f"Result saved to {output_file_path}")
