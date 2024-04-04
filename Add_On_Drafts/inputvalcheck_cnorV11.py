#!/usr/bin/env python3
#
# Addon to check code for input validation errors with the use of the strcpy() method
# 
# Authors: 1/c Charles Norman and 1/c Zoe Cousineau

import cppcheck

@cppcheck.checker
def strcpyGuarded(cfg, data):
    # Initialization of checked variables
    lengthCheckCpy = 'false'
    properChecks = 'false'
    sameLine = 'false'

    checkScope = "0"
    compScope = "1"
    lengthScope = "2"

    ifBodyScope = "3"
    ifStateScope = "4"
    elseBodyScope = "5"

    strlenLnNbr = "6"
    compOpLnNbr = "7"

    #numScope = "0"
    for scope in cfg.scopes:
        if scope.type == "If":
            ifStateScope = scope.nestedIn
            ifBodyScope = scope
            #cppcheck.reportError(scope.bodyStart, 'information', 'found a scope')
        if scope.type == "Else":
            elseBodyScope = scope


    for token in cfg.tokenlist:
        if token.isComparisonOp and token.astParent.str == "(":
            compScope = token.scope # scope inside if statement
            checkScope = token.astParent.link.next.scope # the parent is the first (, then link to 
            # the ), then .next with be the { of the body, which should be the same as ifBodyScope
            compOpLnNbr = token.linenr

        if token.str == 'strlen':
            lengthScope = token.scope
            strlenLnNbr = token.linenr
            #cppcheck.reportError(token, 'information', 'testing: ' + str(strlenLnNbr))

        if compScope == lengthScope:
            properChecks = 'true'
            # Shows we have a comparison to strlen in the same scope

        if str(strlenLnNbr) == str(compOpLnNbr):
            sameLine = 'true'
            # Ensuring the strlen is used in a comparison "if statement"

        if (token.isName and token.str == 'strcpy') and ((properChecks == 'true' and sameLine == 'true') or token.scope == elseBodyScope):
            cppcheck.reportError(token, 'information', 'strcpy is in scope "if( < ){" or "else{" : properly guarded ')
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