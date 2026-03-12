#!/bin/bash

input=$1

case $input in

start)
    sleep 300 &
    echo "monfo server started"
    ;;
stop)
    PID_ID=$(pgrep sleep)
    if [ -z "$PID_ID" ]
      then
          echo "mongodb is not running"
    else
       kill "$PID_ID"
       if [ $? -eq 0 ]
       then 
          echo "mongodb server is stopped"
       else
          echo "failed to stop mongodbb"
       fi
    fi
    ;;
*)
    echo "usage:$0 {start|stop}"
esac
