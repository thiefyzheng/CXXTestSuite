#include <unistd.h>
#include <stdio.h>

int ft_strlen(char *str)
{
	int count;
	count = 0;
	while(*str != 0)
	{
		str++;
		count++;
	}
	return count;
}
