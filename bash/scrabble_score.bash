<< '////'

Introduction

Scrabble is a word game where players place letter tiles on a board to form words. Each letter has a value.
A word's score is the sum of its letters' values.

Instructions

Your task is to compute a word's Scrabble score by summing the values of its letters.

The letters are valued as follows:
Letter	                        Value
A, E, I, O, U, L, N, R, S, T    1
D, G	                          2
B, C, M, P	                    3
F, H, V, W, Y	                  4
K	                              5
J, X	                          8
Q, Z	                          10

For example, the word "cabbage" is worth 14 points:
3 points for C
1 point for A
3 points for B
3 points for B
1 point for A
2 points for G
1 point for E

////


#!/usr/bin/env bash

main () {
  declare -A dict

  dict["a"]=1
  dict["b"]=3
  dict["c"]=3
  dict["d"]=2
  dict["e"]=1
  dict["f"]=4
  dict["g"]=2
  dict["h"]=4
  dict["i"]=1
  dict["j"]=8
  dict["k"]=5
  dict["l"]=1
  dict["m"]=3
  dict["n"]=1
  dict["o"]=1
  dict["p"]=3
  dict["q"]=10
  dict["r"]=1
  dict["s"]=1
  dict["t"]=1
  dict["u"]=1
  dict["v"]=4
  dict["w"]=4
  dict["x"]=8
  dict["y"]=4
  dict["z"]=10

  word="$*"
  word_array=()
  score=0

  for (( i=0; i<"${#word}"; i++ )); do
		let="${word:$i:1}"
		lwcs_let="${let,}"
		if [[ "$lwcs_let" =~ [a-z] ]]; then
			word_array+=("$lwcs_let")
		fi
	done

	for i in "${word_array[@]}"; do
    (( score+=${dict[$i]} ))
  done

	echo "$score"
}

main "$@"
