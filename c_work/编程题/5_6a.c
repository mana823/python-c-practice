// ============================================================
// 第5章 第6题：检测 UPC 有效性
// 题目：
//   修改 4.1 节的 upc.c 程序，使其可以检测 UPC 的有效性。
//   在用户输入 UPC 后，程序将显示 VALID 或 NOT VALID。
// ============================================================

// * 批改：
// ✅ 本版逻辑已完全正确。
//   - 第二组 scanf 末尾多余的逗号已删除。
//   - 校验位 a = 9 - (total - 1) % 10 公式正确。
//   - 判断条件已改成 a == last，正确。
//   - first_sum、second_sum 奇偶位分配正确。
//   - total = 3 * first_sum + second_sum 正确。
//   - 你的注释“%1d 宽度对于整数是字符限制”✅ 正确。
//
// ⚠️ 可选清理 1：最后一行
//     printf("Check digit: %d\n", 9 - (total - 1) % 10);
//   题目只要求输出 VALID / NOT VALID，这一行是额外的。
//   如果保留，建议直接复用 a，避免重复计算：
//     printf("Check digit: %d\n", a);
//
// ⚠️ 可选清理 2：VALID / NOT VALID 后没有换行。
//   题目没强制，但加上 \n 输出更清晰。
//
// ? 变量名 a 含义不直观，建议改成 check，可读性更好。
//   不改也不影响正确性。

// ------------------------------------------------------------
// * 本文件唯一可运行的 main（保留你的结构，做最小清理）：

#include <stdio.h>

int main(void)
{
    int d, i1, i2, i3, i4, i5, j1, j2, j3, j4, j5;
    int first_sum, second_sum, total, last, check;

    printf("Enter the first (single) digit: ");
    scanf("%1d", &d);    // * %1d：宽度限制为 1，逐位读取。

    printf("Enter first group of five digits: ");
    scanf("%1d%1d%1d%1d%1d", &i1, &i2, &i3, &i4, &i5);

    printf("Enter second group of five digits: ");
    scanf("%1d%1d%1d%1d%1d", &j1, &j2, &j3, &j4, &j5);

    printf("Enter the last (single) digit: ");
    scanf("%1d", &last);

    // * 奇数位：d、i2、i4、j1、j3、j5
    first_sum = d + i2 + i4 + j1 + j3 + j5;
    // * 偶数位：i1、i3、i5、j2、j4
    second_sum = i1 + i3 + i5 + j2 + j4;
    // * 加权和
    total = 3 * first_sum + second_sum;

    // * 计算校验位
    check = 9 - (total - 1) % 10;

    // * 用计算出的 check 与输入的 last 比较。
    if (check == last)
        printf("VALID\n");
    else
        printf("NOT VALID\n");

    // ? 题目没要求输出 Check digit，这里不输出。
    // ? 如果保留，直接写 printf("Check digit: %d\n", check); 即可。

    return 0;
}

// * 验证（完整 UPC 013800151735）：
//   d = 0，第一组 13800，第二组 15173，last = 5
//   first_sum  = 0 + 3 + 0 + 1 + 1 + 3 = 8
//   second_sum = 1 + 8 + 0 + 5 + 7 = 21
//   total      = 3 * 8 + 21 = 45
//   check      = 9 - (45 - 1) % 10 = 5
//   check == last（5 == 5）→ VALID ✅
//
//   若 last 改成 6：
//   check = 5，last = 6，5 != 6 → NOT VALID ✅

// ============================================================
// 批改总结：
// ✅ 本版逻辑完全正确，a == last 判断已改对。
// ⚠️ 可选清理：最后一行 Check digit 题目没要求，可删；
//    保留的话直接用 a/check，避免重复计算。
// ⚠️ 可选：VALID / NOT VALID 后加 \n。
// ? 可选：变量名 a 改成 check 更直观。
// * 核心逻辑已无错误。
// ============================================================