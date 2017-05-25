# -*- coding: utf-8 -*-

from paddle.trainer_config_helpers import *

is_predict = get_config_arg('is_predict', bool, False)

process = 'process'
if is_predict:
    process = 'predict_process'

test = 'data/test.list'
train = 'data/train.list'
if is_predict:
    train = None
    test = 'data/pred.list'

define_py_data_sources2(
    train_list=train,
    test_list=test,
    module="data_provider",
    obj=process
)

batch_size = 3

if is_predict:
    batch_size = 1

settings(
    batch_size=batch_size,
    learning_rate=0.0001,
    learning_method=RMSPropOptimizer(),#MomentumOptimizer(1e-4),#RMSPropOptimizer(epsilon=0.0001,rho=0.95),
    regularization=L2Regularization(5e-4),
    gradient_clipping_threshold=25
)

input_data = []

for i in range(30):
    input_data.append(data_layer(name='data_%s' % i, size=30))

label = data_layer(name='label', size=30)

fc_con_layers = []

for i in range(30):
    if i > 1:
        fc_con_layers.append(fc_layer(input=concat_layer(input=[input_data[i], input_data[i-1]]),size=4,act=TanhActivation()))
    else:
        fc_con_layers.append(fc_layer(input=input_data[0], size=4, act=TanhActivation()))


lstm_output = []

for i in range(30):
    lstm_output.append(lstmemory(name='lstm_1_%s' % i,input=fc_con_layers[i], act=ReluActivation()))

lstm_reversed = []

fc_con_layers = []

for i in range(30):
    lstm_reversed.append(simple_lstm(input=lstm_output[i], size=1, act=ReluActivation()))
#
# for i in range(30):
#     lstm_reversed.append(lstmemory(name='lstm_2_%s' % i,input=lstm_output[i], act=ReluActivation()))


output_layers = []

for i in range(30):
    output_layers.append(last_seq(fc_layer(input=lstm_reversed[i], size=1, act=TanhActivation())))


if not is_predict:
    cost = regression_cost(input=concat_layer(input=output_layers),label=label)
    outputs(cost)
else:
    outputs(output_layers)







# import paddle.v2 as paddle
# import numpy as np
# import data_provider
#
# paddle.init(use_gpu=False)
#
#
# def input_data():
#     x = paddle.layer.data(name='power', type=paddle.data_type.dense_vector_sequence(30))
#     y = paddle.layer.data(name='predict', type=paddle.data_type.dense_vector_sequence(30))
#     return x, y
#
# def lstm_array(input_seq):
#     for i in range(15):
#         lstm_output = paddle.networks.simple_lstm(input=input_seq, size=4, reverse=False, act=paddle.activation.ReluActivation())
#         input_seq = paddle.layer.concat(input=[input_seq, lstm_output])
#     output_seq =  paddle.layer.fc_layer(input=input_seq, size=1, act=paddle.activation.ReluActivation())
#     return output_seq
#
# def event_handler(event):
#     if isinstance(event, paddle.event.EndIteration):
#         if event.batch_id % 100 == 0:
#             print "Pass %d, Batch %d, Cost %f" % (event.pass_id, event.batch_id, event.cost)
#
#     if isinstance(event, paddle.event.EndPass):
#         result = trainer.test(
#             reader=paddle.batch(data_provider.getTestBatch(), batch_size=2),
#             feeding=feeding)
#         print "Test %d, Cost %f" % (event.pass_id, result.cost)
#
#
# x,y = input_data()
# lstm_arr = lstm_array(x)
# cost = paddle.layer.mse(input=lstm_arr, label=y)
#
# parameters = paddle.parameters.create(cost)
#
# print parameters.keys()
#
# optimizer = paddle.optimizer.RMSProp()
#
# trainer = paddle.trainer.SGD(cost=cost, parameters=parameters, update_equation=optimizer)
# feeding = {'x':0,'y':1}
# trainer.train(reader=data_provider.reader(), event_handler=event_handler,num_passes=1,feeding=feeding)
#
