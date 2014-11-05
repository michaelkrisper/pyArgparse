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
    parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()
    result = fib(args.num)

    if args.verbose:
        print("The {}th fib number is {}".format(args.num, result))
    elif args.quiet:
        print(result)
    else:
        print("Fib({}) = {}".format(args.num, result))

    if args.output:
        with open("fibonacci.txt", "a") as f:
            f.write("{}\n".format(result))


if __name__ == "__main__":
    main()