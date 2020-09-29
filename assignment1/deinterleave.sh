#!/bin/bash
#Taken from https://gist.github.com/nathanhaigh/3521724
paste - - - - - - - -  | tee >(cut -f 1-4 | tr "\t" "\n" > $1) | cut -f 5-8 | tr "\t" "\n" > $2