# -*- coding: utf-8 -*-

def split_data(filename):
    data = {}
    with open(filename, 'r') as openFile:
        f = openFile.readlines()[1:]
        for line in f:
            line_elements = line.rstrip('\r\n').split(',')
            key = line_elements[1]
            if key in data:
                data[key].append([line_elements[0],line_elements[2]])
            else:
                data[key] = [[line_elements[0], line_elements[2]]]
    for key in data:
        with open('data/%s' % key, 'w+') as writeFile:
            for elem in data[key]:
                line = ','.join(elem)
                line += '\n'
                writeFile.write(line)



def reshape_data():
    data = {}
    # raw data
    with open('Tianchi_power.csv','r') as openFile:
        f = openFile.readlines()[1:]
        for line in f:
            line_elements = line.rstrip('\n\r').split(',')
            current_spot = int(line_elements[1])
            key = '%s' % current_spot
            value = float(line_elements[2])
            if key in data:
                data[key].append(value)
            else:
                data[key] = [value]

    max_values = []
    with open('data/data','w+') as openFile:
        for i in range(1,1455):
            key = '%s' % i
            values = data[key]
            max_value = max(values)
            max_values.append((key, max_value))
            line = '%s,' % key
            length = len(values)
            line += ','.join(['%s' % (x/max_value) for x in values[length-606:length]])
            line += '\n'
            openFile.write(line)

    with open('data/max_value', 'w+') as openFile:
        for i in max_values:
            openFile.write('%s,%s\n' % (i[0],i[1]))

reshape_data()
