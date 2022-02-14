#!/bin/bash  

#˙echo "enter arguments with python command for example: Python3 "example.py" "latitude" "Longitude" "period" "

python3 -m pip install -r Requirments.txt

echo "enter latitude value"
read latitude
echo "enter longitude value"
read longitude 
echo "enter period value"
read period


python3 src/main.py "$latitude" "$longitude" "$period"

 

