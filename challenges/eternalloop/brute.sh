#!/bin/bash
created by n0w4n
# creating numerical list
echo "[-] Creating a numerical list for bruteforcing"
crunch 1 6 1234567890 -o num.list &>/dev/null
# running fcrackzip as long if needed
echo "[-] Running fcrackzip trying the numerical list"
while [[ true ]]; do
    file=$(ls | grep zip)
    fcrackzip -u -D -p num.list $file > result
    pwd=$(cat result | tr -d '\n' | awk '{print $5}')
    result=$(cat result | tr -d '\n' | grep FOUND)
    if [[ -z $result ]]; then
        echo "No password found in file $file"
        break 2
    else
        echo "Password found in file $file == $pwd"
        unzip -q -P "$pwd" "$file"
        rm $file
    fi
done
# cleaning up
rm -f result num.list
