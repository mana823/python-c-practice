// ============================================================
// 第5章 第3题：修改 broker.c
// 题目：
//   修改 5.2 节的 broker.c 程序，做出下面两种改变。
//   (a) 不再直接输入交易额，而是要求用户输入股票的数量和每股的价格。
//   (b) 增加语句用来计算经纪人竞争对手的佣金
//       （少于 2000 股时佣金为每股 33 美元 + 3 美分，
//         2000 股或更多股时佣金为每股 33 美元 + 2 美分）。
//   在显示原有经纪人佣金的同时，也显示出竞争对手的佣金。
// ============================================================

// ! 你的原始代码（整体注释，避免与下面可运行版本冲突）：
/*
#include <stdio.h>

int main(void)
{
    float number, value, commission;
    printf("Input number and value: ");
    scanf("%f%f", &number, &value);
    if (value * number < 2500) commission = 30 + 0.017f * value * number;
    if (value * number >= 2500 && value * number <6250) commission = 56 + 0.0066f * value * number;
    if (commission <= 39) commission =39;
    // 略
    printf("We have %.2f\n", commission);
    if (number < 2000) commission = (number * 0.03 + 33);  // 利用执行顺序一个变量多用
    if (number >= 2000) commission = (number * 0.02 + 33);
    printf("Other have %.2f", commission);  // 最后一行没必要换行
    return 0;
}
*/

// * 批改：
// ✅ 已修正的点：
//   - 交易额用 value * number，正确。
//   - 前两档佣金公式正确。
//   - 加了最低收费 39 美元的判断，方向正确。
//   - 对手佣金公式 number * 0.03 + 33 和 number * 0.02 + 33，正确。
//   - 对手佣金判断用 number < 2000，正确。
//   - printf 改成 %.2f，正确。
//   - 你的注释“利用执行顺序一个变量多用”✅ 可行：
//     原佣金已经 printf 过了，后面复用 commission 存对手佣金，不会影响已输出的结果。
//   - 最后一行不换行，题目没强制要求，可以不加 \n。✅
//
// ⚠️ 关键问题 1：最低收费判断的位置。
//   `if (commission <= 39) commission = 39;` 放在 `// 略` 之前，
//   只覆盖了前两档。如果补全后面的档位，这行必须放到所有档位判断之后。
//   否则交易额 >= 6250 时，commission 还没有被赋值，
//   这里判断的是未初始化的垃圾值，属于未定义行为。
//   完整程序中应写成：
//     if (trade < 2500) ...
//     else if (trade < 6250) ...
//     ... 补全所有档位 ...
//     if (commission < 39.00f) commission = 39.00f;
//
// ⚠️ 问题 2：最低收费条件写成 `commission <= 39`，
//   建议改成 `commission < 39.00f`，和 broker.c 原程序保持一致。
//   两者在本例结果相同（等于 39 时赋不赋值都是 39），
//   但 `< 39.00f` 更标准，常量也建议写 39.00f 保持 float 类型。
//
// ⚠️ 问题 3：佣金档位只写了前两档，后面用“略”代替。
//   实际程序需要补全 6250~20000、20000~50000、
//   50000~500000、>500000 四档，否则交易额 >= 6250 时 commission 未赋值。
//
// ⚠️ 问题 4：变量名 number、value 含义不直观。
//   number 是股数，value 是每股价格，
//   建议改成 shares 和 price，或至少在注释里写清楚。
//
// ? 问题 5：number（股数）用 float 可以算，但股数通常是整数，
//   用 int 更规范。本题用 float 不影响结果，但建议改 int。
//
// ? 问题 6：复用 commission 存对手佣金虽然可行，
//   但建议用单独变量 rival，代码更清晰，也不怕以后调整输出顺序。

// ------------------------------------------------------------
// * 正确思路：
//   1. 输入股数 shares 和每股价格 price。
//   2. 交易额 trade = shares * price。
//   3. 用 trade 走 broker.c 的级联 if-else，算原经纪人佣金。
//   4. 所有档位判断完之后，再统一做最低收费 39 美元判断。
//   5. 用 shares 判断对手佣金：
//        shares < 2000  → 33 + 0.03 * shares
//        shares >= 2000 → 33 + 0.02 * shares
//   6. 两个佣金分别输出。

