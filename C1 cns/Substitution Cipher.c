#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void encrypt(char *message, char *key) 
{
    int i;
	for (i = 0; i < strlen(message); i++) 
	{
        if (message[i] >= 'a' && message[i] <= 'z') 
		{
            message[i] = key[message[i] - 'a'];
        }
    }
}
void decrypt(char *message, char *key) 
{
	int i,j;
    for (i = 0; i < strlen(message); i++) 
	{
        for (j = 0; j < 26; j++) 
		{
            if (message[i] == key[j]) 
			{
                message[i] = 'a' + j;
                break;
            }
        }
    }
}
int main() 
{
    char key[26];
    int i;
    printf("Enter the substitution key (26 lowercase letters in random order): ");
    scanf("%s", key);
    if (strlen(key) != 26) 
	{
        printf("Invalid key length. Please provide 26 letters.\n");
        return 1;
    }
    for (i = 0; i < 26; i++) 
	{
        if (key[i] < 'a' || key[i] > 'z') 
		{
            printf("Invalid key. Please provide only lowercase letters.\n");
            return 1;
        }
    }
    char message[100];
    printf("Enter the message to encrypt: ");
    scanf(" %[^\n]s", message);
    encrypt(message, key);
    printf("Encrypted message: %s\n", message);
    decrypt(message, key);
    printf("Decrypted message: %s\n", message);
}
