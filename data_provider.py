# -*- coding:utf-8 -*-

from paddle.trainer.PyDataProvider2 import *


TERM_SIZE=30

def initHook(settings, id,**kwargs):
    input_types = {}
    settings.id = id
    input_types['power'] = dense_vector_sequence(30)
    input_types['temp_max'] = dense_vector_sequence(30)
    input_types['temp_min'] = dense_vector_sequence(30)
    input_types['label'] = dense_vector(30)
    settings.input_types = input_types

@provider(init_hook=initHook, cache=CacheType.CACHE_PASS_IN_MEM)
def process(settings, filename):
    data = []
    fac_id = settings.id
    max_temp = []
    min_temp = []
    with open(filename, 'r') as openFile:
        line = openFile.readlines()[fac_id-1]
        data = map(float, line.rstrip('\n\r').split(',')[1:])
    with open('data/data/temp', 'r') as openFile:
        lines = openFile.readlines()
        min_temp = map(float, lines[0].rstrip('\n\r').split(','))
        max_temp = map(float, lines[1].rstrip('\n\r').split(','))

    for l in range(0,546):
        batch = {}
        batch['label'] = data[l+30:l+60]
        batch['power'] = [data[l:l+30]]
        batch['temp_max'] = [max_temp[l+30:l+60]]
        batch['temp_min'] = [min_temp[l+30:l+60]]
        yield batch




        # with open(filename, 'r') as openFile:
    #     lines = openFile.readlines()[fac_id-1]
    #     for line in lines:
    #         elements = line.rstrip('\n\r').split(',')
    #         data.append(float(elements[1]))
    # max_len = len(data)
    #
    # for i in range(max_len-60):
    #     batch = {}
    #     for j in range(30):
    #         batch['data_%s' % j] = [data[i+j:i+j+30]]
    #     batch['label'] = data[i+60:i+90]
    #     yield batch






###
def initPredictHook(settings,id, **kwargs):
    input_types = {}
    settings.id = id
    input_types['power'] = dense_vector_sequence(30)
    input_types['temp_max'] = dense_vector_sequence(30)
    input_types['temp_min'] = dense_vector_sequence(30)
    settings.input_types = input_types

###
@provider(init_hook=initPredictHook, cache=CacheType.CACHE_PASS_IN_MEM)
def predict_process(settings, filename):
    data = []
    max_temp = []
    min_temp = []
    fac_id = settings.id
    with open(filename, 'r') as openFile:
        line = openFile.readlines()[fac_id-1]
        data = map(float, line.rstrip('\n\r').split(',')[1:])
    with open('data/data/temp', 'r') as openFile:
        lines = openFile.readlines()
        min_temp = map(float, lines[0].rstrip('\n\r').split(','))
        max_temp = map(float, lines[1].rstrip('\n\r').split(','))
        batch = {}
        batch['power'] = [data[576:606]]
        batch['temp_max'] = [max_temp[606:636]]
        batch['temp_min'] = [min_temp[606:636]]
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
