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

main () {
  string="$*"
  pattern="\[[^\(\)\{\}]*\]"
  
  match=$(echo "$string" | grep -o "$pattern")

  while [[ -n "$match" ]]; do
    without_brackets=${match:1:-1}
    string=${string//"$match"/"$without_brackets"}
    match=$(echo "$string" | grep -o "$pattern")
  done

  echo "$string"

  if [[ $string =~ .*[\]]+.* ]] || [[ $string =~ .*[\[]+.* ]]; then
    echo "false"
  else
    echo "true"
  fi
}

main "$@"
