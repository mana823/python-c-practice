// ============================================================
// 第5章 第9题：输入两个日期，显示哪一个更早
// 题目：
//   Enter first date (mm/dd/yy): 3/6/08
//   Enter second date (mm/dd/yy): 5/17/07
//   5/17/07 is earlier than 3/6/08
// ============================================================

// ! 你的原始代码（整体注释，避免与下面可运行版本冲突）：
/*
#include <stdio.h>

int main(void)
{
    int day1, day2, month1, month2, year1, year2;
    printf("Enter first date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month1, &day1, &year1);
    printf("Enter second date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month2, &day2, &year2);
    if (year2 < year1) printf("%d/%d/%.2d is earlier than %d/%d/%.2d",month2, day2, year2, month1, day1, year1);
    if (year1 == year2) {
        if (month2 < month1) printf("%d/%d/%.2d is earlier than %d/%d/%.2d",month2, day2, year2, month1, day1, year1);
        else if (month2 == month1) {
            if (day2 > day1) printf("%d/%d/%.2d is earlier than %d/%d/%.2d", month1, day1, year1, month2, day2, year2);
            else printf("%d/%d/%.2d is earlier than %d/%d/%.2d",month2, day2, year2, month1, day1, year1);
        }
        else if (month2 > month1) printf("%d/%d/%.2d is earlier than %d/%d/%.2d", month1, day1, year1, month2, day2, year2);
    }
    if (year2 > year1) printf("%d/%d/%.2d is earlier than %d/%d/%.2d", month1, day1, year1, month2, day2, year2);
    return 0;
}
*/

// * 批改：
// ✅ 核心比较逻辑正确：
//   - year2 < year1 → 第二个日期更早。
//   - year1 == year2 时，先比月，再比日。
//   - month2 == month1 时，day2 > day1 → 第一个日期更早；
//     day2 <= day1 → 第二个日期更早（你标注了“暂不考虑 day 相等”）。
//   - year2 > year1 → 第一个日期更早。
//
// ✅ 拼写已修正：第二个提示 "Enter second date" 正确。
// ✅ 括号已修正：main 函数在 return 0; 后正常闭合，没有多余的 }。
// ✅ 年份用 %.2d 输出，符合 yy 格式：输入 08 输出 08，输入 7 输出 07。
//
// ⚠️ 警告（不是错误）：day 相等时，你的 else 会输出“第二个日期更早”。
//    你标注了“暂不考虑 day 相等”，所以这里不判错，只提醒：
//    如果两个日期完全相同，应输出“两个日期相同”之类的信息，
//    而不是强行说第二个更早。
//
// ⚠️ 警告：三个独立 if 判断 year。
//    你的注释“因为前置条件 year 之间比大小只能有一个成立，
//    所以用多个连续 if 可以”✅ 逻辑上正确：
//    year2 < year1、year1 == year2、year2 > year1 三者互斥，
//    最多只有一个成立，不会互相覆盖。
//    但按你自己的笔记“安全铁律”，业务语义是“多选一”时，
//    更推荐 if-else if 链，语义更明确，也抗未来变更。
//    本题用独立 if 能跑对，但不是最稳妥的写法。
//
// ⚠️ 警告：每次 printf 都重复写 "is earlier than" 和一整串日期，
//    可以先把“较早日期”和“较晚日期”存到变量里，
//    最后只 printf 一次，减少重复，也不容易写错参数顺序。
//
// ⚠️ 警告：内层 month2 == month1 分支里，
//    你用的是 if (day2 > day1) ... else ...，
//    day2 == day1 时会走 else，输出“第二个日期更早”。
//    你标注了“暂不考虑 day 相等”，所以不判错；
//    完整程序应单独处理相等情况。

// ------------------------------------------------------------
// * 正确思路：
//   1. 读入两个日期。
//   2. 比较 year；year 相同再比 month；month 相同再比 day。
//   3. 把较早的日期存到 earlier 系列变量，
//      较晚的日期存到 later 系列变量。
//   4. 最后统一 printf 一次。
//   5. 用 if-else if 链，保证“多选一”语义明确。
//
// * 本文件唯一可运行的 main：

#include <stdio.h>

