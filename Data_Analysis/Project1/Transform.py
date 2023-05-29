import csv
import gzip

# Specify the path to the input TSV file (.tsv.gz)
input_file_path = 'title.ratings.tsv.gz'

# Specify the path to the output CSV file
output_file_path = 'title.ratings.csv'

# Open the input TSV file using gzip
with gzip.open(input_file_path, 'rt') as tsv_file:
  # Open the output CSV file
  with open(output_file_path, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Read the TSV file line by line
    for line in tsv_file:
      # Split the line using tabs as the delimiter
      row = line.strip().split('\t')

      # Write the row to the CSV file
      csv_writer.writerow(row)

# Print a success message
print(
  f"Conversion complete! TSV file '{input_file_path}' converted to CSV file '{output_file_path}'."
)
