#!/bin/bash

file_path="test.txt"

if [ -e "$file_path" ]; then
    echo "$file_path passwords are enabled."

    if [ -w "$file_path" ]; then
        echo "You have permission to edit $file_path."
    else
        echo "You do NOT have permission to edit $file_path."
    fi

else
    echo "$file_path does not exist."
fi

