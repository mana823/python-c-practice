// ============================================================
// 5.3节 第10、11题
// ============================================================

// ------------------------------------------------------------
// * 第10题：
// 下面的代码片段的输出结果是什么？（假设 i 是整型变量。）
// i = 1;
// switch (i % 3) {
// case 0: printf("zero");
// case 1: printf("one");
// case 2: printf("two");
// }
// ------------------------------------------------------------

// * 你的原答：
// 10.答: onetwo

// * 批改：✅ 正确。
// * 过程：
//   i = 1，i % 3 = 1。
//   switch 匹配 case 1，打印 "one"。
//   但 case 1 后面没有 break，发生贯穿（fall through），
//   继续执行 case 2，打印 "two"。
//   case 2 后面也没有 break，但后面没有其他 case 了，
//   所以 switch 结束。
//   最终输出：onetwo。
// ? 补充：如果 case 1 后面有 break，就只会输出 "one"。
// ?       本题故意省略 break，考查的就是 switch 的贯穿行为。

// ------------------------------------------------------------
// * 第11题：
// 表 5-5 给出了美国佐治亚州的电话区号，以及每个区号所对应地区最大的城市。
//
// 区号   主要城市
// 229    Albany
// 404    Atlanta
// 470    Atlanta
// 478    Macon
// 678    Atlanta
// 706    Columbus
// 762    Columbus
// 770    Atlanta
// 912    Savannah
//
// 编写一个 switch 语句，其控制表达式是变量 area_code。
// 如果 area_code 的值在表中，switch 语句打印出相应的城市名；
// 否则 switch 语句显示消息 "Area code not recognized"。
// 使用 5.3 节讨论的方法，使 switch 语句尽可能地简单。
// ------------------------------------------------------------

// ! 你的原始代码（整体注释，避免与下面的完整版 main 冲突）：
/*
#include <stdio.h>

int main(void)
{
    int area_code;
    printf("Input: ");
    scanf("%3d", &area_code);

    switch (area_code) {       // * 你的注释：switch 是控制语句，所以后面只能跟一个语句
                               // * （可以是复合语句），但 case 是标签，后面不用花括号，
                               // * 也能接多个语句。
                               // ✅ 方向正确。更严谨地说：
                               // * switch 后面必须跟一个语句（通常是复合语句 { ... }）；
                               // * case 和 default 是标签，不是语句，标签后面可以接多条语句，
                               // * 不加花括号时，这些语句的作用域是整个 switch 块。
    case 229: printf("Albany");  break;
    case 404: printf("Atlanta"); break;
    case 470: printf("Atlanta"); break;
    // 略
    default: printf("Area code not recognized");  // * 你的注释：default 也是标签 ✅ 正确。
    }
}
*/

// * 对你原代码的批改：
// ✅ 已写的 229、404、470 三个 case 都正确。
// ✅ default 也正确。
// ❌ 代码不完整：缺少 478、678、706、762、770、912 这些区号。
// ❌ 没有按 5.3 节的方法简化：多个区号对应同一城市时，
//    应该把多个 case 标签叠在一起，共用一个 printf + break。
//    你写的是：
//      case 404: printf("Atlanta"); break;
//      case 470: printf("Atlanta"); break;
//    这样虽然结果对，但没有用到“多个 case 共用一段代码”的简化技巧。
// ⚠️ default 后面建议加 break;，虽然 switch 末尾的 default 不加也能正常结束，
//    但加上更统一、更安全。
// ⚠️ 缺少 return 0;，C99 起 main 可以省略，但显式写出更规范。

// * 5.3 节的简化方法：
//   把对应同一城市的多个 case 标签连续写在一起，
//   只在最后一条 case 后面写 printf 和 break。
//   这样代码更短、更清晰。

// * 完整正确写法（本文件唯一可运行的 main）：

#include <stdio.h>

int main(void)
{
    int area_code;

    printf("Input: ");
    scanf("%3d", &area_code);

    switch (area_code) {
        case 229:
            printf("Albany");
            break;

        // * 404、470、678、770 都对应 Atlanta，叠在一起共用一个分支。
        case 404:
        case 470:
        case 678:
        case 770:
            printf("Atlanta");
            break;

        case 478:
            printf("Macon");
            break;

        // * 706、762 都对应 Columbus，叠在一起共用一个分支。
        case 706:
        case 762:
            printf("Columbus");
            break;

        case 912:
            printf("Savannah");
            break;

        default:
            printf("Area code not recognized");
            break;  // * default 后加 break 更统一，虽然末尾不加也能结束。
    }

    return 0;
}

// * 以 area_code = 770 验证：
// *   匹配 case 770，贯穿到下面共用的 printf("Atlanta")，输出 Atlanta。
// * 以 area_code = 762 验证：
// *   匹配 case 762，贯穿到下面共用的 printf("Columbus")，输出 Columbus。
// * 以 area_code = 123 验证：
// *   不匹配任何 case，执行 default，输出 Area code not recognized。

// ============================================================
// 最终批改汇总：
// 第10题：✅ 正确。i % 3 = 1，匹配 case 1 打印 one，
//         没有 break，贯穿到 case 2 打印 two，输出 onetwo。
// 第11题：
// ✅ 已写的 229、404、470 和 default 正确。
// ❌ 缺少 478、678、706、762、770、912。
// ❌ 没有使用“多个 case 叠在一起共用一段代码”的简化方法。
// ? default 后建议加 break;，末尾建议加 return 0;。
// * 完整代码见上，核心是：
//   case 404: case 470: case 678: case 770: printf("Atlanta"); break;
//   case 706: case 762: printf("Columbus"); break;
// ============================================================