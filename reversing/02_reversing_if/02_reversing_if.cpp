#include <stdio.h>

int main() {
	int a, b, c;
	a = 1;
	b = 2;

	printf("before if statement\n");

	if (a > b)
		c = 1;
	else
		c = 0;

	printf("after if statement\n");
	
	return 0;
}