int main(void)
{
    int month1, day1, year1;
    int month2, day2, year2;
    int emonth, eday, eyear;   // * earlier：较早的日期
    int lmonth, lday, lyear;   // * later：较晚的日期

    printf("Enter first date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month1, &day1, &year1);

    printf("Enter second date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month2, &day2, &year2);

    // * 判断哪个日期更早，把结果存到 earlier / later。
    // * 用 if-else if 链，语义是“多选一”，命中一个就跳过后面。
    if (year1 < year2) {
        emonth = month1; eday = day1; eyear = year1;
        lmonth = month2; lday = day2; lyear = year2;
    } else if (year1 > year2) {
        emonth = month2; eday = day2; eyear = year2;
        lmonth = month1; lday = day1; lyear = year1;
    } else {
        // * 年份相同，比较月份。
        if (month1 < month2) {
            emonth = month1; eday = day1; eyear = year1;
            lmonth = month2; lday = day2; lyear = year2;
        } else if (month1 > month2) {
            emonth = month2; eday = day2; eyear = year2;
            lmonth = month1; lday = day1; lyear = year1;
        } else {
            // * 年月都相同，比较日。
            if (day1 < day2) {
                emonth = month1; eday = day1; eyear = year1;
                lmonth = month2; lday = day2; lyear = year2;
            } else if (day1 > day2) {
                emonth = month2; eday = day2; eyear = year2;
                lmonth = month1; lday = day1; lyear = year1;
            } else {
                // * 两个日期完全相同。
                printf("The two dates are the same.\n");
                return 0;
            }
        }
    }

    // * 统一输出一次，减少重复。
    printf("%d/%d/%.2d is earlier than %d/%d/%.2d\n",
           emonth, eday, eyear, lmonth, lday, lyear);

    return 0;
}

// * 验证：
//   输入 3/6/08 和 5/17/07：
//     year1 = 8，year2 = 7，year1 > year2，
//     所以第二个日期更早，输出 5/17/07 is earlier than 3/6/08  ✅
//
//   输入 3/6/08 和 3/6/08：
//     年月日都相同，输出 The two dates are the same.  ✅
//
//   输入 12/31/99 和 1/1/00：
//     year1 = 99，year2 = 0，year1 > year2，
//     第二个日期更早，输出 1/1/00 is earlier than 12/31/99  ✅

// ============================================================
// * 你的笔记批改：
// 【极客复盘：独立 if 与 if-else if 的最终抉择】
// 1. 逻辑等价性：条件互斥时，多个独立 if 与 if-else if
//    最终执行的分支相同。✅ 正确。
// 2. 底层执行差异：
//    - if-else if：命中一个分支后，分支体末尾有一条 jmp
//      直接跳过后续所有 cmp，后面的条件根本不进指令流。✅ 正确。
//    - 多个 if：每个 if 独立生成 cmp + 条件跳转，
//      前一个命中不影响后一个继续求值，
//      所有条件都会被摆上执行路径。✅ 正确。
// 3. [安全铁律]：
//    - 永远不要过度依赖“当前条件互斥”这一前提，
//      需求会变，互斥会破。✅ 正确。
//    - 业务语义是“多选一” → 无脑 if-else if / switch，
//      语义明确、抗变更、不会因为未来加条件而静默多执行一个分支。
//      ✅ 正确。
//    - 业务语义是“逐个筛掉不合格的” → 连续 if + return（卫语句），
//      这是另一套用法，别和“多选一”混为一谈。✅ 正确。
// 4. [性能备注]：
//    - 性能是顺带的，不是主要理由。现代 CPU 分支预测下，
//      连续 if 全命中预测时代价没想象中大。
//      选 if-else if 是为了语义和抗变更，不是抠那几条 cmp。
//    ✅ 正确。
// ? 补充：本题你的三个独立 if 判断 year，正好符合“条件互斥”这个前提，
// ? 所以能跑对。但按你自己的安全铁律，多选一场景优先 if-else if 链，
// ? 上面给的完整代码就是按这个原则改写的。
// ============================================================

// ============================================================
// 批改总结：
// ✅ 核心比较逻辑正确：先比年，再比月，再比日。
// ✅ 拼写、括号、年份格式都已修正。
// ⚠️ 警告：day 相等时会输出“第二个日期更早”，
//    你标注了暂不考虑，不判错；完整程序应处理相等情况。
// ⚠️ 警告：三个独立 if 判断 year，逻辑上互斥能跑对，
//    但按你的安全铁律，多选一场景更推荐 if-else if 链。
// ⚠️ 警告：printf 重复写了多次，建议先存 earlier/later，
//    最后统一输出一次。
// * 你的笔记【独立 if 与 if-else if 的最终抉择】内容正确，
//   底层执行差异、安全铁律、性能备注都说得对。
// ============================================================