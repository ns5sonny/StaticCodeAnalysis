/** @file test_6.c
 *
 *  @brief Formal Methods for Information Security Capstone - Buffer overflow example #6
 *
 *  The copyData function causes a buffer overflow when a string is copied to a buffer
 *  of smaller size using a loop and the strcpy function.
 *  The strcpy function call is not guarded, and the loop condition does not prevent
 *  the buffer overflow.
 *  The add-on should flag the strcpy as unguarded.
 *
 *  @author Mohamed Elwakil
 */

#include <stdio.h>
#include <string.h>

void copyData(char *input) {
  char buffer[16];
  int i;

  for (i = 0; i < strlen(input); i++) {
    strcpy(buffer, input); // Buffer overflow vulnerability
  }
}

int main() {
  char userInput[256];
  printf("Enter input: ");
  fgets(userInput, sizeof(userInput), stdin);

  copyData(userInput);

  return 0;
}