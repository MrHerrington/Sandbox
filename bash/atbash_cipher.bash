<< '////'

Instructions

Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in
the alphabet such that the resulting alphabet is backwards. The first letter is replaced with the last
letter, the second with the second-last, and so on.
An Atbash cipher for the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba

It is a very weak cipher because it only has one possible key, and it is a simple mono-alphabetic
substitution cipher. However, this may not have been an issue in the cipher's time.
Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters,
leaving numbers unchanged, and punctuation is excluded. This is to make it harder to guess
things based on word boundaries. All text will be encoded as lowercase letters.

Examples

Encoding test gives gvhg
Encoding x123 yes gives c123b vh
Decoding gvhg gives test
Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog

////


#!/usr/bin/env bash

main () {
  declare -A dict

  dict["a"]="z"
  dict["b"]="y"
  dict["c"]="x"
  dict["d"]="w"
  dict["e"]="v"
  dict["f"]="u"
  dict["g"]="t"
  dict["h"]="s"
  dict["i"]="r"
  dict["j"]="q"
  dict["k"]="p"
  dict["l"]="o"
  dict["m"]="n"
  dict["n"]="m"
  dict["o"]="l"
  dict["p"]="k"
  dict["q"]="j"
  dict["r"]="i"
  dict["s"]="h"
  dict["t"]="g"
  dict["u"]="f"
  dict["v"]="e"
  dict["w"]="d"
  dict["x"]="c"
  dict["y"]="b"
  dict["z"]="a"

  operation="$1"
  phrase="$2"
  new_phrase=""
  res_phrase=""
  counter=0
  
  for ((i=0; i<${#phrase}; i++)); do
    
    if [[ ${phrase:$i:1} =~ [[:alpha:]] ]]; then
      letter=${phrase:$i:1}
      lc_letter=${letter,}
      new_phrase+="${dict[$lc_letter]}"
    fi

    if [[ ${phrase:$i:1} =~ [[:digit:]] ]]; then
      new_phrase+=${phrase:$i:1}
    fi

  done

  if [[ $operation == "encode" ]]; then

    for ((i=0; i<${#new_phrase}; i++)); do
      
      if [[ $counter -eq 5 ]]; then
        res_phrase="$res_phrase "
        (( i-- ))
        counter=0
      else
        res_phrase+="${new_phrase:$i:1}"
        (( counter++ ))
      fi

    done
  
  elif [[ $operation == "decode" ]]; then
    
    for ((i=0; i<${#new_phrase}; i++)); do
      res_phrase+="${new_phrase:$i:1}"
    done

  fi

  echo "$res_phrase"
}

main "$@"
