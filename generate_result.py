# -*- coding:utf-8 -*-

# def generate(filname):
#     with open(filname, 'r') as f:


def generate_result():

    max_values = [0]*1454
    with open('data/data/max_value', 'r')  as openFile:
        lines = openFile.readlines()
        for line in lines:
            elements = line.rstrip('\n\r').split(',')
            max_values[int(elements[0])-1] = float(elements[1])
    result = []

    for i in range(1454):
        print "Calculating Factory %s" % i
        seq = [0]*31
        seq[0] = i
        with open('result/%s/rank-00000' % (i+1), 'r') as resFile:
            line = resFile.readlines()[0]
            elements = line.rstrip('\n\r').split(';')[0:30]
            seq[1:31] = [max_values[i] * float(x) for x in elements]
        result.append(seq)

    with open('result.csv', 'w+') as writingFile:
        for element in result:
            line = ','.join(['%s' % x for x in element])
            line += '\n'
            writingFile.write(line)


    # sum

    sum_res = [0]*30
    for i in range(30):
        s = 0
        for j in range(1454):
            s += result[j][i+1]
        sum_res[i] = s

    with open('final.csv', 'w+') as writingFile:
        line = 'predict_date,predict_power_consumptio\n'
        writingFile.write(line)
        start_date = 20160901
        for i in range(30):
            start_date += i
            writingFile.write('%s,%s\n' % (start_date, sum_res[i]))


generate_result()