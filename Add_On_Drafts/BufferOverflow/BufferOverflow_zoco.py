import cppcheck

msgB = "Code DOES NOT pass test"
msgSC = "Watch out! Using strcpy is not the best idea"
msgP = "Code passes test"

@cppcheck.checker
def strcpyWOstrlen_check(cfg):
    has_strcpy = False
    has_strlen = False
    has_str1 = False
    has_ptr = False
    for token in cfg.tokenlist:
        if token.str == "strcpy":
            has_strcpy = True
        elif token.str == "strlen":
            has_strlen = True
        elif token.str == "str[]"
            has_str1 = True
        elif token.str == "*ptr"
            has_ptr = True

    if has_strcpy and not has_strlen:
        cppcheckdata.reportError("strcpy", msgB)
    if has_strcpy and not has_str1:
        cppcheckdata.reportError("strcpy", msgB)
    if has_strcpy and not has_ptr:
        cppcheckdata.reportError("strcpy", msgB)
    elif has_strcpy and has_strlen:
        cppcheckdata.reportPass("strcpy", msgP)
    elif has_strcpy and has_str1:
        cppcheckdata.reportPass("strcpy", msgP)
    elif has_strcpy and has_ptr:
        cppcheckdata.reportPass("strcpy", msgP)
    elif has_strcpy:
        cppcheckdata.reportError("strcpy", msgSC)
    else:
        cppcheckdata.reportPass("strcpy", "Code is not applicable to this add on")
