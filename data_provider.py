# -*- coding:utf-8 -*-

from paddle.trainer.PyDataProvider2 import *


TERM_SIZE=30

def initHook(settings, **kwargs):
    input_types = {}
    for i in range(30):
        input_types['data_%s' % i] = dense_vector_sequence(30)
    input_types['label'] = dense_vector(30)

    settings.input_types = input_types

@provider(init_hook=initHook, cache=CacheType.CACHE_PASS_IN_MEM)
def process(settings, filename):
    data = []
    with open(filename, 'r') as openFile:
        lines = openFile.readlines()
        for line in lines:
            elements = line.rstrip('\n\r').split(',')
            data.append(float(elements[1]))
    max_len = len(data)

    for i in range(max_len-90):
        batch = {}
        for j in range(30):
            batch['data_%s' % j] = [data[i+j:i+j+30]]
        batch['label'] = data[i+60:i+90]
        yield batch






###
def initPredictHook(settings, **kwargs):
    input_types = {}
    for i in range(30):
        input_types['data_%s' % i] = dense_vector_sequence(30)
    settings.input_types = input_types

###
@provider(init_hook=initPredictHook, cache=CacheType.CACHE_PASS_IN_MEM)
def predict_process(settings, filename):
    data = []
    with open(filename, 'r') as openFile:
        lines = openFile.readlines()
        for line in lines:
            elements = line.rstrip('\n\r').split(',')
            data.append(float(elements[1]))
    batch = {}
    for j in range(30):
        batch['data_%s' % j] = [data[j:j + 30]]
    yield batch
#
# def get_batch(test=False):
#     data = []
#
#     step = 1
#     if test:
#         step = 10
#
#     with open('data/data/1', 'r') as openFile:
#         lines = openFile.readlines()
#         for line in lines:
#             data.append(line.rstrip('\r\n').split(',')[1])
#     for i in range(0,len(data)-60,step):
#         yield {'x':[data[i:i+30]],'y':[data[i+30:i+60]]}
#
#
# def reader():
#     return get_batch(False)
#
# def getTestBatch():
#     return get_batch(True)
