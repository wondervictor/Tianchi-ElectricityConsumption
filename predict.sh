#!/usr/bin/env bash

set -e
fac_id=$1
output=$2
cfg=trainer.py
output_dir=${output}
log=${output}/train.log
model=${output}/${fac_id}/pass-00199

paddle train \
    --config=${cfg} \
    --save_dir=${output_dir} \
    --job=test \
    --config_args=is_predict=1,id=${fac_id} \
    --init_model_path=${model} \
    --use_gpu=false \
    --predict_output_dir=result

mv pass-00199 model
rm -rf pass-*