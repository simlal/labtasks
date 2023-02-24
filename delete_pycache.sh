#!/bin/sh

# Find all pycache files and recursively remove them from the Django dir.
# Run before staging files and committing

find . | grep "__pycache__/" | xargs rm -rf