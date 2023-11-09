#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
int gcdExtended(int a, int b, int *x, int *y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }
    int x1, y1;
    int gcd = gcdExtended(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return gcd;
}
void getKeyMatrix(int keyMatrix[2][2]) {
	int i, j;
    printf("Enter key matrix (4 integers): ");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            scanf("%d", &keyMatrix[i][j]);
        }
    }
}
void isValidMatrix(int keyMatrix[2][2]) {
    int det = keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0];
    if (det == 0) {
        printf("Det equals to zero, invalid key matrix!\n");
        exit(1);
    }
    int x, y;
    if (gcdExtended(det, 26, &x, &y) != 1) {
        printf("Determinant is not invertible modulo 26, invalid key matrix!\n");
        exit(1);
    }
}
void reverseMatrix(int keyMatrix[2][2], int reverseMatrix[2][2]) {
    int det = keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0];
    int detMod26 = (det % 26 + 26) % 26;
    int factor;
    for (factor = 1; factor < 26; factor++) {
        if ((detMod26 * factor) % 26 == 1) {
            break;
        }
    }
    reverseMatrix[0][0] = (keyMatrix[1][1] * factor) % 26;
    reverseMatrix[0][1] = (26 - keyMatrix[0][1]) * factor % 26;
    reverseMatrix[1][0] = (26 - keyMatrix[1][0]) * factor % 26;
    reverseMatrix[1][1] = (keyMatrix[0][0] * factor) % 26;
}
void echoResult(const char *label, int adder, int *phrase, int size) {
	int i;
    printf("%s", label);
    for (i = 0; i < size; i += 4) {
        printf("%c%c", phrase[i] + (64 + adder), phrase[i + 1] + (64 + adder));
        if (i + 4 < size) {
            printf("-");
        }
    }
    printf("\n");
}
void encrypt(const char *phrase, int alphaZero) {
    int keyMatrix[2][2];
    int i;
    getKeyMatrix(keyMatrix);
    isValidMatrix(keyMatrix);
    int len = strlen(phrase);
    int phraseToNum[len];
    for (i = 0; i < len; i++) {
        phraseToNum[i] = toupper(phrase[i]) - (64 + alphaZero);
    }
    int phraseEncoded[len * 2];
    for (i = 0; i < len; i += 2) {
        int x = (keyMatrix[0][0] * phraseToNum[i] + keyMatrix[0][1] * phraseToNum[i + 1]) % 26;
        int y = (keyMatrix[1][0] * phraseToNum[i] + keyMatrix[1][1] * phraseToNum[i + 1]) % 26;
        phraseEncoded[i * 2] = alphaZero ? x : (x == 0 ? 26 : x);
        phraseEncoded[i * 2 + 1] = alphaZero ? y : (y == 0 ? 26 : y);
    }
    echoResult("Encrypted message: ", alphaZero, phraseEncoded, len * 2);
}
void decrypt(const char *phrase, int alphaZero) {
    int keyMatrix[2][2], revKeyMatrix[2][2];
    getKeyMatrix(keyMatrix);
    isValidMatrix(keyMatrix);
    int len = strlen(phrase);
    int phraseToNum[len];
    int i;
    for (i = 0; i < len; i++) {
        phraseToNum[i] = toupper(phrase[i]) - (64 + alphaZero);
    }
    reverseMatrix(keyMatrix, revKeyMatrix);
    int phraseDecoded[len * 2];
    for (i = 0; i < len; i += 2) {
        phraseDecoded[i * 2] = (revKeyMatrix[0][0] * phraseToNum[i] + revKeyMatrix[0][1] * phraseToNum[i + 1]) % 26;
        phraseDecoded[i * 2 + 1] = (revKeyMatrix[1][0] * phraseToNum[i] + revKeyMatrix[1][1] * phraseToNum[i + 1]) % 26;
    }
    echoResult("Decrypted message: ", alphaZero, phraseDecoded, len * 2);
}
int main() {
    char opt;
    char phrase[100];
    printf("Hill Cipher Implementation (2x2)\n");
    printf("-------------------------\n");
    printf("1. Encrypt text (A=0,B=1,...Z=25)\n");
    printf("2. Decrypt text (A=0,B=1,...Z=25)\n");
    printf("3. Exit\n\n");
    while(1) {
    	printf("Select your choice: ");
    	scanf(" %c", &opt);
    	switch (opt) {
        	case '1':
            	printf("Enter message to encrypt: ");
        	    scanf("%s", phrase);
	            encrypt(phrase, 1);
	            break;
	        case '2':
	            printf("Enter message to decrypt: ");
	            scanf("%s", phrase);
	            decrypt(phrase, 1);
	            break;
	        case '3':
	        	exit(1);
    	}
	}
    return 0;
}
