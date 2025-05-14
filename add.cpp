#include <iostream>
using namespace std;

int add(int x, int y)
{
	return x+y;
}

int main()
{
	int x = 15, y = 10;
	cout << "Sum of 15 and 10 is " << add(x, y) << "\n";
	return 0;
}
