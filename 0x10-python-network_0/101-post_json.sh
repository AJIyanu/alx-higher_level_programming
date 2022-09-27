#!/bin/bash
# send json file post
curl -X POST $1 -H "content-type:application/json" -d @$2
