// 现在编写一个程序来显示平方表。首先程序提示用户输入一个数 n，然后显示出 n 行的输出，每行包含一个 1~n 的数及其平方值。

// This program prints a table of squares.
// Enter number of entries in table: 5
// 1        1
// 2        4
// 3        9
// 4       16
// 5       25

// 把期望的平方数个数存储在变量 n 中。程序需要用一个循环来重复显示数 i 和它的平方值，循环从 i 等于 1 开始。
// 如果 i 小于或等于 n，那么循环将反复进行。需要保证的是每次执行循环时对 i 的值加 1。

// 可以使用 while 语句编写循环。（坦白地说，现在没有更多其他的选择，因为 while 语句是目前为止我们唯一掌握的循环类型。）下面是完整的程序。

#include <stdio.h>

int main(void)
{
    int i, n;

    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);

    i = 1;
    while (i <= n) {
        printf("%10d%10d\n", i, i * i);
        i++;
    }
    return 0;
}