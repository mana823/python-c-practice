// 为了显示 scanf 函数的模式匹配能力，考虑读入由用户输入的分数。
// 分数通常的形式为分子/分母。scanf 函数允许读入整个分数，而不用将分子和分母视为两个整数分别读入。下面的分数相加程序体现了这一方法。


/* 把两个分数相加 */

#include <stdio.h>

int main(void)
{
    int num1, denom1, num2, denom2, result_num, result_denom;    // 由于我们用的是通分，用整数完全够用

    printf("Enter first fraction: ");
    scanf("%d/%d",&num1, &denom1);      // <-- 直接在输入时就把/给写了，这样的话拿值需要想清楚这样运算，运算在内部，输入在外部显示

    printf("Enter second fraction: ");
    scanf("%d/%d", &num2, &denom2);

    result_num = num1 * denom2 + num2 * denom1;    // <-- 通分后的分子总和
    result_denom = denom1 * denom2;                // <-- 通分后的分母值
    printf("The sum is %d/%d\n", result_num, result_denom);    // <-- 注意，结果并没有化为最简分数
    return 0;
}

