#!/bin/bash
# 2018-09-05 (cc) <paul4hough@gmail.com>
#

if [ -e pytest ] ; then
  pytest
else
  echo FAIL: pytest not found
  exit 1
fi
