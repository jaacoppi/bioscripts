# read a file produced by samtools depth
# reference file as input.bed
# TODO: document output file

import pandas as pd
import sys

# Check if at least one command line argument is provided
if len(sys.argv) < 3:
    print("Usage: python3 depth_parser.py input output")
    sys.exit(1)

# Retrieve the name from the command line argument
depths_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Read input files
bed_file_path = 'input.bed'

print("Depths_parser: reading " + bed_file_path)
bed_df = pd.read_csv(bed_file_path, sep='\t', header=None, names=['Chrom', 'Start', 'End','Gene' , 'exonCount',  'MANE', 'nm'])
print("Depths_parser: reading " + depths_file_path)
depths_df = pd.read_csv(depths_file_path, sep='\t', header=None, names=['Chrom', 'Position', 'Depth'])

# Function to get depths for a given range
def get_depths_for_range(chrom, start, end):
    relevant_depths = depths_df[(depths_df['Chrom'] == chrom) & (depths_df['Position'] >= start) & (depths_df['Position'] <= end)]
    return relevant_depths['Depth'].tolist()

# Create a new dataframe with additional 'Depths' column
print("Depths_parser: creating dataframe")
output_df = bed_df.copy()
output_df['Depths'] = bed_df.apply(lambda row: get_depths_for_range(row['Chrom'], row['Start'], row['End']), axis=1)

# Function to calculate min, max, avg, and median from a list of depths
def calculate_stats(depths):
    if depths:
        return min(depths), max(depths), sum(depths) / len(depths), sorted(depths)[len(depths)//2]
    else:
        return None, None, None, None

# Create new columns for min, max, avg, median
print("Depths_parser: calculating stats")
output_df[['Min', 'Max', 'Avg', 'Median']] = pd.DataFrame(output_df['Depths'].apply(calculate_stats).tolist(), index=output_df.index)

# Reorder columns, moving 'Depths' to the last column
print("Depths_parser: reordering columns")
output_df = output_df[['Gene', 'Chrom', 'Start', 'End', 'Min', 'Max', 'Avg', 'Median', 'Depths']]

# Save the result to a new file with additional columns
print("Depths_parser: saving to " + output_file_path)
output_df.to_csv(output_file_path, sep='\t', index=False)

print("Depths_parser: Result saved to " + output_file_path)
