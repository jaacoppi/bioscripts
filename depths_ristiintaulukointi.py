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
for tsv_file in output_files:
    print("Reading file " + tsv_file)
    tsv_df = pd.read_csv(tsv_file, sep='\t')

    input_bed_df[['Chrom', 'Start', 'End']] = input_bed_df[['Chrom', 'Start', 'End']].astype(tsv_df[['Chrom', 'Start', 'End']].dtypes)

    # Merge DataFrames based on 'Chrom', 'Start', and 'End'
    merged_df = pd.merge(input_bed_df, tsv_df, how='inner', on=['Chrom', 'Start', 'End'])

    # If any matching lines were found, add them to the final_data list
    if not merged_df.empty:
        final_data.append(merged_df)

# Concatenate the matching lines into a final DataFrame
final_df = pd.concat(final_data, ignore_index=True)

# Print the final DataFrame
print(final_df)
