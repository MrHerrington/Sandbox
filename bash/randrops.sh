<< '////'

Introduction
Raindrops is a slightly more complex version of the FizzBuzz challenge, a classic interview question.

Instructions
Your task is to convert a number into its corresponding raindrop sounds.

If a given number:
is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.

Examples
28 is divisible by 7, but not 3 or 5, so the result would be "Plong".
30 is divisible by 3 and 5, but not 7, so the result would be "PlingPlang".
34 is not divisible by 3, 5, or 7, so the result would be "34".

Note
A common way to test if one number is evenly divisible by another is to compare the remainder or modulus to zero.
Most languages provide operators or functions for one (or both) of these.

////


#!/usr/bin/env bash

main () {
    RES=""

    if [[ $(("$@" % 3)) -eq 0 ]]; then
        RES+="Pling"
    fi

    if [[ $(("$@" % 5)) -eq 0 ]]; then
        RES+="Plang"
    fi

    if [[ $(("$@" % 7)) -eq 0 ]]; then
        RES+="Plong"
    fi

    if [[ -z $RES ]]; then
        RES="$*"
    fi

    echo "$RES"
}

main "$@"
