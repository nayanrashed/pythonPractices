import csv
'''file = open('example.csv')
file_reader =  csv.reader(file)
'''
# data = list(file_reader)
# print(data)
# print(data[0][2])

# reading a csv file row wise
'''for row in file_reader:
    print('Row No= '+str(file_reader.line_num)+' '+str(row))'''
    
# writing a csv file
output_file = open('out.csv', 'w', newline='')
output_writer=csv.writer(output_file)
# output_writer=csv.writer(output_file, delimiter='.')
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['a','b','c','d'])
output_file.close()



 