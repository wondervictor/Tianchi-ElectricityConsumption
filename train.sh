#!/usr/bin/env bash

set -e

cfg=trainer.py
output_dir=output
log=output/train.log
paddle train \
    --config=${cfg} \
    --save_dir=${output_dir} \
    --trainer_count=2 \
    --log_period=1000 \
    --dot_period=100 \
    --num_passes=50 \
    --use_gpu=false \
    --show_parameter_stats_period=3000 \
    2>&1 | tee ${log}