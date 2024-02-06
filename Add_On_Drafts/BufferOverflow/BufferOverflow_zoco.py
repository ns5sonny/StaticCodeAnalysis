import cppcheckdata

msgB = 'Code DOES NOT pass test'
msgSC = 'Watch out! Using strcpy is not the best idea'
msgP = 'Code passes test'
@cppcheck.checker
def strcpy_check(cfg, data):
    has_strcpy = False
    has_strlen = False
 #   has_str1 = False
 #   has_ptr = False
    for token in cfg.tokenlist:
        if token.str == 'strcpy':
            has_strcpy = True
        if token.str == 'strlen':
            has_strlen = True
  #      elif token.str == 'str[]':
   #         has_str1 = True
    #    elif token.str == '*ptr':
     #       has_ptr = True

    if has_strcpy and not has_strlen:
        cppcheckdata.reportError(token, 'information', msgB)
 #   elif has_strcpy and not has_str1:
 #      cppcheckdata.reportError(token, 'information',msgB)
 #   elif has_strcpy and not has_ptr:
 #       cppcheckdata.reportError(token, 'information', msgB)
 #   elif has_strcpy and has_strlen:
 #       cppcheckdata.reportPass(token, 'information', msgP)
 #   elif has_strcpy and has_str1:
 #       cppcheckdata.reportPass(token, 'information', msgP)
 #   elif has_strcpy and has_ptr:
 #       cppcheckdata.reportPass(token, 'information', msgP)
    elif has_strcpy:
        cppcheckdata.reportError(token, 'information', msgSC)
    else:
        cppcheckdata.reportPass(token, 'information', 'Code is not applicable to this add on')
