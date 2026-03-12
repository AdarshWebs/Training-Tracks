#!/bin/bash

filepath=$1

if [ -f "$filepath" ]
   then 
      echo "$filepath is regular file"
      exit 0 
elif [ -d "$filepath" ]
   then 
      echo "$filepath this is directory "
      exit 1
else
      echo "$filepath this is another type"
      exit 2
fi
