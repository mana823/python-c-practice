// ============================================================
// 第2章 第8题：计算第一、二、三个月还贷后的剩余贷款金额
// 题目要求用户输入：贷款金额、利率、月还款额，保留两位小数输出。
// 提示：每月余额 = 上月余额 - 月还款 + 上月余额 × 月利率
//       月利率 = 年利率 / 100 / 12
// ============================================================

#include <stdio.h>  // * 正确：标准输入输出头文件。

// ! 原始错误点 1：用 #define 把贷款、利率、还款额写死了。
// ! 题目要求用户输入这三个值，应改用 scanf 读取，不是硬编码。
// #define LOAN 20000.00
// #define RATE 6.0
// #define PYTMENT 386.66

int main(void)
{
    double loan, rate, payment;      // * 正确：用 double 存储贷款、利率、月还款。
    double first, second, third;     // * 正确：存三个月后的余额。
    double monthly_rate;             // * 新增：月利率，避免每次重复计算。

    // * 正确：提示并读取贷款金额。
    printf("Enter amount of loan: ");
    scanf("%lf", &loan);

    // * 正确：提示并读取年利率。
    printf("Enter interest rate: ");
    scanf("%lf", &rate);

    // ! 原始错误点 2：第三个 printf 写成了 "Enter monthly payment:"，但读取的是利率。
    // ! 应为 "Enter interest rate:"，否则提示与实际输入不符。
    // * 修正如下：
    printf("Enter monthly payment: ");
    scanf("%lf", &payment);

    // ! 原始错误点 3：月利率计算错误。
    // ! 原代码用 RATE * 0.01 + 1，这是“年利率 + 1”，不是月利率。
    // ! 正确做法：年利率先转百分数，再除以 12。
    // * 正确：
    monthly_rate = rate / 100.0 / 12.0;  // * 月利率，例如 6.0 → 0.005

    // ! 原始错误点 4：余额计算公式错误。
    // ! 原代码：first = LOAN * (RATE * 0.01 + 1) - PYTMENT;
    // ! 这是按年利率算的，应该是按“月利率”加利息。
    // * 正确公式：本月余额 = 上月余额 - 月还款 + 上月余额 × 月利率
    // *           = 上月余额 × (1 + 月利率) - 月还款
    first  = loan   * (1 + monthly_rate) - payment;  // * 第一个月后余额
    second = first  * (1 + monthly_rate) - payment;  // * 第二个月后余额
    third  = second * (1 + monthly_rate) - payment;  // * 第三个月后余额

    printf("Balance remaining after first payment:  $%.2lf\n", first);   // * 正确：两位小数。
    printf("Balance remaining after second payment: $%.2lf\n", second);  // * 正确。
    printf("Balance remaining after third payment:  $%.2lf", third);     // * 正确：末尾不换行，题目示例如此。

    return 0;  // * 正确：程序正常结束。
}

// ============================================================
// 批改总结：
// ❌ 主要错误：
//   1. 用 #define 写死贷款/利率/还款额，题目要求用户输入，应改用 scanf。
//   2. 第三个 printf 提示写成了 "Enter monthly payment:"，应为 "Enter interest rate:"。
//   3. 月利率计算错误：用了年利率，应该 年利率 / 100 / 12。
//   4. 余额公式用错了利率。
// ✅ 正确部分：变量类型用 double、输出保留两位小数、末尾无换行都正确。
// * 修正后，输入 20000.00 / 6.0 / 386.66 输出应为：
//   $19713.34
//   $19425.25
//   $19135.71
// ============================================================