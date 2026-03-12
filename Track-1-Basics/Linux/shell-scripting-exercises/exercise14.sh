#!/bin/bash

DAY=$(date +%F)

for FILE in adarsh/*.jpg
do
    [ -e "$FILE" ] || continue
    mv "$FILE" "adarsh/${DAY}-$(basename "$FILE")"
done
