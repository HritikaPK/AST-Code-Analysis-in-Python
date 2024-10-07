#!/bin/bash

echo "Running 1.py on true_negative_1"
echo
echo
for testcase in true_negative_1/*; do
  echo "-------------------------"
  echo "Running 1.py with test case: $testcase"
  echo
  python 1.py "$testcase"
  echo "Finished running 1.py with test case: $testcase"
  echo "-------------------------"
  echo
  echo
done

