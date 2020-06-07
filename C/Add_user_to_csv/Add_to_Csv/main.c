#include <stdio.h>
#include <stdlib.h>
/* Author, Yusef Quinlan */
int main()
{



    FILE * fptr2 = fopen("cfile.csv", "a");
    fputs("firstName,SecondName\n", fptr2);
    char  aChar[256];
    void insert(){
        char a[256],b[256];
        printf("What is the first name?:    \n");
        scanf(" %2048[0-9a-zA-Z ]s", &a);
        printf("What is the second name?:   \n");
        scanf(" %2048[0-9a-zA-Z ]s", &b);
        fputs(a,fptr2);
        fputs(",",fptr2);
        fputs(b,fptr2);
        fputs("\n",fptr2);
        char yn;
        printf("Would you like to enter another person? y/n for yes/no : \n");
        scanf("%s",&yn);
        if(yn =='y'){
            insert();
        }
    }
    insert();
    return 0;
}
