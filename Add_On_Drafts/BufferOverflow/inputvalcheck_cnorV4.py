#!/usr/bin/env python3
#
# Locate inputs in the code
#
# Strategy taken from findcasts.py

import cppcheck

@cppcheck.checker
def compCheck(cfg, data):
    for token in cfg.tokenlist:
        # Detection to see if we can identify a comparison (e.g. strlen < some number)
        if token.isComparisonOp:
            cppcheck.reportError(token, 'information', 'found a comparison')

@cppcheck.checker            
def inputval_checker(cfg, data):
    for token in cfg.tokenlist:
        if token.isName and token.str == 'scanf':
            cppcheck.reportError(token, 'information', 'found an input, scanf is not secure')
        if token.isName and token.str == 'fgets':
            cppcheck.reportError(token, 'information', 'found an input, fgets requires validation')
        if token.isName and token.str == 'strcpy':
            cppcheck.reportError(token, 'information', 'this is a potentially unsafe function! Ensure proper guards')
        
        
@cppcheck.checker # it took an embarrassingly long time to figure out I need this line before every method or they won't run
# Method to determine if proper guards are being used for strcpy
def buffOverflowCheck(cfg, data):
    myLoc = '' # I'd like to be able to identify where the If statement is outside its loop
    for scope in cfg.scopes:
        if scope.type == 'If':
            myLoc = scope.bodyStart
            cppcheck.reportError(myLoc, 'information', 'found an If statement')
            # ideally I'd like to be checking to see if strcpy is used inside this statement
        if scope.type == 'Else': # just to see if this works too
            cppcheck.reportError(scope.bodyStart, 'information', 'caught by Else')

    """ for token in cfg.tokenlist:
        while token.str != myLoc:
            if token.isName and token.str == 'strcpy':
                cppcheck.reportError(token, 'information', 'found strcpy inside if statement') """