// * 本文件唯一可运行的 main：

#include <stdio.h>

int main(void)
{
    int shares;              // * 股数，用 int 更规范。
    float price;             // * 每股价格。
    float trade;             // * 交易额 = 股数 × 每股价格。
    float commission;        // * 原经纪人佣金。
    float rival;             // * 竞争对手佣金。
                             // ? 用单独变量 rival 比复用 commission 更清晰。

    printf("Enter number of shares and price per share: ");
    scanf("%d%f", &shares, &price);

    // * 先算交易额，后面佣金都基于它。
    trade = shares * price;

    // * 原经纪人佣金：broker.c 的级联 if-else，基于交易额。
    if (trade < 2500.00f)
        commission = 30.00f + .017f * trade;
    else if (trade < 6250.00f)
        commission = 56.00f + .0066f * trade;
    else if (trade < 20000.00f)
        commission = 76.00f + .0034f * trade;
    else if (trade < 50000.00f)
        commission = 100.00f + .0022f * trade;
    else if (trade < 500000.00f)
        commission = 155.00f + .0011f * trade;
    else
        commission = 255.00f + .0009f * trade;

    // * 最低收费判断：必须放在所有档位判断之后，
    // * 此时 commission 一定已经被赋值。
    if (commission < 39.00f)
        commission = 39.00f;

    // * 竞争对手佣金：按“股数”判断，不是按交易额或每股价格。
    // * 少于 2000 股：33 + 0.03 × 股数
    // * 2000 股及以上：33 + 0.02 × 股数
    if (shares < 2000)
        rival = 33.00f + .03f * shares;
    else
        rival = 33.00f + .02f * shares;

    // * 两个佣金分别输出，保留两位小数。
    // * 最后一行不换行，符合你的要求，题目也没强制。
    printf("Original broker's commission: $%.2f\n", commission);
    printf("Rival broker's commission:    $%.2f", rival);

    return 0;
}

// * 验证：
//   输入 1000 股，每股 10 美元：
//     trade = 10000，落在 6250~20000 档，
//     原佣金 = 76 + 0.0034 * 10000 = 110.00
//     对手佣金：1000 < 2000，
//              33 + 0.03 * 1000 = 63.00
//   输出：
//     Original broker's commission: $110.00
//     Rival broker's commission:    $63.00
//
//   输入 3000 股，每股 10 美元：
//     trade = 30000，落在 20000~50000 档，
//     原佣金 = 100 + 0.0022 * 30000 = 166.00
//     对手佣金：3000 >= 2000，
//              33 + 0.02 * 3000 = 93.00
//   输出：
//     Original broker's commission: $166.00
//     Rival broker's commission:    $93.00
//
//   输入 100 股，每股 10 美元：
//     trade = 1000，原佣金 = 30 + 0.017 * 1000 = 47.00
//     对手佣金 = 33 + 0.03 * 100 = 36.00
//   输出：
//     Original broker's commission: $47.00
//     Rival broker's commission:    $36.00
//
//   输入 50 股，每股 10 美元：
//     trade = 500，原佣金 = 30 + 0.017 * 500 = 38.50
//     低于最低收费 39，最终原佣金 = 39.00
//     对手佣金 = 33 + 0.03 * 50 = 34.50
//   输出：
//     Original broker's commission: $39.00
//     Rival broker's commission:    $34.50

// ============================================================
// 批改总结：
// ✅ 交易额、前两档佣金、对手佣金公式、%.2f 输出都已改对。
// ✅ 最低收费判断方向正确。
// ⚠️ 最低收费判断位置不对：必须放在所有档位判断之后，
//    否则交易额 >= 6250 时 commission 未初始化，判断的是垃圾值。
// ⚠️ 佣金档位只写了前两档，需要补全后面四档。
// ⚠️ 最低收费条件建议写成 commission < 39.00f，常量写 39.00f。
// ? 建议股数用 int，变量名改成 shares/price，对手佣金用 rival 单独存。
// * 最后一行不换行，可以，题目没强制。
// ============================================================