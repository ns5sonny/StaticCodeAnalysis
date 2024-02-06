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
        if token.isName and token.str == 'strcpy':
            cppcheck.reportError(token, 'information', 'this is a potentially unsafe function! Ensure proper guards')


# Method to determine if proper guards are being used for strcpy
def buffOverflowCheck(cfg, data):
    for scope in data.scopes: 
        if scope.type == 'If': # and simpleMatch(scope.bodyStart, '{'):
            cppcheck.reportError(scope.bodyStart, 'information', 'found a guard')
    # Originally this was way too complex and checked for too much at once,
    # now the goal is to determine if a guard is in place before moving on to more
    # complex tasks.