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

ere_quote() {
  # Usage: ere_quote "string"
  sed 's/[][\.|$(){}?+*^]/\\&/g' <<< "$*"
}

create_source () {
  for file in "${files[@]}"; do
    while read line; do
      string_num=$(awk -v text="$line" 'index($0, text) { print NR; exit }' "$file")
      full_string="$file$sep$string_num$sep$line"
      full_source+=( "$full_string" )
    done < "$file"
  done

}

split_on_sep () {
  # Usage: split_on_sep "array_name" "sep" "string"
  local -n __temp_arr=$1

  while read -r __line; do
    if [[ -n "$__line" ]]; then
      __temp_arr+=( "$__line" )
    fi
  done < <(awk -v sep="$2" 'BEGIN{ RS=sep }{ print $0 }' <<< "$3")
}

main () {
  declare -a flags files full_source source
  local subpattern
  local good_list

  args=( "$@" )
  sep="->sep<-"
  in_str_sep=":"

  for arg in "${args[@]}"; do
    if [[ "$arg" =~ ^-.$ ]]; then
      flags+=( "$arg" )
    elif [[ -f "$arg" ]]; then
      files+=( "$arg" )
    else
      subpattern="$arg"
    fi
  done

  purged_subpattern=$(ere_quote "$subpattern")
  pattern="(.+.txt:)?(\d*:)?$purged_subpattern"

  create_source

  for str in "${full_source[@]}"; do
    temp_arr=()
    
    split_on_sep "temp_arr" "$sep" "$str"
    
    if [[ "${#files[@]}" -gt 1 ]]; then
      source+=( "${temp_arr[0]}:${temp_arr[2]}" )
    else
      source+=( "${temp_arr[2]}" )
    fi

  done
  
  if [[ ! ${flags[*]} =~ -n ]]; then
    
    for str in "${source[@]}"; do
      purge_str=()
      split_on_sep "purge_str" "$in_str_sep" "$str"

      if [[ "${purge_str[-1]}" =~ $pattern ]]; then
        good_list+=( "$str" )
      fi
    done
  
  fi
  
  OPTIONS=":nlivx"

  while getopts ${OPTIONS} option; do
    case ${option} in
      n)
        source=()
        good_list=()

        for str in "${full_source[@]}"; do
          temp_arr=()
          
          split_on_sep "temp_arr" "$sep" "$str"
          
          if [[ "${#files[@]}" -gt 1 ]]; then
            source+=( "${temp_arr[0]}:${temp_arr[1]}:${temp_arr[2]}" )
          else
            source+=( "${temp_arr[1]}:${temp_arr[2]}" )
          fi
        done

        for str in "${source[@]}"; do
          purge_str=()
          split_on_sep "purge_str" "$in_str_sep" "$str"
          
          if [[ "${purge_str[-1]}" =~ $pattern ]]; then
            good_list+=( "$str" )
          fi
        done
        ;;
      x)
        good_list=()
        pattern="$pattern$"

        for str in "${source[@]}"; do
          purge_str=()
          split_on_sep "purge_str" "$in_str_sep" "$str"

          if [[ "${purge_str[-1]}" =~ $pattern ]] || { [[ ${flags[*]} =~ -i ]] && [[ "${purge_str[-1]^^}" =~ ${pattern^^} ]]; }; then
            good_list+=( "$str" )
          fi
        done
        ;;
      i)
        good_list=()
        pattern="${pattern^^}"

        for str in "${source[@]}"; do
          purge_str=()
          split_on_sep "purge_str" "$in_str_sep" "$str"
          
          if [[ "${purge_str[-1]^^}" =~ $pattern ]]; then
            good_list+=( "$str" )
          fi
        done
        ;;
      l)
        :
        ;;
      v)
        :
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

  if [[ ${flags[*]} =~ -l ]]; then
    local good_files

    for file in "${files[@]}"; do
      if [[ ${good_list[*]} =~ $file ]] && [[ ! ${good_files[*]} =~ $file ]]; then
        good_files+=( "$file" )
      fi
    done

    if [[ "${#files[@]}" -gt 1 ]]; then
      for file in "${good_files[@]}"; do echo "$file"; done
    elif [[ -n "${good_list[*]}" ]] && [[ "${#files[@]}" -eq 1 ]]; then
      echo "${files[0]}"
    fi
  
  else

    if [[ ! ${flags[*]} =~ -v ]]; then
      for str in "${good_list[@]}"; do
        echo "$str"
      done
    
    else
      
      for str in "${source[@]}"; do
        if [[ ! ${good_list[*]} =~ "$str" ]]; then
          echo "$str"
        fi
      done

    fi
  fi
}

setup
main "$@"
teardown
