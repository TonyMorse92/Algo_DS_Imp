#include <iostream>

using namespace std;

int fib(int n)
{
	if (n <= 1) {
		return 1;
	}
	
	return fib(n - 1) + fib(n - 2);
}


int main()
{
	int n = 1;
	cout << fib(n) << "\n";

	n = 2;
	cout << fib(n) << "\n";

	n = 10;
	cout << fib(n) << "\n";

	return 0;
}
