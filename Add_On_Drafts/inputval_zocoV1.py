#Draft 1 of Add on Validating Input Error

#Imports
import re
import sys
import os
import cppcheckdata

#define functions that involve inputting data
id_inputFuncts ={
'cin',
'getline',
'ifStream',
'input',
'argc',
'argv',
'>>',
'<<',
'scanf',
'fgets',
}

#define functions that validate input 
id_validateFuncts = {
'isPositiveIngeger',
'isNumeric',
'isAlphaNumeric',
'isAlphaNumeric',
'isValidEmail',
'isValidDate',
'isIntRange'
}

#Define Vars with Msgs
errorID = '2024'
msgB = '!! Code does not pass Input Validation test !!'
msgG = 'Code PASSES Input Validation test!!'
msgNA = 'Input Validation test NOT APPLICABLE!'
msgWUT = 'UNKNOWN ERROR: What the heck happened?!?'

#Reporting Error function
def reportError(token, msgB, errorID, lineID):
	cppcheckdata.reportError(token, msgB, errorID, lineID)

#Report pass function
def reportPass(token, msgG):
	cppcheckdata.reportPass(token, msgG)
	
#Report not applicable function
def reportNA(token, msgNA):
	cppcheckdata.reportNA(token, msgNA)
	
#Report other wild error
def reportWUT(token, msgWUT):
	cppcheckdata.reportWUT(token, msgWUT)

#search file for input functs
def check_takeInput(cfg):
	for token in cfg.tokenlist:
		if token.str in id_inputFuncts:
			#if it does have an input funct and it has a validate funct, pass test
			if token.str in id_validateFuncts:
				reportPass(token, msgG)
			#if it has an input funct but not a validate funct, fail test
			if token.str not in id_validateFuncts:
				reportError(token, msgB)
			#if stuff goes crazy, error error
			else:
				reportWUT(token, msgWUT)
		#if it does not have an input funct, pass test
		if token.str not in id_inputFuncts:
			reportNA(token, msgNA)
		#if anything crazy happens, throw other error msg
		else:
			reportWUT(token, msgWUT)
	#at end of full function, need
	sys.exit(cppcheckdata.EXIT_CODE)

