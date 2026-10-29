// 在下面这个用到 while 语句的示例中，我们编写了一个程序，对用户输入的整数数列进行求和计算。下面显示的是用户能看到的内容：

// This program sums a series of integers.
// Enter integers (0 to terminate): 8 23 71 5 0
// The sum is: 107

// 很明显，该程序需要一个循环来读入数（用 scanf 函数）并将其累加。
// 用 n 表示当前读入的数，而 sum 表示所有先前读入的数的总和，得到如下程序：

#include <stdio.h>

int main(void)
{
    int n, sum = 0;
    printf("This program sums a series of integers.\n");
    printf("Enter integers (0 to terminate): ");

    scanf("%d", &n);    // 这里写的多余的数被扔至缓冲区，下面循环时scanf自会提取，不遇到0循环不停止
    while (n != 0) {
        sum += n;
        scanf("%d", &n);
    }
    printf("The sum is: %d\n", sum);
    return 0;
}
