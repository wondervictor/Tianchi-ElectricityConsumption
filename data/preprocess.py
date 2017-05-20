# -*- coding: utf-8 -*-

def split_data(filename):
    data = {}
    with open(filename, 'r') as openFile:
        f =  openFile.readlines()[1:]
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

split_data('Tianchi_power.csv')

