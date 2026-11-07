// 第7章 第6题：显示各类型的 sizeof 值
// 题目：
//   显示 sizeof(int)、sizeof(short)、sizeof(long)、
//   sizeof(float)、sizeof(double)、sizeof(long double) 的值。
// ============================================================

// * 你的代码（微调：最后一行补了 \n，逻辑没动）：
#include <stdio.h>

int main(void)
{
    // * 你的注释“sizeof 返回无符号整型，所以用 u，z 表示这个 size_t”
    // ✅ 正确。sizeof 返回 size_t，是无符号整型；
    //    %zu 中 z 是长度修饰符，表示 size_t，u 表示无符号十进制。

    printf("Int: %zu\n", sizeof(int));
    printf("Short: %zu\n", sizeof(short));
    printf("Long: %zu\n", sizeof(long));
    printf("Float: %zu\n", sizeof(float));
    printf("Double: %zu\n", sizeof(double));
    printf("Long Double: %zu\n", sizeof(long double));  // * 微调：补了 \n

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 完全正确。
//   - sizeof 返回 size_t，用 %zu 打印是标准写法。
//   - 六种类型都覆盖到了，没有遗漏。
//   - 你的注释对 size_t 和 %zu 的理解正确。
//
// ⚠️ 微调：最后一行 printf 末尾补了 \n，输出更整洁。
//
// ? 补充：
//   1. sizeof 是运算符，不是函数，所以 sizeof(int) 的括号
//      在类型名上是必需的，在变量上可以省略，如 sizeof x。
//   2. sizeof 的结果单位是字节（byte），不是位。
//      在常见平台上通常是：
//        int         4
//        short       2
//        long        4（32 位 Windows）或 8（64 位 Linux/macOS）
//        float       4
//        double      8
//        long double 12 或 16（依实现而定）
//   3. C 标准只保证各类型的最小范围，不保证固定字节数，
//      所以“在我的机器上”具体是多少，必须用 sizeof 实测。
//
// ? C23 相关：sizeof 和 %zu 在 C23 下没有变化，
//   规则与 C99/C11 一致。
// ============================================================