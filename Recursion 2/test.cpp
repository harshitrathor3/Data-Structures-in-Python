#include<bits/stdc++.h>
using namespace std;
int main(){int t;
cin>>t;
while(t--){
    
int n,cm1=0,c1=0;
cin>>n;
int a[n];
for(int i=0;i<n;i++){
cin>>a[i];
if(a[i]==1)
c1++;
else cm1++;
}
if(c1==0 )
cout<<"yes"<<endl;
else if(n%3==0){
    if(c1/2==cm1)
cout<<"yes"<<endl;
else cout<<"no"<<endl;
}
else if(n%3==1){
    int x=cm1*2;
    if(x+1==c1)
cout<<"yes"<<endl;
else if(x-2==c1)
cout<<"yes"<<endl;
else cout<<"no"<<endl;
}
else { int x=cm1*2;
    if(x-1==c1)
cout<<"yes"<<endl;
else if(x+2==c1)
cout<<"yes"<<endl;
else cout<<"no"<<endl;
}
}
}