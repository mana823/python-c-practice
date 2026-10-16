/*华氏温度转换为摄氏温度*/
// 下面的程序提示用户输入一个华氏度，然后输出一个对应的摄氏温度。此程序输出格式如下:
//      Enter Fahtrenheit temperature: 212
//      Celsius equivalent: 100.0
// 这段程序允许温度值不是整数，这也是摄氏度温度显示100.0而不是100的原因。

/* 将华氏温度转化为摄氏温度 */
#include <stdio.h>

#define FREEZING_PT 32.0f   // <-- 预处理一般写在main前面   (华氏度32度=摄氏度0度，所以先减32度)
#define SCALE_FACTOR (5.0f / 9.0f)  // <-- 华氏度与摄氏度缩比是5:9
int main(void)
{
    float fahrenheit, celsius;   // <-- 声明变量

    printf("Enter Fahrenheit temperature: ");
    scanf("%f", &fahrenheit);

    celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;  // <-- 可以看成celdius = (fahrenheit - 32.0f) * (5.0f / 9.0f)
// 是(5.0f / 9.0f)而不是(5 / 9)，因为两个整数相除，那么C语言会对结果向下取舍入。则值为0，不是我们想要的
    printf("Celsius equivalent: %1.f\n", celsius);  // <-- "1.f"中"1"是保留一位小数,"f"是类型
    return 0;
}


