#!/usr/bin/env python3
# dpw@Darryls-iMac.localdomain
# 2023-03-03 21:03:10
#
import datetime

filename = "/tmp/junk.txt"

# using 'with' ensures the file closes correctly...
with open(filename, "w") as f:
    f.write(f"this is a test from me sent {datetime.datetime.now()}\n")
    f.write("bye now...")

print(f"file updated : {filename}")
