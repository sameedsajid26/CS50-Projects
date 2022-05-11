#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
// rejects if no or more than 1 key added
    if (argc != 2)
    {                                                            
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        for(int i = 0; i < strlen(argv[1]); i++)                 // checks if each character of key is a number
        {
        if (!isdigit(argv[1][i]))
        {                                                        // if key not a digit, returns an invalid numbr(1)
            printf("Usage: ./caesar key\n");
            return 1;
        }
        }

        int key = atoi(argv[1]);                                 // argv(1) is the integer key

        string plain = get_string("plain text: ");                // gets the plain text from user

        printf("ciphertext: ");


        for (int i = 0; i<strlen(plain); i++)
        {
            if (isalpha(plain[i]))
            {
                if (islower(plain[i]))
                {
                 char l = ( (( (plain[i] - 'a') + key ) % 26) + 'a' );  //from ascii(a=97) to alpha index(where a is 0) and back to ascii

                 printf("%c", l);
                }

                else if (isupper(plain[i]))
                {
                 char u = ( (( (plain[i] - 'A') + key ) % 26) + 'A' );  //from ascii(A = 65) to alpha index(where A is 0) and back to ascii

                 printf("%c", u);
                }
            }

            else
            {
                printf("%c", plain[i]);                                //prints any other non alpha character as it is
            }
        }
        printf("\n");

    }
}