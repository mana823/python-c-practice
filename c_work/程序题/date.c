// ============================================================
// 第5章：用“法定”格式显示英文日期
// 题目：
//   英文合同和其他法律文档中经常使用下列日期格式：
//   Dated this _______ day of ______, 20__.
//   用户以月/日/年的格式输入日期，然后计算机显示出“法定”格式的日期：
//   Enter date (mm/dd/yy): 7/19/14
//   Dated this 19th day of July, 2014.
//
//   提示：用一个 switch 语句显示日期的后缀，
//         再用另一个 switch 语句显示出月份名。
// ============================================================

#include <stdio.h>

int main(void)
{
    int month, day, year;

    printf("Enter date (mm/dd/yy): ");
    scanf("%d/%d/%d", &month, &day, &year);  // * 正确：按 月/日/年 读取。

    printf("Dated this %d", day);             // * 正确：先输出 "Dated this " 和日号。

    // ! 原始错误：第一个 switch 的每个 case 组后面都缺少 break;
    // ! 后果：C 的 switch 会发生“贯穿”（fall through），
    // !       例如 day = 1 时，打印 "st" 后不会停，
    // !       会继续执行 case 2 打印 "nd"，case 3 打印 "rd"，
    // !       最后 default 打印 "th"，输出变成 "stndrdth"，完全错误。
    // * 你的注释：“和 if-else 语句一样，后面都没有冒号(:)”
    // ! 这句话不准确：switch 语句头 `switch (day)` 后面确实没有冒号，
    // ! 但每个 `case` 和 `default` 标签后面是有冒号的。
    // * 你的注释：“多个 printf 拼接，在 Python 则用 step=""”
    // ? 这里想说的应该是 Python 里可以用字符串拼接或 end=""，
    // ? 但 C 里就是连续调用 printf，输出会自然拼在一起，思路没问题。
    // * 正确写法：每个 case 组末尾加 break;
    switch (day) {
        case 1: case 21: case 31:
            printf("st");
            break;                  // * 必须加：否则会继续执行下面的 case。
        case 2: case 22:
            printf("nd");
            break;                  // * 必须加。
        case 3: case 23:
            printf("rd");
            break;                  // * 必须加。
        default:
            printf("th");           // * 你的注释：“别忘了最后的另外” ✅ 正确。
            break;                  // * default 后加不加 break 都可以，加上更统一。
    }

    printf(" day of ");             // * 正确：前后留空格，与后面月份拼接。
                                    // * 你的注释：“注意排版，在前后留一个空格” ✅ 正确。

    // ! 原始问题：月份 switch 只写到 7 月，8~12 月缺失。
    // ! 如果输入 8/1/14，月份名不会输出，结果变成 " day of , 2014."。
    // * 正确写法：补全 8~12 月。
    switch (month) {
        case 1:  printf("January");   break;  // * 你的注释：break 直接加在后面，清晰易懂 ✅
        case 2:  printf("February");  break;
        case 3:  printf("March");     break;
        case 4:  printf("April");     break;
        case 5:  printf("May");       break;
        case 6:  printf("June");      break;
        case 7:  printf("July");      break;
        // * 以下为补全的 8~12 月：
        case 8:  printf("August");    break;
        case 9:  printf("September"); break;
        case 10: printf("October");   break;
        case 11: printf("November");  break;
        case 12: printf("December");  break;
        // ? 可选：加 default 处理非法月份，例如 printf("Unknown"); break;
    }

    // * 正确：输出 ", 20" + 两位年份 + "." 并换行。
    // * 输入 7/19/14 时，year = 14，%.2d 输出 14，得到 ", 2014."。
    // * 你的注释：“%d 也没关系，与输入有关，换行符为下文排版做准备”
    // ? 这里用 %.2d 比 %d 更稳：如果年份输入 4，%.2d 会输出 04，
    // ? 得到 2004；用 %d 会输出 4，得到 204，不符合 20__ 的格式。
    // ? 所以保留 %.2d 或改成 %02d 更好。
    printf(", 20%.2d.\n", year);

    return 0;
}

// ============================================================
// 批改总结：
// ❌ 主要错误：第一个 switch 的 case 组后缺少 break;，会发生贯穿，
//    导致日期后缀输出成 "stndrdth" 之类。
// ❌ 次要问题：月份 switch 只写到 7 月，8~12 月缺失，需补全。
// ⚠️ 注释小瑕疵：“和 if-else 一样后面都没有冒号”不准确，
//    switch 头没有冒号，但 case/default 标签后面有冒号。
// ✅ 其他部分正确：scanf 格式、printf 拼接、月份 break、
//    最后 ", 20%.2d.\n" 的格式都符合题目要求。
//
// * 修正后输入 7/19/14，输出：
//   Dated this 19th day of July, 2014.
// ============================================================