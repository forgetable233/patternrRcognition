#!/usr/bin/env bash
#cd ..
echo `pwd`
if [ ! -f "dataset.rar" ]; then
    echo "unable to find dataset.rar"
    exit
fi

if [ ! -d "data" ]; then
    mkdir "data"
fi

mv dataset.rar data
cd data || exit
mkdir json
mkdir bmp
unrar e dataset.rar

# shellcheck disable=SC2035
mv *.json json
# shellcheck disable=SC2035
mv *.bmp bmp
