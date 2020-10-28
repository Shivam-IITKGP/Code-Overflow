// C++ program to find the given number is even or odd
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    
    // Input a number
    
    cout << "Enter an integer: ";
    cin >> n;
   
    // Checking if the number is even or odd 
    
    (n % 2 == 0) ? cout << n << " is even." :  cout << n << " is odd.";
    
    return 0;
}
