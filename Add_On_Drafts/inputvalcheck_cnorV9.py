#!/usr/bin/env python3
#
# Find strlen then see if strcpy exists in same scope
#
# Strategy taken from findcasts.py

import cppcheck

@cppcheck.checker
def strcpyGuardCheck(cfg, data):
    lengthCheckCpy = 'false'
    properChecks = 'false'
    checkScope = "0"
    compScope = "0"
    lengthScope = "0"

    ifBodyScope = "0"
    ifStateScope = "0"

    #numScope = "0"
    for scope in cfg.scopes:
        if scope.type == "If":
            ifStateScope = scope.nestedIn
            ifBodyScope = scope
            #cppcheck.reportError(scope.bodyStart, 'information', 'found a scope')


    for token in cfg.tokenlist:
        # Detection to see if we can identify a comparison (e.g. strlen < some number)
        
        """ if token.isComparisonOp and token.next.isNumber and token.astOperand2.next.link.next.str == 'strlen':
            #cppcheck.reportError(token, 'information', 'forward comparing strlen to a number')
            checkScope = token.next.next.next.scope """

        if token.isComparisonOp and token.astParent.str == "(":
            compScope = token.scope # scope inside if statement
            checkScope = token.astParent.link.next.scope # the parent is the first (, then link to 
            # the ), then .next with be the { of the body, which should have strcpy in same scope
        if token.str == 'strlen':
            lengthScope = token.scope

        """ if token.isNumber:
            numScope = token.scope """
        
        if compScope == lengthScope:
            properChecks = 'true'
            # Shows we have a comparison to strlen in the same scope

        # testing scope loop successes
        if token.str == 'strcpy' and token.scope == ifBodyScope:
            cppcheck.reportError(token, 'information', 'found right scope for strcpy')
        if token.isComparisonOp and token.scope == ifStateScope:
            cppcheck.reportError(token, 'information', 'found right scope for comp')
        #if token.str == 'strlen' and token.linenr
        # reminder to use linenr to ensure comp and strlen in same statement



        if token.isName and token.str == 'strcpy' and token.scope == checkScope:
            cppcheck.reportError(token, 'information', 'strlen check and strcpy are in same scope')
            # extra "error" to show our checks are happening properly, i.e. success state
            lengthCheckCpy = 'true'

        if (token.isName and token.str == 'strcpy') and (lengthCheckCpy == 'false' or properChecks == 'false'):
            cppcheck.reportError(token, 'information', 'strcpy does not have proper guards')
        

#@cppcheck.checker
def inputval_checkers(cfg, data):
    for token in cfg.tokenlist:
        if token.isName and token.str == 'scanf':
            cppcheck.reportError(token, 'information', 'found an input, scanf is not secure')
        if token.isName and token.str == 'fgets':
            cppcheck.reportError(token, 'information', 'found an input, fgets requires validation')
        if token.isName and token.str == 'strcpy':
            cppcheck.reportError(token, 'information', 'this is a potentially unsafe function! Ensure proper guards')