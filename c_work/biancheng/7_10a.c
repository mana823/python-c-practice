// ============================================================
// 第7章 第10题：统计句子中元音字母的个数
// 题目：
//   Enter a sentence: And that's the way it is.
//   Your sentence contains 6 vowels.
// ============================================================

// * 你的代码（微调：toupper 参数转 unsigned char，输出补 \n）：
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int n, sum = 0;

    printf("Enter a sentence: ");

    // * 循环条件正确：
    // *   n = getchar() 先把读到的字符存进 n，
    // *   再判断不是换行、也不是 EOF。
    // * n 声明为 int，能正确保存 EOF，这点做得好。
    while ((n = getchar()) != '\n' && n != EOF) {

        // * 微调：toupper 参数转 unsigned char。
        // * toupper 要求参数是 unsigned char 的值或 EOF。
        // * 如果 n 是负值（扩展字符集），直接传是未定义行为。
        // * 本题输入基本是 ASCII，实际不会出问题，
        // * 但写成 (unsigned char)n 更严谨。
        n = toupper((unsigned char)n);

        if (n == 'A' || n == 'E' || n == 'I' || n == 'O' || n == 'U')
            sum++;
    }

    // * 微调：末尾补 \n，输出更整洁。
    printf("Your sentence contains %d vowels.\n", sum);

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 完全正确。
//   - n 用 int，能正确保存 getchar 的返回值和 EOF。
//   - sum 初始化为 0，正确。
//   - while 条件同时判断换行和 EOF，正确。
//   - toupper 统一转大写，大小写元音都能统计。
//   - A/E/I/O/U 五个元音判断完整。
//   - 输出格式与题目示例一致。
//
// ⚠️ 警告（微调，不是错误）：
//   toupper 参数建议转 unsigned char，
//   避免 char 为负值时传给 toupper 造成未定义行为。
//   本题 ASCII 输入不会触发，但写成 (unsigned char)n 更严谨。
//
// ⚠️ 警告（微调）：输出末尾建议加 \n。
//
// ? 补充：
//   元音判断可以写得更紧凑：
//     if (n == 'A' || n == 'E' || n == 'I' || n == 'O' || n == 'U')
//   也可以先转成小写再判断，效果一样。
//   你现在的写法清晰直观，不需要改。
//
// ? C23 相关：toupper、getchar 的规则与 C99/C11 一致，
//   本题没有 C23 特有的变化。
// ============================================================