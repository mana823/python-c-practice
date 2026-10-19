// ============================================================
// 第3章 第3题：分解 ISBN
// 题目：
// Enter ISBN: 978-0-393-97950-3
// GS1 prefix: 978
// Group identifier: 0
// Publisher code: 393
// Item number: 97950
// Check digit: 3
// ============================================================

#include <stdio.h>  // * 正确：标准输入输出头文件。

int main(void)
{
    int isbn, prefix, identifier, code, number, digit;
    // * 正确：各段都用 int 存储。ISBN 分段后每段数值都不大，int 足够。
    // ? 小建议：变量 isbn 声明了但没使用，可以删掉，避免无用变量。
    // ? 若保留，可写 (void)isbn; 或直接删除。

    printf("Enter ISBN: ");  // * 正确：提示输入。
    // * 正确：scanf 用 "-" 分隔五个 %d。
    // * 输入 978-0-393-97950-3 时：
    // *   %d 读 978，遇到 '-' 停止；格式串 '-' 匹配输入 '-'；
    // *   依此类推，五段都能正确读取。
    // ? 可选：检查返回值，如 if (scanf("%d-%d-%d-%d-%d", ...) != 5) { ... }
    // ?       练习中可不写。
    scanf("%d-%d-%d-%d-%d", &prefix, &identifier, &code, &number, &digit);

    printf("GS1 prefix: %d\n", prefix);            // * 正确：输出 GS1 前缀。
    printf("Group identifier: %d\n", identifier);  // * 正确：输出组标识。
    printf("Publisher code: %d\n", code);          // * 正确：输出出版商编号。
    printf("Item number: %d\n", number);           // * 正确：输出产品编号。
    printf("Check digit: %d", digit);              // * 正确：输出校验数字。
                                                   // * 末尾不换行，题目示例也没要求，没问题。

    return 0;  // * 正确：程序正常结束。
}

// ============================================================
// 批改总结：
// ✅ 完全正确。分段读取、输出格式均符合题目要求。
// ? 唯一小建议：删除未使用的 isbn 变量；可选检查 scanf 返回值。
// ============================================================