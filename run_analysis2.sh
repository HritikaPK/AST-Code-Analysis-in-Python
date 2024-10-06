#!/bin/bash

# Running 2.py on test cases from true_positives_2
echo "Running 2.py on true_positives_2"
for testcase in true_positives_2/*; do
  echo "Running 2.py with test case: $testcase"
  python 2.py "$testcase"
  echo "Finished running 2.py with test case: $testcase"
  echo "-------------------------"
done
