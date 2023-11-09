#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s = "Hello world";
    string ans = "";
    for (auto it : s)
    {
        ans += (it ^ 0);
    }
    cout << "Original Text:" << s << endl;
    cout << "Result:" << ans;
}
