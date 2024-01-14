import os
import pandas as pd
from glob import glob

# Get a list of all output files in the current directory with a .tsv extension
output_files = glob('*.tsv')

# Read input.bed file
input_bed_path = 'input.bed'
input_bed_df = pd.read_csv(input_bed_path, sep='\t', header=None, names=['Chrom', 'Start', 'End', 'Gene', 'Somefield', 'Somefield2'])

# Initialize empty list to store values for the final output
final_data = []

# Loop through each .tsv file
input_bed_df = input_bed_df.astype(str)


# Create a DataFrame
summed_df = pd.DataFrame(columns=['min', 'files'])

for tsv_file in output_files:
    print("Reading file " + tsv_file)
    tsv_df = pd.read_csv(tsv_file, sep='\t')
    tsv_df = tsv_df.astype(str)

    # Merge DataFrames based on 'Chrom', 'Start', and 'End'
    merged_df = pd.merge(input_bed_df, tsv_df, how='inner', on=['Chrom', 'Start', 'End'])
    merged_df = merged_df.drop('Depths', axis=1)

    # If any matching lines were found, add them to the final_data list
    if not merged_df.empty:
        merged_df['files'] = tsv_file
        if summed_df['min'].empty or int(summed_df['min'][0]) > int(merged_df['Min'][0]):
            print("Why doesn't this work?")
            summed_df['min'] = int (merged_df['Min'].iloc[0])
            print(summed_df['min'])

             
        summed_df['files'] = summed_df['files'] + tsv_file + ", "

final_data.append(summed_df)

# Concatenate the matching lines into a final DataFrame
final_df = pd.concat(final_data, ignore_index=True)

# Print the final DataFrame
print(final_df)
