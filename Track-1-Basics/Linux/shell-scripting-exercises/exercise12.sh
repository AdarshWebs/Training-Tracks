#!/bin/bash

function file_count()
   {
     local number_of_files=$(ls -l | wc -l )
     echo "$number_of_files"
   }
file_count
