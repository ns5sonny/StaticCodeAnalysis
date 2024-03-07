#!/usr/bin/env python3
#
# Addon to check code for input validation errors with the use of the strcpy() method
# 
# Authors: 1/c Charles Norman and 1/c Zoe Cousineau

import cppcheck

@cppcheck.checker
def strcpyGuarded(cfg, data):
    lengthCheckCpy = 'false'
    properChecks = 'false'

    checkScope = "0"
    compScope = "1"
    lengthScope = "2"

    ifBodyScope = "3"
    ifStateScope = "4"
    elseBodyScope = "5"

    #numScope = "0"
    for scope in cfg.scopes:
        if scope.type == "If":
            ifStateScope = scope.nestedIn
            ifBodyScope = scope
            #cppcheck.reportError(scope.bodyStart, 'information', 'found a scope')
        if scope.type == 'Else':
            elseBodyScope = scope


    for token in cfg.tokenlist:
        # Detection to see if we can identify a comparison (e.g. strlen < some number)

        if token.isComparisonOp and token.astParent.str == "(":
            compScope = token.scope # scope inside if statement
            checkScope = token.astParent.link.next.scope # the parent is the first (, then link to 
            # the ), then .next with be the { of the body, which should be the same as ifBodyScope
        
        if token.str == 'strlen':
            lengthScope = token.scope
        if compScope == lengthScope:
            properChecks = 'true'
            # Shows we have a comparison to strlen in the same scope

        # testing scope loop successes
        #if token.str == 'strcpy' and (token.scope == ifBodyScope or token.scope == elseBodyScope):
        #    cppcheck.reportError(token, 'information', 'found the scope for strcpy yay!')
        #if token.isComparisonOp and token.scope == ifStateScope:
        #    cppcheck.reportError(token, 'information', 'found right scope for comp')
        #if token.str == 'strlen' and token.linenr
        # reminder to use linenr to ensure comp and strlen in same statement



        if token.isName and token.str == 'strcpy' and (token.scope == checkScope or token.scope == elseBodyScope):
            cppcheck.reportError(token, 'information', 'strcpy is in scope "if( < ){ or else{ ')
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