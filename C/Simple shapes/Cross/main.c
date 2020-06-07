#include <stdio.h>
#include <stdlib.h>
/* Author Yusef Quinlan */
void main()
{

    int a;
    int b;
    for(b=0;b<39;b++)
    {
        if ((b==0) || (b==38) )
        {
            for(a=0;a<30;a++)
            {
                if (a< 20)
                {
                    printf(" ");
                }
                else if((a > 19) && ( a < 29))
                {
                    printf("%c",248);
                }
                else if(a==29){
                    printf("%c\n",248);
                }
            }
        }
        else if((b > 0) && (b < 14) )
        {
            for(a=0;a<30;a++)
            {
                if (a<20)
                {
                   printf(" ");
                }
                else if (a==20){
                    printf("%c",248);
                }
                else if( (a >20) && (a<29) )
                {
                    printf(" ");
                }
                else if(a==29){
                    printf("%c\n", 248);
                }
            }
        }
        else if((b == 14))
        {
             for(a=0;a<51;a++){
            if(a<20){
                printf("%c",248);
            }
            else if ((a > 19) && (a < 30))
                {
                    printf(" ");
                }
            else if ( (a > 30) && (a < 50))
            {
                printf("%c",248);
            }
            else if(a==50)
            {
                printf("%c\n",248);
            }
             }
        }
          else if((b > 14) && (b < 22) ){
          for(a=0;a<50;a++){
            if (a==0)
            {
                printf("%c",248);
            }
            else if((a > 0) &&(a<49))
            {
                printf(" ");
            }
            else if(a==49)
            {
                printf("%c\n",248);
            }
          }
        }
         else if((b == 23))
        {
             for(a=0;a<51;a++){
            if(a<20){
                printf("%c",248);
            }
            else if ((a > 19) && (a < 30))
                {
                    printf(" ");
                }
            else if ( (a > 30) && (a < 50))
            {
                printf("%c",248);
            }
            else if(a==50)
            {
                printf("%c\n",248);
            }
             }
        }
         else if((b > 23) && (b < 37) )
        {
            for(a=0;a<30;a++)
            {
                if (a<20)
                {
                   printf(" ");
                }
                else if (a==20){
                    printf("%c",248);
                }
                else if( (a >20) && (a<29) )
                {
                    printf(" ");
                }
                else if(a==29){
                    printf("%c\n", 248);
                }
            }
        }
    }
}
