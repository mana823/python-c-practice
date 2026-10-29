// ============================================================
// 2.4节 第3、4题
// ============================================================

// * 第3题题目：
// 通过下列方法缩写程序 dweight.c：
// (1) 用初始化器替换对变量 height、length 和 width 的赋值；
// (2) 去掉变量 weight，在最后的 printf 语句中计算 (volume + 165) / 166。

// ! 你的原代码（第3题）：
// #include <stdio.h>
// #define HEIGHT 8
// #define LENGTH 12
// #define WIDTH 10
// int main(void)
// {
//     int height, length, width, volume = HEIGHT * LENGTH * WIDTH;
//     printf("Dimensions: %d*%d*%d\n",length, width, height);
//     printf("Volume (cubic inches): %d\n", volume);
//     printf("Dimensional weight (pounds): %d\n",(volume + 165) / 166);
//     return 0;
// }

// ! 批改：
// ! 1. 题目要求用初始化器替换赋值，应写成 int height = 8, length = 12, width = 10;
// !    你却用了宏定义 #define，这不符合题目要求。
// ! 2. 变量 height, length, width 没有初始化，但在 printf 中使用了它们，值不确定。
// ! 3. 格式字符串建议用 %dx%dx%d，原题通常是这个格式。
// * 正确写法（因同一文件只能有一个 main，此处注释掉）：
/*
#include <stdio.h>
int main(void) {
    int height = 8, length = 12, width = 10;  // * 用初始化器替换赋值
    int volume = height * length * width;     // * 计算体积
    printf("Dimensions: %dx%dx%d\n", length, width, height);
    printf("Volume (cubic inches): %d\n", volume);
    printf("Dimensional weight (pounds): %d\n", (volume + 165) / 166);  // * 去掉 weight，直接计算
    return 0;
}
*/

// ============================================================
// * 第4题题目：
// 编写一个程序来声明几个 int 型和 float 型变量，不对这些变量进行初始化，然后显示它们的值。
// 这些值是否有规律？（通常情况下没有。）

#include <stdio.h>  // * 预处理指令，包含 printf 声明

int main(void)      // * 主函数，当前文件中唯一可运行的 main
{
    int a, b;       // * 声明 int 变量，未初始化
    float c, d;     // * 声明 float 变量，未初始化

    // * 你的原代码只打印了 a 和 c，建议把 b 和 d 也打印出来，更符合“几个变量”的要求。
    printf("a = %d\n", a);  // * 打印未初始化的 int 变量。值不确定，可能是 0，也可能是其他值。
    printf("b = %d\n", b);  // * 补充打印 b
    printf("c = %f\n", c);  // * 打印未初始化的 float 变量。%f 默认输出 6 位小数。
    printf("d = %f\n", d);  // * 补充打印 d

    return 0;
}

// * 批改：
// (b) 你的观察基本正确：
//   - int 用 %d 输出整数，没有小数点，你看到输出 0。
//   - float 用 %f 输出浮点数，默认 6 位小数，你看到输出 0.000000。
// ? 但要注意：未初始化的局部变量值是不确定的（undefined behavior），
// ? 打印它们可能得到任何值，不一定是 0。你看到 0 只是当前编译器的巧合。
// ? 题目问“这些值是否有规律？” 答案：通常没有规律，不应依赖。
// * 补充：最好使用 %f 时加上 \n，方便查看。你的原代码第二个 printf 没有换行。

// ============================================================
// 总结：
// 第3题：❌ 错误，已给出正确写法（注释中）。
// 第4题：✅ 基本正确，已补充打印 b 和 d，并说明未初始化变量的不确定性。
// ============================================================