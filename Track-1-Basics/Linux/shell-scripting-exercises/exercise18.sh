#!/bin/bash

function logging()
{
   message=$@
   set_message="random number :$message"
   echo "$set_message"
   logger -i -p user.info "$set_message"
}

logging $RANDOM
logging $RANDOM
