#include <iostream>

using namespace std;

int fib(int n)
{
	if (n <= 1) {
		return 1;
	}
	
	return fib(n - 1) + fib(n - 2);
}

int* it_fib(int n)
{
	int* fib_list = new int[n];

	fib_list[0] = 1;
	fib_list[1] = 1;

	for (int i = 2; i < n; i++) {
		fib_list[i] = fib_list[i-1] + fib_list[i-2];	
	} 

	return fib_list;	
}

int main()
{
/*	for (int n = 0; n < 45; n++) {
	
		cout << "Index: " << n << "  fib(n): " << fib(n) << "\n";
	}
*/

	int n = 45;

	int* list = it_fib(n);

	for(int i = 0; i < n; i++) {
		cout << "Index: " << i << "  fib(n): " << *(list + i) << "\n";
	}

	delete [] list;	
	return 0;
}
