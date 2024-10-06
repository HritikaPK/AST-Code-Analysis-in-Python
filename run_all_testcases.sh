#!/bin/bash

# Running 1.py on test cases from testcase_positives_1 and testcase_negative_1
echo "Running 1.py on true_positives_1 and true_negative_1"
for testcase in true_positives_1/* true_negative_1/*; do
  echo "Running 1.py with test case: $testcase"
  python 1.py "$testcase"
  echo "Finished running 1.py with test case: $testcase"
  echo "-------------------------"
done

# Running 2.py on test cases from testcase_positives_2
echo "Running 2.py on true_positives_2"
for testcase in true_positives_2/*; do
  echo "Running 2.py with test case: $testcase"
  python 2.py "$testcase"
  echo "Finished running 2.py with test case: $testcase"
  echo "-------------------------"
done
