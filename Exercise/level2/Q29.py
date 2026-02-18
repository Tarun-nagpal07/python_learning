'''Read a CSV file of student names and test marks. Calculate each student's average and
write a new CSV with an extra 'Average' column appended.'''


import csv

data = open('student.csv')

csv_data = csv.reader(data)

data_lines= list(csv_data)


new_data = []

for row in data_lines[1:]:
    scores = list(map(int, row[1:4])) 
    avg = sum(scores) / len(scores)
    new_row = row + [f"{avg:.2f}"]  
    new_data.append(new_row)

file_to_output = open('student_report.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerows(new_data)
file_to_output.close()

