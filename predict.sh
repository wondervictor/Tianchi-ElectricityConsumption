#!/usr/bin/env bash

fac_id=$1
output=output
cfg=trainer.py
output_dir=${output}
log=${output}/train.log
model=${output}/${fac_id}/pass-00199

mkdir result/${fac_id}

paddle train \
    --config=${cfg} \
    --save_dir=${output_dir} \
    --job=test \
    --config_args=is_predict=1,id=${fac_id} \
    --init_model_path=${model} \
    --use_gpu=false \
    --predict_output_dir=result/${fac_id}

path=${output}/${fac_id}

mv  ${model} ${path}/model

rm -rf ${path}/pass-*