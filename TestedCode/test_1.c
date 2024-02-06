#include <stdio.h>
#include <string.h>

void copyData(char *input) {
  char buffer[16];
  strcpy(buffer, input); // Buffer overflow vulnerability  
}

int main() {
  char userInput[256];
  printf("Enter input: ");
  fgets(userInput, 256, stdin);
  
  copyData(userInput);
  
  return 0;
}