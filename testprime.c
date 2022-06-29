#include <stdio.h>


int main(void)
{
	int i = 0;
	int j = 0;
	int num = 0;

	scanf("%d", &num);
	printf("we got this number = %d\n", num);
	for (i = 1; i <= num; i ++)
	{
		if (num % i == 0)
		{
			printf("%d\t", i);
			j++;
		}
	}
	if (j == 2)
		printf("prime\n");
	else
		printf("not prime\n");
	return (0);
}
