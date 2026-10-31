#include <stdio.h>

int main(void)
{
    int i, n;
    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
        printf("%10d%10d\n", i, i * i);
    printf("%d", i);       // <-- 因为最后还得进行一次i++，但是i虽然最后大于n但是我们只看执行次数
    return 0;
}