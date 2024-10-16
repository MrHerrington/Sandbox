<< '////'

Introduction

You are starting a secret coding club with some friends and friends-of-friends. Not everyone knows each other, so you and your
friends have decided to create a secret handshake that you can use to recognize that someone is a member. You don't want anyone
who isn't in the know to be able to crack the code.
You've designed the code so that one person says a number between 1 and 31, and the other person turns it into a series of actions.

Instructions

Your task is to convert a number between 1 and 31 to a sequence of actions in the secret handshake.
The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary.
Start at the right-most digit and move left.

The actions for each number place are:
00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump
10000 = Reverse the order of the operations in the secret handshake.

Let's use the number 9 as an example:
9 in binary is 1001.
The digit that is farthest to the right is 1, so the first action is wink.
Going left, the next digit is 0, so there is no double-blink.
Going left again, the next digit is 0, so you leave your eyes open.
Going left again, the next digit is 1, so you jump.
That was the last digit, so the final code is:
wink, jump
Given the number 26, which is 11010 in binary, we get the following actions:
double blink
jump
reverse actions
The secret handshake for 26 is therefore:
jump, double blink

Note

If you aren't sure what binary is or how it works, check out this binary tutorial.

////


#!/usr/bin/env bash

main () {
  num="$*"
  res_str=""
  
  D2B=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})
  full_binary=${D2B[$num]}
  binary=${full_binary:(-5)}

  if [ "${binary:(-1):1}" -eq 1 ]; then
    act1+="wink"
  fi

  if [ "${binary:(-2):1}" -eq 1 ]; then
    act2+="double blink"
  fi

  if [ "${binary:(-3):1}" -eq 1 ]; then
    act3+="close your eyes"
  fi

  if [ "${binary:(-4):1}" -eq 1 ]; then
    act4+="jump"
  fi

  arr=( "$act1" "$act2" "$act3" "$act4" )
  rev_arr=( "$act4" "$act3" "$act2" "$act1" )

  if [ "${binary:(-5):1}" -eq 1 ]; then
    target_arr=( "${rev_arr[@]}" )
  else
    target_arr=( "${arr[@]}" )
  fi
  
  for i in "${target_arr[@]}"; do
    if [[ -z $res_str ]] && [[ -n "$i" ]]; then
      res_str+="$i"
    elif [[ -n $res_str ]] && [[ -n "$i" ]]; then
      res_str+=",$i"
    fi
  done

  echo "$res_str"
}

main "$@"
