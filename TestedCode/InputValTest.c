#include <stdio.h>

int main() {
    char bufferScan[10];
    
    // This line should be flagged by the input validation checker
    scanf("%s", bufferScan);

    // Space for other code...

    char bufferGets[100];

    // Prompt the user for input
    printf("Enter some text: ");

    // Use fgets to get input from the user, should flag in checker
    fgets(bufferGets, sizeof(bufferGets), stdin);

    // Display the entered text
    printf("You entered: %s", bufferGets);

    return 0;
}