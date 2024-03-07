/** @file test_3.c
 *
 *  @brief Formal Methods for Information Security Capstone - Buffer overflow example #3
 *
 *  The copyData function causes a buffer overflow when an array with up to 256 elements is copied to an array with 16 elements using the strcpy function
 *	The strcpy function call is guarded by an if: if(16 > strlen(input)) 
 *	The add-on should flag the strcpy as guarded
 *
 *  @author Mohamed M. Elwakil
 */
 
#include <stdio.h>
#include <string.h>

void copyData(char *input) {
  char buffer[16];
  
  // Check input length
  if(16 > strlen(input)) { 
    strcpy(buffer, input);
  }
  else {
    printf("Input too long\n");
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