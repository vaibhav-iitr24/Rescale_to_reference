#!/bin/bash
#$1: List of input files (space-separated)
#$2: Merged output file
#$3: Frequency output file

{
    echo "$1" | tr ' ' '\n' | while read -r fname; do
        cat "$fname"
    done
} > "$2"


awk '{diff = $3 - $2; print diff}' "$2" | sort -n | uniq -c | awk '{print $2, $1}' | tr ' ' '\t' > "$3"

