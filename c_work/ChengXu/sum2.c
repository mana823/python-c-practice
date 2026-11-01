#include <stdio.h>

int main(void)
{
    long n, sum = 0;   // <-- 默认类型，编译器会转换成long int n

    printf("This program sums a series of integers.\n");
    printf("Enter integers (0 to terminate): ");

    scanf("%ld", &n);
    while (n != 0) {
        sum += n;
        scanf("%ld", &n);

    }
    printf("The sum is: %ld\n", sum);
    return 0;
}
// 可惜没用，在windows系统中long int 也是4字节