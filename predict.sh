#!/usr/bin/env bash

set -e

cfg=trainer.py
output_dir=output
log=output/train.log
model=output/pass-00049

paddle train \
    --config=${cfg} \
    --save_dir=${output_dir} \
    --job=test \
    --config_args=is_predict=1 \
    --init_model_path=${model} \
    --use_gpu=false \
    --predict_output_dir=result