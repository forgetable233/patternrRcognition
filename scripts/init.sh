#!/usr/bin/env bash
#cd ..
echo `pwd`
if [ ! -f "dataset.rar" ]; then
    echo "unable to find dataset.rar"
    exit
fi

unrar x dataset.rar
mv dataset.rar dataset/