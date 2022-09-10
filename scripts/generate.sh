#!/bin/bash

for (( i=1; i<1698; i++ ))

do

 echo $i
 python3 correct.py $i

done
