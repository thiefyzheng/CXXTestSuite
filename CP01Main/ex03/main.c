#include <stdio.h>

void ft_div_mod(int a, int b, int *div, int *mod);

int main()
{
	int x = 43453450;
	int y = 639;
	int a;
	int b;
	int *result = &a;
	int *remainder = &b;
	ft_div_mod(x, y, &a, &b);
	printf("%d\n",a);

	printf("%d\n",b);

	return 1;
}


