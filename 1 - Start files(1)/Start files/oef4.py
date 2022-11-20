import json
applications = {}
with open('logs_laptop_month.csv') as csv_file:
    # read the first line without using it to ignore the headers
    csv_file.readline()
    line = csv_file.readline()
    while line:
        record = line.split(',')
        if len(record) > 2 and record[0] == 'Error':
            # print(record[2])
            if record[2] in applications:
                applications[record[2]] += 1
            else:
                applications[record[2]] = 1
        line = csv_file.readline() # read out the next line
    print(applications)
with open('logs_laptop_month.json', 'w') as json_file:
    json.dump(applications, json_file, indent=2)