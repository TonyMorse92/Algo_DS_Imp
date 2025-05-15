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
	for (int n = 0; n < 45; n++) {
	
		cout << "Index: " << n << "  fib(n): " << fib(n) << "\n";
	}

	return 0;
}
