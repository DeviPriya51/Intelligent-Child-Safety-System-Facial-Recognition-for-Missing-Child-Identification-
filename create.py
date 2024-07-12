import csv



# Specify the CSV file path
csv_file_path = 'example.csv'

# Write data to CSV
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write header
    writer.writerow(['face descriptor', 'bounding box', 'name','img path'])


print(f'Data written to {csv_file_path}')
