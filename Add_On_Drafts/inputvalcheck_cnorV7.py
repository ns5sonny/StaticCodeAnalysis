#!/usr/bin/env python3
#
# Find strlen then see if strcpy exists in same scope
#
# Strategy taken from findcasts.py

import cppcheck

@cppcheck.checker
def compCheck(cfg, data):
    lengthCheckCpy = 'false'
    checkScope = "0"
    for token in cfg.tokenlist:
        # Detection to see if we can identify a comparison (e.g. strlen < some number)
        
        if token.isComparisonOp and token.next.isNumber and token.astOperand2.next.link.next.str == 'strlen':
            #cppcheck.reportError(token, 'information', 'forward comparing strlen to a number')
            checkScope = token.next.next.next.scope
        
        if token.isName and token.str == 'strcpy' and token.scope == checkScope:
            #cppcheck.reportError(token, 'information', 'strlen check and strcpy are in same scope')
            lengthCheckCpy = 'true'

        if token.isName and token.str == 'strcpy' and lengthCheckCpy == 'false':
            cppcheck.reportError(token, 'information', 'strcpy does not have proper guards')
        

#@cppcheck.checker
def inputval_checker(cfg, data):
    for token in cfg.tokenlist:
        if token.isName and token.str == 'scanf':
            cppcheck.reportError(token, 'information', 'found an input, scanf is not secure')
        if token.isName and token.str == 'fgets':
            cppcheck.reportError(token, 'information', 'found an input, fgets requires validation')
        if token.isName and token.str == 'strcpy':
            cppcheck.reportError(token, 'information', 'this is a potentially unsafe function! Ensure proper guards')