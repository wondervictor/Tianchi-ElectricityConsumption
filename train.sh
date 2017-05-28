#!/usr/bin/env bash

fac_id=$1
output=output
cfg=trainer.py
output_dir=${output}/${fac_id}

mkdir ${output_dir}

log=${output}/${fac_id}/train.log

paddle train \
    --config=${cfg} \
    --save_dir=${output_dir} \
    --trainer_count=2 \
    --log_period=10000 \
    --dot_period=10000 \
    --num_passes=200 \
    --use_gpu=false \
    --config_args=id=${fac_id}\
    --show_parameter_stats_period=300 \
    2>&1 | tee ${log}
