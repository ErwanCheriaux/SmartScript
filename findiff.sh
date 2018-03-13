#!/bin/bash

#create tmp directory
mkdir -p /tmp/finddiff

#first find
cd "$1"
find ./ | sort -d > /tmp/finddiff/finddiff1.txt
cd - > /dev/null

#second find
cd "$2"
find ./ | sort -d > /tmp/finddiff/finddiff2.txt
cd - > /dev/null

#diff
diff -u /tmp/finddiff/finddiff*

#remove tmp directory
rm -fr /tmp/finddiff
