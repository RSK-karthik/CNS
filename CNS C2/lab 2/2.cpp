#include<bits/stdc++.h>
using namespace std;
int main(){
string s="Hello world";
string ans1="";
string ans2="";
string ans3="";
for(auto it : s){
    ans1+=(it&127);
    
}
for(auto it : s){
    ans2+=(it|127);

}
for(auto it : s){
    ans3+=(it^127);

}
cout<<"AND "<<ans1<<endl;
cout<<"OR "<<ans2<<endl;
cout<<"XOR "<<ans3<<endl;

}
