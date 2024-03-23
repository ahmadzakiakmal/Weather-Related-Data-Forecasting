import csv

def copy_csv(input_file, output_file):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        with open(output_file, 'a', newline='') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)

# Example usage:
input_files = []
for i in range(19,31):
    input_files.append("./data/2023-11-" + str(i) + ".csv")
output_file = './data/join.csv'
for input_file in input_files:
  copy_csv(input_file, output_file)
