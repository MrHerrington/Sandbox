<< '////'

Instructions

Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant
could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat.
One grain on the first square of a chess board, with the number of grains doubling on each successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

Write code that shows:
  - how many grains were on a given square, and;
  - the total number of grains on the chessboard.

////


#!/usr/bin/env bash

main () {
  var="$@"

  if [[ "$var" == "total" ]]; then
    echo 18446744073709551615

  elif [[ "$var" -lt 1 || "$var" -gt 64 ]]; then
    echo "Error: invalid input"
    exit 1

  else
    (( degree=2**("$var"-1) ))
    echo ${degree#-}

  fi
}

main "$@"
