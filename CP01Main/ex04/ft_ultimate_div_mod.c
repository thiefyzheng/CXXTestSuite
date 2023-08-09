#include <stdio.h>

void ft_ultimate_div_mod(int *a, int *b)
{
	int x = *a;
	int y = *b;
	int s;
	int r;
	s = x/y;
	r = x%y;
	*a = s;
	*b = r;
}


