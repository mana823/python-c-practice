// ============================================================
// 第7章 第11题：输入英文名和姓，输出“姓, 名首字母.”
// 题目：
//   Enter a first and last name: Lloyd Fosdick
//   Fosdick, L.
// ============================================================

// * 你的代码（微调：去掉 while 里多余的 unsigned char 强转，其余保留）：
#include <stdio.h>

int main(void)
{
    int m;
    char n;

    printf("Enter a first and last name: ");
    scanf("%c", &n);

    for (; ;) {
        if (getchar() == ' ') {
            // * 微调：去掉 (unsigned char) 强转。
            // * getchar 返回 int，可能是 EOF（-1）。
            // * 如果强转成 unsigned char，EOF 会变成 255，
            // * 再和 EOF 比较就永远不成立，EOF 判断失效。
            // * 直接 m = getchar() 才能正确保留 EOF 信息。
            while ((m = getchar()) != '\n' && m != EOF)
                printf("%c", m);
            break;
        }
    }

    // ✅ 点号和换行已补上，正确。
    printf(", %c.\n", n);

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 逻辑正确：读首字母 → 跳过名 → 输出姓 → 输出 ", 首字母."。
// ✅ 点号和换行已补上。
// ✅ m 改成 int，能正确接收 getchar 的返回值。
// ⚠️ 唯一问题：while 里的 (unsigned char) 强转多余，且会破坏 EOF 判断。
//    getchar 返回 int，直接赋给 int m 即可，不要强转。
//    EOF 是 -1，强转 unsigned char 后变成 255，和 EOF 比较永远不成立。
//
// ? 补充（不是错误，题目保证输入名和姓）：
//    如果输入只有一个单词、没有空格，
//    for (; ;) 会一直读 getchar，直到 EOF 也停不下来，
//    因为没有判断 EOF。可以加一个兜底：
//      int ch;
//      while ((ch = getchar()) != ' ' && ch != '\n' && ch != EOF)
//          ;
//    但题目默认输入“名 姓”，有空格，当前写法能正确工作。
//
// ? C23 下 getchar、scanf、printf 规则与 C99/C11 一致，无特殊变化。
// ============================================================


// 只有toupper需要强转unsigned char(否则输入负数会发生向下越界)