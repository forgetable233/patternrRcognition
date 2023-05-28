#!/usr/bin/env bash
#cd ..
echo `pwd`
if [ -f "dataset.rar" ]; then
    unrar x dataset.rar
    mv dataset.rar dataset/
fi

python src/jsonrenew.py
python src/jsontrans.py
