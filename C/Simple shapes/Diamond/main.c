#include <stdio.h>
#include <stdlib.h>
/*Author is Yusef Quinlan */
void main()
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

