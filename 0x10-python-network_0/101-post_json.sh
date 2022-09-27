#!/bin/bash
# send json file post
curl -X POST $1 -d @$2
