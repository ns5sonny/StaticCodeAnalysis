#!/usr/bin/env python3
#
# Locate inputs in the code
#
# Strategy taken from findcasts.py

import cppcheck

@cppcheck.checker
def inputval_checker(cfg, data):
    for token in cfg.tokenlist:
        if token.isName and token.str == 'scanf':
            cppcheck.reportError(token, 'information', 'found an input, scanf is not secure')
        if token.isName and token.str == 'fgets':
            cppcheck.reportError(token, 'information', 'found an input, fgets requires validation')