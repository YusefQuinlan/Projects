#include <stdio.h>
#include <stdlib.h>

/* Author is Yusef Quinlan */
void main()
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
