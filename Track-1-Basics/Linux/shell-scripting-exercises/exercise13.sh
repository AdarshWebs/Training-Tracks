#!/bin/bash

function file_count()
   {
     dir=$1
     echo "$dir"
     local number_of_files=$(ls "$dir" | wc -l)
     echo "$number_of_files"
   }
file_count "/etc"
file_count "/var"
file_count "/usr/bin"
file_count "adarsh"
