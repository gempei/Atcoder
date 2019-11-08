/*
#include <iostream>
#include <string.h>
using std::cin;
using std::cout;
using std::endl;
using std::string;
int main(void){
    string s;
    cin >> s;
    for (int i=0; i<3;i++)
        if(s[i]==s[i+1])
            cout << "Bad" << endl;
    return 0;
}
*/

#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::string;
int main(void){
    string s;
    cin >> s;
    bool isgood = true;
    if (s[0] == s[1]) isgood = false;
    if (s[1] == s[2]) isgood = false;
    if (s[2] == s[3]) isgood = false;
    if (isgood) {
        cout << "Good" << endl;
    } else {
        cout << "Bad" << endl;
    }
    return 0;
}
