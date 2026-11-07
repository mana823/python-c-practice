// ============================================================
// 第7章 第3题：修改 sum2.c，对 double 型值组成的数列求和
// 题目：
//   修改 7.1 节的程序 sum2.c，对 double 型值组成的数列求和。
// ============================================================

// * 你的代码（逻辑正确，保留原样）：
#include <stdio.h>

int main(void)
{
    double n, sum = 0;

    // ⚠️ 警告：提示语还写着 integers，但现在输入的是浮点数。
    //    建议改成 "This program sums a series of numbers." 和
    //    "Enter numbers (0 to terminate): "，与 double 输入一致。
    printf("This program sums a series of integers.\n");
    printf("Enter integers (0 to terminate): ");

    scanf("%lf", &n);      // ✅ double 配 %lf，正确。

    while (n != 0) {       // ✅ 你的注释“0 会发生常规算术转换为浮点”正确：
                           //    n 是 double，比较时 0 转成 0.0，判断没问题。
        sum += n;          // ✅ 累加
        scanf("%lf", &n);  // ✅ 继续读下一个 double
    }

    // ✅ %.2lf 保留两位小数，double 配 %lf 或 %f 都可以。
    printf("The sum is: %.2lf\n", sum);

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 逻辑完全正确。
//   - 类型从 int 改为 double，符合题目要求。
//   - scanf 用 %lf，printf 用 %lf，格式符与 double 匹配。
//   - while (n != 0) 遇到 0 终止，正确。
//   - sum 初始化为 0，累加逻辑正确。
//   - 你的注释“0 会发生常规算术转换为浮点”正确。
//
// ⚠️ 警告（不是错误）：提示语还写着 integers，
//    现在输入的是浮点数，建议改成 numbers 或 floating-point numbers，
//    让提示和实际输入类型一致。
//
// ? 补充：printf 中 %lf 和 %f 对 double 是等价的，
//    用 %.2lf 或 %.2f 都行，保持 %lf 也没问题。
// ============================================================