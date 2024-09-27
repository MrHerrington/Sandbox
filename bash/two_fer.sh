: "
Introduction

In some English accents, when you say 'two for' quickly, it sounds like 'two fer'. Two-for-one is a way of saying
that if you buy one, you also get one for free. So the phrase 'two-fer' often implies a two-for-one offer.
Imagine a bakery that has a holiday offer where you can buy two cookies for the price of one ('two-fer one!').
You take the offer and (very generously) decide to give the extra cookie to someone else in the queue.

Instructions

Your task is to determine what you will say as you give away the extra cookie.
If you know the person's name (e.g. if they're named Do-yun), then you will say:
One for Do-yun, one for me.
If you don't know the person's name, you will say you instead.
One for you, one for me.
"


#!/usr/bin/env bash

main () {
  echo "One for ${1:-you}, one for me."
}

main "$@"
