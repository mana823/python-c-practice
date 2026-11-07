// ============================================================
// 第7章 第8题：12 小时制输入 + 航班选择
// 题目：
//   修改第5章的编程题8，要求用户输入12小时制的时间。
//   输入格式为 时:分 后跟 A、P、AM 或 PM（大小写均可）。
//   数值时间和 AM/PM 之间允许有空白，但不强制。
//   示例：1:15p、1:15pm、1:15 P、1:15 PM、1:15 p、1:15 pm
//   可以假定输入格式合法，不需要错误判定。
// ============================================================

// ! 你的原始代码（整体注释，避免与下面可运行版本冲突）：
/*
#include <stdio.h>
#include <ctype.h>
int main(void)
{
    int hour, minute;
    int t, n;
    printf("Enter a 12-hour time: ");
    scanf("%d:%d %c", &hour, &minute, &n);
    if (toupper(n) == 'A') t = hour * 60 + minute;
    if (toupper(n) == 'P') t = (12 + hour) * 60 + minute;
    if (t <= 480)
        printf("Closest departure time is 8:00 a.m., arriving at 10:16 a.m.\n");
    else if (t <= 583)
        printf("Closest departure time is 9:43 a.m., arriving at 11:52 a.m.\n");
    else if (t <= 679)
        printf("Closest departure time is 11:19 a.m., arriving at 1:31 p.m.\n");
    else if (t <= 767)
        printf("Closest departure time is 12:47 p.m., arriving at 3:00 p.m.\n");
    else if (t <= 840)
        printf("Closest departure time is 2:00 p.m., arriving at 4:08 p.m.\n");
    else if (t <= 945)
        printf("Closest departure time is 3:45 p.m., arriving at 5:55 p.m.\n");
    else if (t <= 1140)
        printf("Closest departure time is 7:00 p.m., arriving at 9:20 p.m.\n");
    else
        printf("Closest departure time is 9:45 p.m., arriving at 11:58 p.m.\n");

    return 0;
}
*/

// * 批改：
//
// ✅ 航班选择部分完全正确：
//   把时间换算成分钟，按 <= 分档，找第一个 >= 的航班，与第5章第8题一致。
//
// ✅ AM/PM 只用第一个字符判断，正确：
//   题目允许 A、P、AM、PM，第一个字符 A/P 已经足够区分，
//   toupper 统一转大写也正确。
//
// ❌ 严重逻辑错误 1：12 点没有特殊处理。
//   12 小时制里 12 点很特殊：
//     12:xx AM 是午夜，对应 24 小时制的 0:xx；
//     12:xx PM 是中午，对应 24 小时制的 12:xx。
//   你的代码：
//     12:00 AM → t = 12*60 + 0 = 720（12:00）  ❌ 应为 0:00
//     12:00 PM → t = (12+12)*60 = 1440（24:00） ❌ 应为 12:00
//   这会导致 12:xx AM 被当成中午，12:xx PM 被当成第二天 0:xx，
//   航班选择完全错误。
//
//   正确规则：
//     AM：hour == 12 时，24 小时制 hour = 0；否则不变。
//     PM：hour == 12 时，24 小时制 hour = 12；否则 hour += 12。
//
// ❌ 类型错配 2：scanf 用 %c 读 int 变量。
//   %c 要求 char*，传 int* 是未定义行为。
//   你的注释“用 int 无妨”不准确：
//   实际运行时 %c 只写 1 个字节，剩余字节保留原值，
//   看起来“能跑”，但标准上不保证，属于 UB。
//   应改用 char n;，或者用 int 但读取方式改成 %c 配合临时 char。
//
// ⚠️ 警告 3：toupper 参数建议转 unsigned char。
//   toupper 要求参数是 unsigned char 的值或 EOF。
//   如果 n 是 char 且可能为负值（扩展字符集），直接传是 UB。
//   虽然题目保证输入是 A/P/AM/PM，不会有负值，
//   但写成 toupper((unsigned char)n) 更严谨，C23 下这条规则没有变化。
//
// ⚠️ 警告 4：t 没有初始化。
//   如果 n 既不是 A 也不是 P（题目保证不会），t 未初始化。
//   题目说“可以假定输入合法”，所以可以接受；
//   如果想更稳，可以给 t 一个初值，或者用 else 兜底。
//
// ------------------------------------------------------------
// * 修正版（本文件唯一可运行的 main）：
// ------------------------------------------------------------

#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int hour, minute;
    int t;
    char n;   // * 改用 char 接收 %c，避免类型错配
    char period;

    printf("Enter a 12-hour time: ");
    scanf("%d:%d %c", &hour, &minute, &n);

    // * 统一转大写，判断是 AM 还是 PM。
    // * 题目保证输入是 A/P/AM/PM，第一个字符足以区分。
    period = toupper((unsigned char)n);

    if (period == 'A') {
        // * AM：12:xx AM 是午夜，对应 0:xx；
        // *     其他 1~11 点保持不变。
        if (hour == 12)
            hour = 0;
        t = hour * 60 + minute;
    } else {
        // * PM：12:xx PM 是中午，保持 12；
        // *     其他 1~11 点加 12。
        if (hour != 12)
            hour += 12;
        t = hour * 60 + minute;
    }

    // * 航班选择：与第5章第8题一致。
    if (t <= 480)
        printf("Closest departure time is 8:00 a.m., arriving at 10:16 a.m.\n");
    else if (t <= 583)
        printf("Closest departure time is 9:43 a.m., arriving at 11:52 a.m.\n");
    else if (t <= 679)
        printf("Closest departure time is 11:19 a.m., arriving at 1:31 p.m.\n");
    else if (t <= 767)
        printf("Closest departure time is 12:47 p.m., arriving at 3:00 p.m.\n");
    else if (t <= 840)
        printf("Closest departure time is 2:00 p.m., arriving at 4:08 p.m.\n");
    else if (t <= 945)
        printf("Closest departure time is 3:45 p.m., arriving at 5:55 p.m.\n");
    else if (t <= 1140)
        printf("Closest departure time is 7:00 p.m., arriving at 9:20 p.m.\n");
    else
        printf("Closest departure time is 9:45 p.m., arriving at 11:58 p.m.\n");

    return 0;
}

