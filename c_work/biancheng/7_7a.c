// ============================================================
// 第7章 第7题：两个分数的加、减、乘、除
// 题目：
//   修改第3章的编程题6，使得用户可以对两个分数进行加、减、乘、除运算
//   （在两个分数之间输入 +、-、* 或 / 符号）。
// ============================================================

// * 你的代码（逻辑正确，保留原样，在原处标注）：
#include <stdio.h>

int main(void)
{
    int num1, denom1, num2, denom2, result_num, result_denom;
    char c;

    printf("Enter two fractions separated by sign: ");

    // ✅ scanf 格式串 "%d/%d %c %d/%d" 正确：
    //    格式串里的空格会匹配零个或多个空白字符，
    //    所以输入 "5/6 + 3/4"、"5/6+3/4"、"5/6  +  3/4" 都能正确读取。
    //    符号前后的空格可有可无，灵活。
    scanf("%d/%d %c %d/%d", &num1, &denom1, &c, &num2, &denom2);

    // ✅ 你的注释“switch/case 里没有字符，只有整数；
    //    'A' 是 65，char 提升成 int，比较层统一”正确。
    //    switch 控制表达式 c 会整型提升为 int，
    //    case 'A' 这类字符常量本身也是 int 类型。
    switch (c) {
        case '-':
            // ✅ 减法公式正确：
            //    a/b - c/d = (a*d - c*b) / (b*d)
            result_num = num1 * denom2 - num2 * denom1;
            result_denom = denom1 * denom2;
            break;

        case '+':
            // ✅ 加法公式正确：
            //    a/b + c/d = (a*d + c*b) / (b*d)
            result_num = num1 * denom2 + num2 * denom1;
            result_denom = denom1 * denom2;
            break;

        case '*':
            // ✅ 乘法公式正确：
            //    a/b * c/d = (a*c) / (b*d)
            result_num = num1 * num2;
            result_denom = denom1 * denom2;
            break;

        case '/':
            // ✅ 除法公式正确：
            //    a/b ÷ c/d = (a*d) / (b*c)
            result_num = num1 * denom2;
            result_denom = denom1 * num2;
            break;

        // ⚠️ 警告（可选）：没有 default 分支。
        //    如果用户输入的不是 +、-、*、/ 之一，
        //    result_num 和 result_denom 不会被赋值，
        //    printf 会输出未初始化的垃圾值。
        //    题目默认输入合法运算符，所以不加 default 也能过；
        //    但要更稳健，可以加：
        //      default:
        //          printf("Unknown operator: %c\n", c);
        //          return 1;
    }

    printf("The result is %d/%d\n", result_num, result_denom);

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 完全正确。
//   - scanf 格式串 "%d/%d %c %d/%d" 能正确读取带可选空格的输入。
//   - 加、减、乘、除四个公式全部正确。
//   - switch 控制表达式 char 会整型提升，case 字符常量是 int，比较正确。
//   - 每个 case 都有 break，不会贯穿。
//   - 输出格式与题目要求一致。
//
// ⚠️ 警告（可选，不是错误）：
//   1. 没有 default 分支，非法运算符会导致 result_* 未初始化。
//      题目默认输入合法，不改也能过；加 default 更稳健。
//   2. 除法分支没有检查 num2 是否为 0。
//      如果用户输入 5/6 / 0/1，result_denom = denom1 * 0 = 0，
//      输出 0/0，虽然不会崩溃（整数除零只在计算时发生），
//      但结果没有意义。可以在 case '/' 里检查：
//        if (num2 == 0) { printf("Division by zero\n"); return 1; }
//
// ? 补充：你的注释对 switch/整型提升的理解完全正确。
// ? C23 下 switch、字符常量、整型提升的规则与 C99/C11 一致，本题没有变化。
// ============================================================