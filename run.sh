#!/usr/bin/env bash

output_dir=1

for i in $( seq 1 1455 )
do
    echo $i
    sh train.sh $i $output_dir


    sh predict.sh $i $output_dir
done