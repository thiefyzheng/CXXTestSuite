#include <unistd.h>
#include <stdio.h>

void ft_ft(int *nbr);

int	main()
{
	int x = 10;
	ft_ft(&x);
	printf("\n%d", x);
	return 1;
}
