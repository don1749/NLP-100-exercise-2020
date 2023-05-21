import sys

# Get the value of N from the command-line argument
N = int(sys.argv[1])

# Open the input file
with open('popular-names.txt', 'r') as f:
    # Read the lines of the input file
    lines = f.readlines()

    # Calculate the number of lines per file
    lines_per_file = len(lines) // N

    # Split the lines into N pieces
    pieces = [lines[i:i + lines_per_file] for i in range(0, len(lines), lines_per_file)]

    # Write the pieces to the output files
    for i in range(N):
        with open(f'Output/splitOut{i + 1}.txt', 'w') as f_out:
            f_out.writelines(pieces[i])
