<< '////'

Instructions

Calculate the points scored in a single toss of a Darts game.
Darts is a game where players throw darts at a target.
In our particular instance of the game, the target rewards 4 different
amounts of points, depending on where the dart lands:
Our dart scoreboard with values from a complete miss to a bullseye
If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.
The outer circle has a radius of 10 units (this is equivalent to the total radius for the entire target),
the middle circle a radius of 5 units, and the inner circle a radius of 1. Of course, they are all centered
at the same point — that is, the circles are concentric defined by the coordinates (0, 0).
Given a point in the target (defined by its Cartesian coordinates x and y, where x and y are real),
calculate the correct score earned by a dart landing at that point.

Credit

The scoreboard image was created by habere-et-dispertire using Inkscape.

Floating Point Arithmetic

This particular exercise, since it deals with floating point arithmetic, is natural to rely on external tools (see below).
As an extra challenging challenge, find a way to implement this with plain bash.

////


#!/usr/bin/env bash

main () {
  coordinates=( "$1" "$2" )

  if { [[ -z ${coordinates[0]} ]] || [[ ${coordinates[0]} =~ [^-0-9.] ]]; } \
  || { [[ -z ${coordinates[1]} ]] || [[ ${coordinates[1]} =~ [^-0-9.] ]]; }; then
    echo 'Invalid args!'
    exit 1
  
  else
    radius=$( echo "scale=2; sqrt ($1 ^ 2 + $2 ^ 2 )" | bc )
    if [[ $( echo "$radius <= 1" | bc ) -ne 0 ]]; then
      echo 10
    elif [[ $( echo "$radius <= 5" | bc ) -ne 0 ]]; then
      echo 5
    elif [[ $( echo "$radius <= 10" | bc ) -ne 0 ]]; then
      echo 1
    else
      echo 0
    fi
    
  fi 
}

main "$@"
