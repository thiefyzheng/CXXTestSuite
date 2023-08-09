#include <unistd.h>
#include <stdio.h>

void ft_swap(int *a, int *b)
{
	int atemp;
	int btemp;
	atemp = *a;
	btemp = *b;
	*a = btemp;
	*b = atemp;
	}


