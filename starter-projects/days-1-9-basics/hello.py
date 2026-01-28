#!/usr/bin/env python3
"""
Hello World application for Advent of Claude Code.

This is the main entry point for the greeting application.
"""

import argparse
from utils import create_greeting


def main():
    """Main function to run the greeting application."""
    parser = argparse.ArgumentParser(
        description="A friendly greeting application"
    )
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="Name to greet (default: World)"
    )

    args = parser.parse_args()
    greeting = create_greeting(args.name)
    print(greeting)


if __name__ == "__main__":
    main()
