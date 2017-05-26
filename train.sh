#!/usr/bin/env bash

set -e
fac_id=$1
output=$2
cfg=trainer.py
output_dir=${output}/${fac_id}
mdkir output_dir
log=${output}/${fac_id}/train.log
paddle train \
    --config=${cfg} \
    --save_dir=${output_dir} \
    --trainer_count=2 \
    --log_period=1000 \
    --dot_period=100 \
    --num_passes=200 \
    --use_gpu=false \
    --config_args=id=${fac_id}\
    --show_parameter_stats_period=3000 \
    2>&1 | tee ${log}