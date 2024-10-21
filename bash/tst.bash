#!/usr/bin/env bash

arr=( a b c )
echo "${arr[-1]}"

arr="${arr[-1]^^}"
echo $arr
declare -p arr