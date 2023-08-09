#include <stdio.h>

void ft_swap(int *a, int *b);

int main()
{
	int x = 10;
	int y = 90;
	printf("X is %d\n", x);
	printf("Y is %d\n", y);


	ft_swap(&x, &y);
	
	printf("X is %d\n", x);

	printf("Y is %d\n", y);

	return 0;
}


