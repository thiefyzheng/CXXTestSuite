#include <stdio.h>

void ft_ultimate_div_mod(int *a, int *b);

int main()
{
	int f = 2308975;
	int c = 2397;
	int *a = &f;
	int *b = &c;
	ft_ultimate_div_mod(&f, &c);
	printf("Res is %d\n", *a);
	printf("Res is %d\n", *b);
}


