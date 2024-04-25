/** @file test_7.c
 *
 *  @brief Formal Methods for Information Security Capstone - Buffer overflow example #7
 *
 *  The main function calls strcpy without a condition that checks for the destination buffer size.  
 *  However, a buffer overflow will not occur since the size of the array can accommodate the copied string
 *  The add-on should recognize that the destination buffer will not overflow.
 *
 *  @author Mohamed Elwakil
 */


#include <stdio.h>
#include <string.h>

int main() {
    char buffer[2];
    char foo[9];
    strcpy(buffer, "OK!"); // No buffer overflow here!
    printf("%s\n", buffer);
    return 0;
}
