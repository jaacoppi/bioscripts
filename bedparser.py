# Define the input and output file paths
input_file = 'input.txt'
output_file = 'output.txt'

# Function to extract nth element from a list
def extract_nth_element(values, n):
    if n < len(values):
        return values[n]
    else:
        return ''

# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        fields = line.strip().split('\t')
        if len(fields) == 6:
            # Extract the desired fields and split fields 2 and 3
            field1 = fields[0]
            field2 = fields[1].split(',')
            field3 = fields[2].split(',')
            field4 = fields[3]
            field5 = fields[4]
            field6 = fields[5]

            # Determine the maximum length for iterating
            max_len = max(len(field2), len(field3))

            # Iterate over the elements of field 2 and field 3
            for i in range(max_len):
                element2 = extract_nth_element(field2, i)
                element3 = extract_nth_element(field3, i)

                # Check for empty elements and skip the line if both are empty
                if element2 or element3:
                    outfile.write(f"{field1}\t{element2}\t{element3}\t{field4}\t{field5}\t{field6}\n")

print("Processing complete. Output saved to output.txt.")
