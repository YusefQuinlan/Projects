#include <stdio.h>
#include <stdlib.h>
/* Author is Yusef Quinlan */
int main()
{

    {

    int y = 20;
    int x = 21;
    int i;
    int j;
    for(i=0;i<41;i++)
    {

       if (i < 20)
       {
         for (j=0;j <=x;j++)
         {
          if ((j<x) && (j!=y))
          {
              printf(" ");
          }
          else if(j==y)
          {
                printf("%c", 11);
          }
          else if(j==x)
          {
                printf("%c\n",11);
          }

          }
          x+=1;
          y-=1;
         }
         else if(i >= 20)
         {
           for (j=0;j <=x;j++)
           {

           if ((j<x) && (j!=y))
           {
              printf(" ");
           }
           else if(j==y)
           {
                printf("%c", 11);
           }
           else if(j==x)
           {
                printf("%c\n",11);
           }

         }
         x-=1;
         y+=1;
         }
       }
    }
    printf("\n");
    printf("\n");
    printf("\n");
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
  printf("\n");
    printf("\n");
    printf("\n");
{
    int y = 20;
    int x = 30;
    int i;
    int j;
    for(i=0;i<41;i++)
    {
       if (i == 0){
        for (j=0;j<40;j++)
        {
         if (((j< y || j > x)) && (j!=39))
         {
          printf(" ");
         }
         else if ((j ==y) || ((j < x) &&(j > y)) || (j==x) )
         {
         printf("%c",11);
         }
         else if (j == 39)
         {
             printf("\n");
         }

        }
        y -=1;
        x +=1;

               }

        else if ((i > 0) && (i < 11))
        {
            for (j=0; j<41; j++)
            {
                if ((j > y) && (j< x) )
                {
                    printf(" ");
                }
                else if(j < y)
                {
                    printf(" ");
                }
                else if (j==y)
                {
                    printf("%c", 11);
                }
                else if (j==x)
                {
                    printf("%c\n",11);
                }
            }
             y -=1;
             x +=1;
        }
         else if ((i > 10) && (i < 21))
        {
            for (j=0; j<42; j++)
            {
                if ((j > y) && (j< x) )
                {
                    printf(" ");
                }
                else if(j < y)
                {
                    printf(" ");
                }
                else if (j==y)
                {
                    printf("%c", 11);
                }
                else if (j==x)
                {
                    printf("%c\n",11);
                }
            }

        }
         else if ((i > 20) && (i < 32))
        {
            for (j=0; j<42; j++)
            {
                if ((j > y) && (j< x) )
                {
                    printf(" ");
                }
                else if(j < y)
                {
                    printf(" ");
                }
                else if (j==y)
                {
                    printf("%c", 11);
                }
                else if (j==x)
                {
                    printf("%c\n",11);
                }
            }
             y +=1;
             x -=1;

        }
        if (i == 32){
        for (j=0;j<40;j++)
        {
         if (((j< y || j > x)) && (j!=39))
         {
          printf(" ");
         }
         else if ((j ==y) || ((j < x) &&(j > y)) || (j==x) )
         {
         printf("%c",11);
         }
         else if (j == 39)
         {
             printf("\n");
         }

        }
        y -=1;
        x +=1;
    }
}
}
    return 0;
}
