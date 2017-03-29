#!/usr/bin/env python3

def f2c (f_temp):
    return (f_temp - 32) * 5 / 9

def c2f (c_temp):
    return c_temp * 9 / 5 + 32

if __name__ == '__main__':

    for c in range (20):
        print ("%0.2f" % c2f (c))

    for f in range (75, 85):
        print ("%0.2f" % f2c (f))
