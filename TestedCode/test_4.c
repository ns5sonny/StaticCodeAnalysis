/** @file test_4.c
 *
 *  @brief Formal Methods for Information Security Capstone - Buffer overflow example #4
 *  The copyData function causes a buffer overflow when an array with up to 256 elements is copied to an array with 16 elements using the strcpy function
 *	The strcpy function call is guarded by the else of an if: if(16 > strlen(input)) 
 *
 *	The add-on should flag the strcpy as guarded
 *
 *  @author Mohamed M. Elwakil
 */
 
#include <stdio.h>
#include <string.h>

void copyData(char *input) {
  char buffer[16];
  
  // Check input length
  if(strlen(input)>16) { 
    printf("Input too long\n");
  }
  else {
	strcpy(buffer, input);
    
    return;
  }
}

int main() {

  char userInput[256];
  printf("Enter input: ");
  fgets(userInput, 256, stdin);

  copyData(userInput);

  return 0;  
}