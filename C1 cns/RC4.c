#include <stdio.h>
#include <string.h>
void display(int disp[], int length) {
	int l;
    char convert[length];
    for (l = 0; l < length; l++) {
        convert[l] = (char)disp[l];
        printf("%c", convert[l]);
    }
}
int main() {
    int temp = 0, i, l;
    char ptext[256];
    char key[256];
    int s[256];
    int k[256];
    printf("\nENTER PLAIN TEXT: ");
    fgets(ptext, sizeof(ptext), stdin);
    printf("ENTER KEY TEXT: ");
    fgets(key, sizeof(key), stdin);
    int ptextLen = strlen(ptext) - 1;
    int keyLen = strlen(key) - 1;
    int cipher[ptextLen];
    int decrypt[ptextLen];
    int ptexti[ptextLen];
    int keyi[keyLen];
    for (i = 0; i < ptextLen; i++) {
        ptexti[i] = (int)ptext[i];
    }
    for (i = 0; i < keyLen; i++) {
        keyi[i] = (int)key[i];
    }
    for (i = 0; i < 255; i++) {
        s[i] = i;
        k[i] = keyi[i % keyLen];
    }
    int j = 0;
    for (i = 0; i < 255; i++) {
        j = (j + s[i] + k[i]) % 256;
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
    i = 0;
    j = 0;
    int z = 0;
    for (l = 0; l < ptextLen; l++) {
        i = (l + 1) % 256;
        j = (j + s[i]) % 256;
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        z = s[(s[i] + s[j]) % 256];
        cipher[l] = z ^ ptexti[l];
        decrypt[l] = z ^ cipher[l];
    }
    printf("ENCRYPTED: ");
    display(cipher, ptextLen);
    printf("\nDECRYPTED: ");
    display(decrypt, ptextLen);
    return 0;
}
