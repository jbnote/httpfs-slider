#! /bin/bash

APPNAME=${1:-httpfs}
slider stop $APPNAME
slider destroy $APPNAME
slider create $APPNAME --appdef $PWD --filesystem hdfs://root --queue dev --resources resources.json --template appConfig.json
