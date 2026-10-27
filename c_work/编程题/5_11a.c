// ============================================================
// 第5章 第11题：两位数转英文单词
// 题目：
//   Enter a two-digit number: 45
//   You entered the number forty-five.
//
//   提示：把数分解为两个数字。
//   用一个 switch 显示第一位数字对应的单词（twenty、thirty 等），
//   用第二个 switch 显示第二位数字对应的单词。
//   不要忘记 11~19 需要特殊处理。
// ============================================================

// * 你的原始代码（微调：补全略写部分、修正句号位置）：
#include <stdio.h>

int main(void)
{
    int num1, num2;
    printf("Enter a two-digit number: ");
    scanf("%1d%1d", &num1, &num2);
    printf("You entered the number ");

    if (num1 == 1) {
        // ✅ 11~19 特殊处理，用 num2 区分 ten、eleven 等，正确。
        // ! 错误：每个单词后面都缺句号。
        //    45 走下面分支会输出 "-five." 带句号，
        //    但 10~19 走这里，输出 "ten"、"eleven" 不带句号，
        //    结果不一致。应统一加句号。
        switch (num2) {
            case 0: printf("ten.\n");      break;
            case 1: printf("eleven.\n");   break;
            case 2: printf("twelve.\n");   break;
            case 3: printf("thirteen.\n"); break;
            case 4: printf("fourteen.\n"); break;
            case 5: printf("fifteen.\n");  break;
            case 6: printf("sixteen.\n");  break;
            case 7: printf("seventeen.\n");break;
            case 8: printf("eighteen.\n"); break;
            case 9: printf("nineteen.\n"); break;
        }
    }
    else {
        // ✅ 十位：twenty、thirty 等，正确。
        switch (num1) {
            case 2:  printf("twenty"); break;
            case 3:  printf("thirty"); break;
            case 4:  printf("forty");  break;
            case 5:  printf("fifty");  break;
            case 6:  printf("sixty");  break;
            case 7:  printf("seventy");break;
            case 8:  printf("eighty"); break;
            case 9:  printf("ninety"); break;
        }

        // ✅ 个位：1~9 加连字符和单词，正确。
        // ! 错误：个位是 0 时（如 20、30），这里什么也不打印，
        //    结果只有 "twenty" 没有句号。
        //    应在 case 0 补一个句号。
        switch (num2) {
            case 0:  printf(".\n");     break;   // 20 → "twenty."
            case 1:  printf("-one.\n"); break;
            case 2:  printf("-two.\n"); break;
            case 3:  printf("-three.\n"); break;
            case 4:  printf("-four.\n"); break;
            case 5:  printf("-five.\n"); break;
            case 6:  printf("-six.\n");  break;
            case 7:  printf("-seven.\n");break;
            case 8:  printf("-eight.\n");break;
            case 9:  printf("-nine.\n"); break;
        }
    }
    return 0;
}

// * 验证：
//   输入 45 → num1=4, num2=5 → "forty" + "-five." → forty-five.  ✅
//   输入 20 → num1=2, num2=0 → "twenty" + "."     → twenty.      ✅
//   输入 10 → num1=1, num2=0 → "ten."             → ten.         ✅
//   输入 13 → num1=1, num2=3 → "thirteen."        → thirteen.    ✅
//   输入 11 → num1=1, num2=1 → "eleven."          → eleven.      ✅

// ============================================================
// 批改总结：
// ✅ 整体结构正确：11~19 特殊分支、十位 switch、个位 switch，思路清楚。
// ✅ scanf("%1d%1d") 逐位读取正确。
// ❌ 错误 1：11~19 分支每个单词后面缺句号。
//    45 会输出 "-five." 带句号，10~19 却不带，输出不一致。
//    修正：ten.、eleven.、twelve. ... nineteen. 都加句号。
// ❌ 错误 2：个位是 0 时（如 20、30），没有分支处理，
//    结果只有 "twenty" 没有句号。
//    修正：个位 switch 补 case 0: printf(".\n"); break;
// * 其他省略的部分按你的标注，不判错。
// ============================================================

// ============================================================
// * 你的笔记批改：
// · printf 宽度 = 最少占位（下限），不截断。✅ 正确。
//   例如 %5d 输出 42 时补 3 个空格，输出 123456 时不截断。
// · printf 精度 = 最少数字位数（下限），补零，不截断。
//   ✅ 对整数正确：%.3d 输出 42 为 042。
//   ? 对浮点数是“小数点后位数”：%.2f 输出 3.14159 为 3.14，
//     这一点和整数精度的含义不同，注意区分。
// · scanf 宽度 = 最多读几个字符（上限），会截断，剩下的留给下次读。
//   ✅ 正确。%1d 只读 1 位，45 读成 4 和 5 两次读，
//   或者 %2d 读 45 的 "45" 只取前 2 个字符。
// · scanf 没有精度。✅ 正确。scanf 不能写 %.2f 这种精度修饰。
// ============================================================