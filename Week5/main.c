#include <stdio.h> //printf
#include <string.h> //strncpy
#include <stdlib.h> //calloc

int main()
{
    char s[] = "Hello, World!\n";
    printf(s);
    int length = strlen(s);
    printf("Original length = %d\n",length);
    int size = sizeof(s);
    printf("Original size = %d\n",size);
    char* ptr = (char *)calloc(length, sizeof(char));
    strncpy(ptr, s, length);
    strncpy((ptr + length), s, size);
    ptr[length-1]=32;
    printf(ptr);
    int new_length = strlen(ptr);
    printf("New length = %d\n",new_length);
    int new_size = sizeof(ptr);
    printf("New size = %d\n",new_size);
    free(ptr);
   
    return 0;
}