// * 验证：
//   12:00 AM → hour 改为 0，t = 0       → 8:00 a.m. 那班  ✅
//   12:30 AM → hour 改为 0，t = 30      → 8:00 a.m. 那班  ✅
//   1:00 AM  → hour 不变，t = 60        → 8:00 a.m. 那班  ✅
//   11:59 AM → hour 不变，t = 719       → 11:19 a.m. 那班 ✅
//   12:00 PM → hour 保持 12，t = 720    → 12:47 p.m. 那班 ✅
//   12:30 PM → hour 保持 12，t = 750    → 12:47 p.m. 那班 ✅
//   1:00 PM  → hour 加 12，t = 780      → 12:47 p.m. 那班 ✅
//   11:59 PM → hour 加 12，t = 1439     → 9:45 p.m. 那班  ✅

// ============================================================
// 批改总结：
// ✅ 航班选择部分完全正确。
// ✅ AM/PM 用第一个字符判断，正确。
// ❌ 严重逻辑错误：12:xx AM / 12:xx PM 没有特殊处理，
//    导致 12 点被算成 0 点或 24 点，航班选择错误。
// ❌ 类型错配：%c 要求 char*，传 int* 是 UB，
//    应改用 char n;。
// ⚠️ toupper 参数建议转 unsigned char，C23 下规则不变。
// ⚠️ t 未初始化，题目保证输入合法，可接受；
//    想更稳健可加 else 兜底。
// * 正确规则：
//    AM 且 hour == 12 → hour = 0；
//    PM 且 hour != 12 → hour += 12；
//    其余保持不变。
// ============================================================



/* ============================================================================
 * 【极客终极复盘：%c 写 int 的物理假象与类型严格匹配的铁律】
 * ============================================================================
 *
 * 1. 逻辑本质（人类直觉 vs 机器物理）：
 *    - 人类直觉：%c 读字符，int 能存字符。既然全局 int 默认是 0，我让 %c 读进 int
 *      的地址，读个 'A' 进去，输出 65，能跑就行。
 *    - 机器物理：%c 要求 char*，你给 int*，这叫“格式符与实参类型不匹配”，是标准 UB。
 *      所谓“能跑”，纯粹是【全局变量零初始化】+【小端序部分写入】在物理上救了命。
 *
 * 2. 底层物理真相（假象的成因）：
 *    - 全局 int 在 .bss 段，启动时被清零（00 00 00 00）。
 *    - 小端序下，%c 往 int 的最低地址写 1 字节。输入 'A'(0x41)，内存变成 00 00 00 41。
 *    - 读出来刚好是 65。换到大端序，写成 41 00 00 00，读出来是 1090519040。
 *    - 如果换局部变量（栈上），剩余 3 字节是垃圾，读出来是天文数字。
 *
 * 3. 认知碰撞（为什么其他招数救不了）：
 *    - 用强制格式符 %hhd 读 int*：依然是 UB。scanf 的铁律是“地址类型严格匹配”，
 *      %hhd 要求 signed char*，你给 int*，编译器直接报警告，底层依然只写 1 字节。
 *    - 用强制指针转换 (char*)&int_var：这叫欺骗编译器。编译过了，但只写了 1 字节，
 *      剩余字节没管，后续按 int 读依然是脏数据（除非你是全 0 的全局变量）。
 *    - 核心差异：printf 容忍提升（float 提 double），但 scanf 是死板的“看图纸硬写内存”，
 *      图纸画多大（%c 是 1 字节），它就写多大，绝不会帮你补齐 int 的 4 字节。
 *
 * 4. 操作法则（规规矩矩的拆解动作）：
 *    - 遇到类型不匹配，开新变量接，再赋值/转换。别在 scanf 里耍花招。
 *    - 正确姿势：char ch; scanf("%c", &ch); int x = (unsigned char)ch;
 *    - 终极姿势：int ch = getchar();  (getchar 返回值天然是 int，包含 0~255 和 EOF)
 *    - 忘掉“格式符强转”和“指针强转”，C 语言里“类型不对”就是“物理尺寸不对”。
 *
 * 5. 致命特例（跨平台炸裂）：
 *    - 小端 x86 上，全局变量 %c 写 int 可能得到正确结果。
 *    - 大端设备、网络字节序处理、非零初始化的内存，这个写法会瞬间暴露原形，输出乱码。
 *
 * 6. [极客箴言]：
 *    - 物理能跑，不代表标准合法。靠 .bss 段清零和小端序兜底的代码，不叫技术，叫赌命。
 *    - 不要试图用格式符去强行解释内存，也不要轻易用指针强转去欺骗编译器。
 *    - 规规矩矩声明对应类型的变量，用合法的转换规则赋值，才是跨平台、抗优化的真代码。
 *
 * 7. [验证命令]：
 *    - 局部变量验证：int x; scanf("%c", &x); printf("%d\n", x); （观察输出垃圾值）
 *    - 严格编译：gcc -Wall -Wextra test.c  （看编译器如何警告 %c 配 int*）
 *    - 强制骗编译器：scanf("%c", (char*)&x); （看是否消除警告，但依然可能读到垃圾）
 * ============================================================================
 */