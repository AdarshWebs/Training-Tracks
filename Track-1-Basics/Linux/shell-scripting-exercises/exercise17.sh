
#!/bin/bash

message="random number is:$RANDOM"
echo "$message"

logger -p user.info "message"
