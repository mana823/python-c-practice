// ============================================================
// 第6章 第4题：给 broker.c 添加循环，支持多笔交易
// 题目：
//   程序在用户输入的交易额为 0 时终止。
//   示例：
//   Enter value of trade: 30000
//   Commission: $166.00
//   Enter value of trade: 20000
//   Commission: $144.00
//   Enter value of trade: 0
// ============================================================

// * 你的代码（微调：去掉 Commission 前多余的 \n，整理缩进，逻辑没动）：
#include <stdio.h>

int main(void)
{
    float commission, value;

    do {
        printf("Enter value of trade: ");
        scanf("%f", &value);

        // * 输入 0 直接退出循环，不计算、不打印佣金。
        // * 你的注释分析正确：如果不 break，而是在下面判断加上 && value != 0，
        // * 那么 value=0 时会进入第一个 if（0 < 2500），算出 30 并打印，
        // * 不符合“输入 0 终止”的要求。
        if (value == 0)
            break;

        if (value < 2500.00f)
            commission = 30.00f + .017f * value;
        else if (value < 6250.00f)
            commission = 56.00f + .0066f * value;
        else if (value < 20000.00f)
            commission = 76.00f + .0034f * value;
        else if (value < 50000.00f)
            commission = 100.00f + .0022f * value;
        else if (value < 500000.00f)
            commission = 155.00f + .0011f * value;
        else
            commission = 255.00f + .0009f * value;

        if (commission < 39.00f)
            commission = 39.00f;

        // * 原代码这里写的是 printf("\nCommission: $%.2f\n", commission);
        // * 前面的 \n 会让第一笔佣金输出前多一个空行，
        // * 与题目示例不符，所以去掉。
        printf("Commission: $%.2f\n", commission);

    } while (value != 0);   // * 因为 value==0 已经 break，这个条件实际不会因 0 而退出，
                            // * 但保留它不影响正确性，语义也更清楚。

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 完全正确。
//   - do-while 循环支持多笔交易，输入 0 用 break 终止，符合题意。
//   - 你的注释分析正确：如果不 break，value=0 会进入第一个 if 算出 30，
//     必须提前终止，不能靠逐级 else if 排除。
//   - 佣金计算、最低收费 39 美元判断都正确。
//   - 以 30000 验证：落在 20000~50000 档，
//     100 + 0.0022*30000 = 166.00，正确。
// * 只做了微调：去掉 Commission 前多余的 \n，并整理了缩进，其余没动。
// ============================================================