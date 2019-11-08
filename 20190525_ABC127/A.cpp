#include <iostream>
using namespace std;

int main(){
  int age,tax;
  cin >> age >> tax;
  if(age>=13){
  	cout << tax << endl;
  }
  else if((6<=age) && (age<=12)){
  	cout << tax/2 << endl;
  }
  else{
  	cout << 0 << endl;
  }
}
