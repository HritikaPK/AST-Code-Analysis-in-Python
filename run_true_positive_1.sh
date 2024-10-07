#!/bin/bash

# Running 1.py on test cases from true_positives_1 and true_negative_1
echo "Analysis: There are no identifiers with length equal 13"
echo 
echo "Running 1.py on true_positives_1"
echo
echo
for testcase in true_positives_1/*; do
  echo "-------------------------"
  echo "Running 1.py with test case: $testcase"
  echo
  python 1.py "$testcase"
  echo "Finished running 1.py with test case: $testcase"
  echo "-------------------------"
  echo
  echo
done
