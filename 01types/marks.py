#!/usr/bin/env python3

marks = []

print ("Enter the marks. One at a time. Finish with -1.")

while 1:
    next = input (": ")

    if next != "-1":
        marks.append (int (next))
    else:
        break

if len (marks) == 0:
    print ("No marks entered.")
else:
    print ("Highest Mark: {0}".format (max (marks)))
    print ("Lowest Mark:  {0}".format (min (marks)))
    print ("Average Mark: {:.2f}".format (sum (marks) / len (marks)))