#!/usr/bin/env bash

start=$1
end=$2

#832 1150 1455

for i in $( seq $start $end )
do
    echo $i
    sh train.sh $i

    sh predict.sh $i
done
