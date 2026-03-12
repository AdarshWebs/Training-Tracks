#!/bin/bash

cd ~/linux_pratice/adarsh

DAY=$(date +%F)s
echo "enter the file extension:"
read extension

echo "enter the prefix :(press enter for the $DAY)"
read

for name in *.$extension
do 
  echo "renaming $name to ${DAY}-${name}"
  mv "$name" "${DAY}-${name}"
done

