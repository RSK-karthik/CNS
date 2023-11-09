#include<stdio.h>

int main()
{
    char arr[] = "Hello World";
    printf("Original string: %s\n" ,arr );
    printf("Xor string: ");
    for(int i=0;arr[i]!='\0';i++)
    {
        char result = arr[i]^127;
        printf("%c",result);
    }
    printf("\n");
    return 0;
}
