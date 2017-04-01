#include <iostream>
#include <string>
using namespace std;

#include "example.h"

int main()
{
  Person a, b;
  a.name = "Calvin";
  b.name = "Hobbes";
  a.age = 30;
  b.age = 20;
  cout << a.name << ": " << a.age << endl;
  cout << b.name << ": " << b.age << endl;
  return 0;
}
