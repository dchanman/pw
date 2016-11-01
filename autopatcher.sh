#!/bin/bash

echo Hi! Please enter a password

# Get the new hash
read newpassword
HASH=`echo -n $newpassword | sha1sum | awk '{print $1}'`
HASHBYTES=`echo -n $HASH | sed -e 's/\([^ ][^ ]\)/\1 /g'`

# Format our hash as a list of bytes
> newpatch.tmp
for b in $HASHBYTES; do
    echo $b >> newpatch.tmp
done;

# Create the new difffile
paste 33184128.program2-hashpatch.dif newpatch.tmp \
    | awk '{print $1 " " $2 " " $4}' \
    > newpatch.dif

# Patch the program and run
echo "Patching the program with the new password hash..."
python2 myidapatcher.py 33184128.program2.exe newpatch.dif
wine 33184128.program2.exe

# Cleanup
python2 myidapatcher.py 33184128.program2.exe newpatch.dif --revert
rm newpatch.tmp
rm newpatch.dif