<< '////'

Introduction
You're given the opportunity to write software for the Bracketeer™, an ancient but powerful mainframe.
The software that runs on it is written in a proprietary language. Much of its syntax is familiar, but you
notice lots of brackets, braces and parentheses. Despite the Bracketeer™ being powerful, it lacks flexibility.
If the source code has any unbalanced brackets, braces or parentheses, the Bracketeer™ crashes and must be rebooted.
To avoid such a scenario, you start writing code that can verify that brackets, braces, and parentheses are balanced
before attempting to run it on the Bracketeer™.

Instructions
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify
that any and all pairs are matched and nested correctly. Any other characters should be ignored.
For example, "{what is (42)}?" is balanced and "[text}" is not.

////


#!/usr/bin/env bash

greedy_check () {
  string="$*"
  pattern="[\[]+.*?[\]]+|[\{]+.*?[\}]+|[\(]+.*?[\)]+"

  match=$(echo "$string" | grep -Po "$pattern" | head -1)

  while [[ -n "$match" ]]; do
    without_brackets=${match:1:-1}
    string=${string//"$match"/"$without_brackets"}
    match=$(echo "$string" | grep -Po "$pattern" | head -1)
  done

  if [[ $string =~ .*[\]]+.* ]] || [[ $string =~ .*[\[]+.* ]] \
  || [[ $string =~ .*[\}]+.* ]] || [[ $string =~ .*[\{]+.* ]] \
  || [[ $string =~ .*[\)]+.* ]] || [[ $string =~ .*[\(]+.* ]]; then
    echo 0
  else
    echo 1
  fi
}

non_greedy_check () {
  string="$*"
  pattern="[\[]+.*[\]]+|[\{]+.*[\}]+|[\(]+.*[\)]+"

  match=$(echo "$string" | grep -Po "$pattern" | head -1)

  while [[ -n "$match" ]]; do
    string=${string//"$match"/}
    match=$(echo "$string" | grep -Po "$pattern" | head -1)
  done

  if [[ $string =~ .*[\]]+.* ]] || [[ $string =~ .*[\[]+.* ]] \
  || [[ $string =~ .*[\}]+.* ]] || [[ $string =~ .*[\{]+.* ]] \
  || [[ $string =~ .*[\)]+.* ]] || [[ $string =~ .*[\(]+.* ]]; then
    echo 0
  else
    echo 1
  fi
}

main () {
  check1=$(greedy_check "$@")
  check2=$(non_greedy_check "$@")

  if [[ $(( check1*check2 )) -eq 1 ]]; then
    echo 'true'
  else
    echo 'false'
  fi
}

main "$@"
