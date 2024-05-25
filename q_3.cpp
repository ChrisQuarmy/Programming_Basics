#include <iostream>
using namespace std;
int main()
{
    int x;
    int L_D=0;
    int n,i;
    int target;

    cout<<"enter number of digit: ";
    cin>>x;
    cout<<"target"<<endl;
    cin>>target;

    for (int i=1; i<=x; i++)
    {
    cout<<"entetr n: ";
    cin>>n;
      if (target==n)
        {
        L_D=i;
        }
    }
    cout<<"the last position is "<<L_D;
    return 0;
}