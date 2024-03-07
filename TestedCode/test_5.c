/** @file test_5.c
 *
 *  @brief Formal Methods for Information Security Capstone - Buffer overflow example #5
 *  The copyData function causes a buffer overflow when an array with up to 256 elements is copied to an array with 16 elements using the strcpy function
 *	The strcpy function call is not guarded. The condition of the if statement is irrelevant.
 *	The add-on should flag the strcpy as not guarded
 *
 *  @author Mohamed M. Elwakil
 */
 
#include <stdio.h>
#include <string.h>

void copyData(char *input) {
  char buffer[16];
  
  // Check input length
  if(1<2) { 
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