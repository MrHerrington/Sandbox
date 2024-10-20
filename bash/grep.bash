<< '////'

Instructions

Search files for lines matching a search string and return all matching lines.
The Unix grep command searches files for lines that match a regular expression. Your task
is to implement a simplified grep command, which supports searching for fixed strings.
The grep command takes three arguments:
The string to search for.
Zero or more flags for customizing the command's behavior.
One or more files to search in.
It then reads the contents of the specified files (in the order specified), finds the lines that
contain the search string, and finally returns those lines in the order in which they were found.
When searching in multiple files, each matching line is prepended by the file name and a colon (':').

Flags

The grep command supports the following flags:
-n Prepend the line number and a colon (':') to each line in the output, placing the number after the filename (if present).
-l Output only the names of the files that contain at least one matching line.
-i Match using a case-insensitive comparison.
-v Invert the program -- collect all lines that fail to match.
-x Search only for lines where the search string matches the entire line.

To grep or not to grep, that is the question

Although this exercise can be trivially solved by simply passing the arguments to grep, implement this exercise
using bash only. The aim of this exercism track is to learn how to use bash builtin commands to solve problems.
To solve this exercise, you'll need to:
parse command line arguments: getopts is useful for this.
iterate over the lines of a file: this is bash FAQ #1
use regular expression matching: bash can do this using the =~ operator within [[ ... ]]

////


#!/usr/bin/env bash

#######################
# prepare data section#
#######################

setup() {
  cat > iliad.txt << END_ILIAD
Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.
END_ILIAD

  cat > midsummer-night.txt << END_MIDSUMMER
I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.
END_MIDSUMMER

  cat > paradise-lost.txt << END_PARADISE
Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed
END_PARADISE
}

#######################
# delete data section #
#######################

teardown() {
  rm iliad.txt midsummer-night.txt paradise-lost.txt
}

##############################
# main functionality section #
##############################

numerate () {
  counter=0

  for line in "${text_strings[@]}"; do
    temp_counter=$counter
    (( counter++ ))
    text_strings[$temp_counter]="$counter:$line"
  done
}

show_arr () {
  temp_arr=()

  for line in "${text_strings[@]}"; do
    if [[ "$options_list" =~ "-n" ]]; then
      if [[ "$line" =~ $with_nums_pattern ]]; then
        temp_arr+=( "$line" )
      fi
    else
      if [[ "$line" =~ $pattern ]]; then
        temp_arr+=( "$line" )
      fi
    fi
  done

  for line in "${temp_arr[@]}"; do
    echo "$line"
  done
}

main () {
  options_list="$*"
  pattern_pos=$(( "$#" - 1 ))
  pattern=${!pattern_pos}
  file_name_pos=$(( "$#" ))
  file_name=${!file_name_pos}
  
  declare -a text_strings
  
  while read line; do
      text_strings+=( "$line" )
  done < "$file_name"

  if [[ "$#" < 3 ]]; then
    for line in "${text_strings[@]}"; do
      if [[ "$line" =~ "$pattern" ]]; then
        echo "$line"
      fi
    done

    exit 0
  fi

  OPTIONS=":nlivx"

  while getopts ${OPTIONS} option; do
    case ${option} in
      n)
        numerate
        with_nums_pattern="[[:digit:]]*?:.*$pattern"
        ;;
      l)
        local temp_arr

        for line in "${text_strings[@]}"; do
          if [[ "$line" =~ "$2" ]] && [[ ! "${temp_arr[*]}" =~ "$3" ]]; then
            temp_arr+=( "$3" )
          fi
        done

        text_strings=("${temp_arr[@]}")
        ;;
      i)
        pattern="${pattern^^}"
        ;;
      x)
        pattern="^$pattern$"
        with_nums_pattern="^$with_nums_pattern$"
        ;;
      :)
        echo "Option -${OPTARG} requires an argument."
        exit 1
        ;;
      ?)
        echo "Invalid option: -${OPTARG}."
        exit 1
        ;;
    esac
  done

  show_arr
}

setup
main "$@"
teardown
