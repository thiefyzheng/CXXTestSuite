#include <unistd.h>
#include <stdio.h>

void ft_ultimate_ft(int *********nbr);

int main()
{
	int x = 42, *p1, **p2, ***p3, ****p4, *****p5, ******p6, *******p7, ********p8;
	p1 = &x; p2 = &p1; p3 = &p2; p4 = &p3; p5 = &p4; p6 = &p5; p7 = &p6; p8 = &p7;
	x = 10;
	ft_ultimate_ft(&p8);
	printf("%d",x);
	return 9;
}

