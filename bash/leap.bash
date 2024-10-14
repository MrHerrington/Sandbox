<< '////'

Introduction

A leap year (in the Gregorian calendar) occurs:
In every year that is evenly divisible by 4.
Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
Some examples:
1997 was not a leap year as it's not divisible by 4.
1900 was not a leap year as it's not divisible by 400.
2000 was a leap year!

Note

For a delightful, four-minute explanation of the whole phenomenon of leap years, check out this YouTube video.

Instructions

Your task is to determine whether a given year is a leap year.

////


#!/usr/bin/env bash

main () {
  year="$*"

  if [[ $year =~ [^[:digit:]] ]] || [[ ${#@} -ne 1 ]]; then
    echo "Usage: leap.sh <year>"
    exit 1
  fi

  if [[ $((year % 400)) -eq 0 ]]; then
    echo "true"
  else
    
    if [[ $((year % 4)) -eq 0 ]] && [[ $((year % 100)) -ne 0 ]]; then
      echo "true"
    else
      echo "false"
    fi

  fi
}

main "$@"
