#!/bin/bash

image=${1}
output=${2:-None}
sigma1=${3:-1}
sigma2=${4:-30}
threshold=${5:-0.87}


python /input/binarize.py --img $image --sigma1 $sigma1 --sigma2 $sigma2 --threshold $threshold --output_path $output
# python binarize.py --img $image --sigma1 $sigma1 --sigma2 $sigma2 --threshold $threshold --output_path $output