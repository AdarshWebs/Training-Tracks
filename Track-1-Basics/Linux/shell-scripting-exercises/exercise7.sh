#!/bin/bash

filepath=$1

if [ -f "$filepath" ]
  then
    echo "$filepath is a regular file"
elif [ -d "$filepath" ]
  then 
    echo "$filepath is a dictory"
else  
    echo "$filepath is another type of file"
fi 
ls -l $filepath
