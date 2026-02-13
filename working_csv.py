import csv

data = open("customer.csv")

csv_data = csv.reader(data)

print(type(csv_data))

data_lines = list(csv_data)

# print(data_lines[2])
print(data_lines[0])

full_names = []
for data in data_lines[1:]:
    full_names.append(data[2] + " " + data[3])
    
print(full_names)

file_to_output = open('to_save_file.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerows(full_names)
file_to_output.close()