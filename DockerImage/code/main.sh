#!/bin/bash

mkdir -p /ext/plaintext_policies
python2 Preprocessor.py --input "/ext/html_policies" --output "/ext/plaintext_policies"
