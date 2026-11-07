// ============================================================
// 第7章 第5题：Scrabble 单词值
// 题目：
//   Enter a word: pitfall
//   Scrabble value: 12
//
//   面值对应：
//     1  = A E I L N O R S T U
//     2  = D G
//     3  = B C M P
//     4  = F H V W Y
//     5  = K
//     8  = J X
//     10 = Q Z
//
//   允许大小写混合，提示用 toupper。
// ============================================================

// * 你的代码（已修正，保留原结构）：
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int n;
    int sum = 0;   // ! 修正：sum 必须初始化为 0。
                   // ! 原代码 int sum; 未初始化，sum += 1 是在垃圾值上累加，
                   // ! 输出结果完全不可预测。

    printf("Enter a word: ");   // * 微调：去掉冒号前多余空格，与题目示例一致。

    // * 循环条件正确：
    // *   n = getchar() 先把读到的字符存进 n，
    // *   再判断不是换行、也不是 EOF。
    // * n 声明为 int，能正确保存 EOF（通常 -1），这点做得好。
    while ((n = getchar()) != '\n' && n != EOF) {

        // * 正确：toupper 参数先转 unsigned char，
        // * 避免 char 为负值时传给 toupper 造成未定义行为。
        // * C23 下这条规则没有变化。
        switch (toupper((unsigned char)n)) {
            case 'A': case 'E': case 'I': case 'L': case 'N':
            case 'O': case 'R': case 'S': case 'T': case 'U':
                sum += 1; break;

            case 'D': case 'G':
                sum += 2; break;

            case 'B': case 'C': case 'M': case 'P':
                sum += 3; break;

            case 'F': case 'H': case 'V': case 'W': case 'Y':
                sum += 4; break;

            case 'K':
                sum += 5; break;

            case 'J': case 'X':
                sum += 8; break;

            case 'Q': case 'Z':
                sum += 10; break;

            default:
                // * 非字母字符（空格、标点等）直接跳过，不计分。
                // * 这里用 continue 和 break 效果一样，
                // * 因为 switch 后面没有其他代码。
                // * 用 break 语义更直观：跳出 switch，继续下一轮 while。
                break;
        }
    }

    // * 微调：末尾加 \n，输出更整洁。
    printf("Scrabble value: %d\n", sum);

    return 0;
}

// ============================================================
// 批改总结：
// ✅ switch 字母分组和面值完全正确。
// ✅ toupper 用法正确，先转 unsigned char 再传参，避免负值 UB。
// ✅ getchar 返回值用 int 保存，能正确处理 EOF。
// ✅ default 跳过非字母字符，符合题目要求。
//
// ❌ 严重错误：sum 没有初始化。
//    原代码 `int sum;` 后直接 `sum += 1;`，
//    是在未初始化的垃圾值上累加，结果不可预测。
//    必须写成 `int sum = 0;`。
//
// ⚠️ 微调：
//    1. printf("Enter a word: ") 去掉冒号前多余空格。
//    2. 输出末尾加 \n。
//    3. default 里的 continue 可以换成 break，
//       两者效果相同，break 语义更直观。
//
// ? C23 相关：本题没有涉及 C23 变化，
//   toupper、getchar、switch 的规则与 C99/C11 一致。
// ============================================================




/* ============================================================================
 * 【极客终极复盘：getchar / toupper / putchar 的接口契约】
 * ============================================================================
 *
 * 1. 逻辑本质（人类直觉 vs 机器物理）：
 *    - 人类直觉：getchar 读字符，toupper 转大写，putchar 写字符，都是“字符”。
 *    - 机器物理：三个函数各有独立契约，类型、值域、内部处理各不相同。
 *      char 不是它们之间的通用货币，int 才是。
 *
 * 2. 三个函数的契约（标准原文语义）：
 *    - getchar：返回 int，值域 0~255（读到的字节）或 EOF(-1)（结束/出错）。
 *      返回 int 是为了装下 257 个状态；char 只有 256 个，装不下。
 *    - toupper：参数是 int，但要求值必须是 unsigned char 能表示的值（0~255）
 *      或 EOF。传负数（如 signed char 提升出的 -61）是 UB，内部查表会越界。
 *    - putchar：参数是 int，内部取 unsigned char 部分写入 stdout；
 *      返回写入的字符值（提升为 int），出错返回 EOF。
 *      putchar(0x1070) 写出 0x70，返回 0x70，不等于传入值。
 *
 * 3. 认知碰撞（为什么“转 int”在应用层成立，在接口层不成立）：
 *    - 应用层：int n = getchar()，值域天然 0~255 或 EOF，传 toupper 天然合法。
 *      强转 (unsigned char)n 对 0~255 是空操作，对 EOF 反而把 -1 变 255，危险。
 *    - 接口层：toupper 不能假设调用者用 int 接 getchar。它可能被
 *      char c = ...; toupper(c); 调用，所以必须要求参数在 0~255 或 EOF。
 *    - 位模式 vs 作为 int 的值：0xC3 在 signed char 里提升为 -61，
 *      在 unsigned char 里提升为 195。位模式相同，传给 toupper 的值不同。
 *      toupper 看的是值，不是位模式。
 *
 * 4. 操作法则（三条铁律）：
 *    - 接 getchar 用 int，不要用 char。char 只有 256 个状态，EOF 和 0xFF 会互冒充。
 *    - 用 int n 接 getchar 后，toupper(n) 直接传，不需要强转；
 *      强转只在 n 是 char 且可能为负时才必要。
 *    - 输出字符用 putchar(c) 或 printf("%c", c)；输出整数值用 %d。
 *      字符 '2' 是 50，整数 2 是 2，别混。
 *
 * 5. 致命特例：
 *    - char n = getchar()：
 *        signed char 读到 0xFF → n == -1 → 被误判 EOF；
 *        unsigned char 读到 EOF → n == 255 → EOF 检测永远失效。
 *    - toupper((char)0xC3) 在 signed char 平台传 -61 → UB。
 *    - toupper((unsigned char)EOF) → 255，不是 EOF，语义被破坏。
 *    - putchar 成功写 0xFF 返回 255，不是 -1；EOF 才是 -1。
 *    - printf("%d", '2') 输出 50，不是 2；printf("%c", 2) 输出控制字符，不是 '2'。
 *
 * 6. [极客箴言]：
 *    - 三个函数三种契约，char 不是通用货币，int 才是中间层。
 *    - getchar 返回 int 是为了装 257 个状态；toupper 要 0~255 是为了查表安全；
 *      putchar 收 int 取 unsigned char 是为了字节语义干净。
 *    - 接口层不替应用层做假设，C 信任程序员；类型安全靠自己保证，不靠语言自动转。
 *
 * 7. [验证命令]：
 *    - printf("%d %d\n", EOF, (unsigned char)EOF);        // -1 255
 *    - printf("%d %d\n", (int)(char)0xC3, (int)(unsigned char)0xC3); // 依平台
 *    - printf("%d\n", putchar(0x1070));                    // 先写 'p'，再打 112
 *    - printf("%zu %zu\n", sizeof('2'), sizeof(char));     // C 里 4 1
 *    - gcc -Wall -Wextra -fsanitize=undefined 跑 toupper 传负值，看 UBSan 报错
 * ============================================================================
 */