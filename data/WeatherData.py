# -*- coding: utf-8 -*-


#weather_type = ['晴','多云','阴','阵雨','雷阵雨','小雨','中雨','大雨','暴雨','雨夹雪','小雪','大雪']

# min_temp_data = ['0']*636
# max_temp_data = ['0']*636
#
#
# with open('weather.txt', 'r') as openFile:
#     f = openFile.readlines()
#     k = 0
#     for i in range(6, len(f),2):
#         line = f[i]
#         line_elements = line.rstrip('\r\n').split(',')[0:3]
#         min_temp_data[k] = line_elements[2]
#         max_temp_data[k] = line_elements[1]
#
#
#         k += 1
#
# with open('data/weather','w+') as openFile:
#     line1 = ','.join(['%s' % x for x in min_temp_data])
#     line1 += '\n'
#     openFile.write(line1)
#     line2 = ','.join(['%s' % x for x in max_temp_data])
#     line2 += '\n'
#     openFile.write(line2)
#     print len(min_temp_data)

#

import numpy as np

import codecs
def normalization_temp():
    # openFile = codecs.open('data/weater', 'r', "unicode")
    # s = openFile.readlines()
    # min_temp = s[0].rstrip('\n').replace('\x00','').split(',')
    # print int(min_temp[1])
    with open('data/weater', 'r') as openFile:
        s = openFile.readlines()
        min_temp = map(float, s[0].rstrip('\n').replace('\x00','').split(','))

        max_temp = map(float, s[1].rstrip('\r\n').replace('\x00','').split(','))

        # print max_temp[1]
        # print float(max_temp[1])
        max_temp_value = max(max_temp)
        min_temp_value = max([abs(x) for x in min_temp])
    #
        min_temp = [float(x)/min_temp_value for x in min_temp]
        max_temp = [float(x)/max_temp_value for x in max_temp]

    with open('data/temp', 'w+') as openFile:
        line_1 = ','.join(['%s' % x for x in min_temp])
        line_1 += '\n'
        line_2 = ','.join(['%s' % x for x in max_temp])
        line_2 += '\n'
        openFile.write(line_1)
        openFile.write(line_2)


normalization_temp()
