import argparse
import sys

def parseIt():
    parser = argparse.ArgumentParser(description='Please add some arguments. This list can help you with that')

    parser.add_argument('config',
                        help='The basic config of this app',
                        nargs='?'
    )

    args = parser.parse_args()

    return args
