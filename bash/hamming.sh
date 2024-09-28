<< '////'

Instructions
Calculate the Hamming distance between two DNA strands.

Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they
achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion cell
divisions in a lifetime!

When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of
DNA get encoded with the incorrect information. If we compare two strands of DNA and count the differences between
them we can see how many mistakes occurred. This is known as the "Hamming distance".

We read DNA using the letters C, A, G and T. Two strands might look like this:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
They have 7 differences, and therefore the Hamming distance is 7.

The Hamming distance is useful for lots of things in science, not just biology,
so it's a nice phrase to be familiar with :)

Implementation notes
The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between
sequences of different lengths should not work.

////


#!/usr/bin/env bash

main () {
    # count args check
    if [[ "$#" -ne 2 ]]; then
        echo "Usage: hamming.sh <string1> <string2>"
        exit 1
    fi

    # both empty args check
    if [[ ${#1} -eq 0 ]] && [[ ${#2} -eq 0 ]]; then
        echo "0"
        exit 0
    fi

    # different args length check
    if [[ ${#1} -ne ${#2} ]] || [[ ${#1} -eq 0 ]] || [[ ${#2} -eq 0 ]]; then
        echo "strands must be of equal length"
        exit 1
    fi

    RES=0
    MAX_LEN=${#1}

    for ((i = 0 ; i < MAX_LEN ; i++)); do
        if [[ ${1:$i:1} != "${2:$i:1}" ]]; then
            (( RES+=1 ))
        fi
    done
    echo $RES
}

main "$@"
