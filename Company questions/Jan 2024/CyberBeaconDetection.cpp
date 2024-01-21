
#include <iostream>


using namespace std;

bool isIlluminated(int x,int y,int xi,int yi,int R){
    return(((x-xi)*(x-xi) + (y-yi)*(y-yi))<=R*R);
} 

int main()
{
int x1=0,y1=0,x2=2,y2=2,xi=0,yi=0,R=3;
 int count =0;
 for(int x=x1;x<=x2;x++){
     for(int y=y1;y<=y2;y++){
         if(isIlluminated(x,y,xi,yi,R)){
             count++;
         }
     }
 }
 cout<<count;
}
