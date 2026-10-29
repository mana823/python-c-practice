// 虽然 C 程序中 while 语句的出现次数远远多于 do 语句，但是后者对于至少需要执行一次的循环来说是非常方便的。
// 为了说明这一点，现在编写一个程序计算用户输入的整数的位数：

// Enter a nonnegative integer: 60
// The number has 2 digit(s).

// 方法是把输入的整数反复除以 10，直到结果变为 0 时停止，除法的次数就是所求的位数。
// 因为不知道到底需要多少次除法运算才能达到 0，所以很明显程序需要某种循环。但是应该用 while 语句还是 do 语句呢？do 语句显然更合适，因为每个整数（包括 0）都至少有一位数字。

// 下面是这个程序。

#include <stdio.h>

int main(void)
{
    int digits = 0, n;
    printf("Enter a nonnegative integer: ");
    scanf("%d", &n);

    
    do {
        n /= 10;
        digits++;
    } while (n > 0);
    printf("The number has %d digit(s).\n", digits);
    return 0;
}
// 因为存在一位数，刚除以就是0，或者数就直接填0，这是前面用while就不太好处理，像过第一关就有点难
