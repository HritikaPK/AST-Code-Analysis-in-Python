#!/bin/bash

# Running 2.py on test cases from true_positives_2
echo "Analysis: Maximum control structure nesting of 4"
echo 
echo "Running 2.py on true_positives_2 cases"
echo
echo
for testcase in true_positives_2/*; do
  echo "-------------------------"
  echo "Running 2.py with test case: $testcase"
  echo 
  python 2.py "$testcase"
  echo "Finished running 2.py with test case: $testcase"
  echo "-------------------------"
  echo
  echo
done
# echo
# # Running 2.py on test cases from true_negative_2
# echo "Running 2.py on true_negative_2 cases"
# echo
# echo
# for testcase in true_negative_2/*; do
#   echo "-------------------------"
#   echo "Running 2.py with test case: $testcase"
#   echo 
#   python 2.py "$testcase"
#   echo "Finished running 2.py with test case: $testcase"
#   echo "-------------------------"
#   echo
#   echo
# done