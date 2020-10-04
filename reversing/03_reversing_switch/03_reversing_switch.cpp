#include <stdio.h>

int main() {
	int n;
	printf("Input number: ");
	scanf("%d", &n);
	printf("before switch statement\n");

	switch (n) {
	case 0: printf("[zero]"); break;
	case 1: printf("[one]"); break;
	case 2: printf("[two]"); break;
	case 3: printf("[three]"); break;
	case 4: printf("[four]"); break;
	default: printf("[error]"); break;
	}

	printf("after switch statement\n");

	return 0;
}