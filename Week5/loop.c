#include <stdio.h> //printf

int main() {

    for(int i = 0; i < 20; i++) {
        if(i<10){
            printf("Loop 0%d. Hello, World!\n", i);
        }else{
            printf("Loop %d. Hello, World!\n", i);
        }
    }

    return 0;
}
