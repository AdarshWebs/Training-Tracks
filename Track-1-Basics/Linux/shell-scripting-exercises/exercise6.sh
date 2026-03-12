#!/bin/bash

echo "enter the file path"
read filepath

if [ -f "$filepath" ]
 then 
   echo "$filepath is a regular file"
elif [ -d "$filepath" ]
 then
   echo "$filepath is a directory"
 else
   echo "$filepath is another type of file"
fi

ls -l $filepath
