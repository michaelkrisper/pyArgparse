#!/usr/bin/python3
# coding=utf-8
"""
Argparse Demo
https://www.youtube.com/watch?v=rnatu3xxVQE&list=WL&index=51
"""
import argparse

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number you wish to calculate", type=int)
    args = parser.parse_args()
    print(args)

    result = fib(args.num)
    print("The {}th fib number is {}".format(args.num, result))


if __name__ == "__main__":
    main()