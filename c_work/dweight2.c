/* 根据用户提供的输入，计算一个箱子的体积重量*/

#include <stdio.h>

int main(void)
{
    int height, length, width, volume,  weight;
    printf("Enter height of box: ");
    scanf("%d\n", &height);   // <-- 因为要打印的语句，这个提示词要和scanf结合一起，更加清晰易懂。之后再换行。
    printf("Enter length of box: ");
    scanf("%d\n", &length);
    printf("Enter width of box: ");
    scanf("%d\n", &width);
    volume = height * length * width;
    weight = (volume + 165) / 166;

    printf("Volume (cubic inches) : %d\n", volume);
    printf("Dimensional weight (pounds): %d\n", weight);
    return 0;
}
// 存在一个问题:如果用户输入的不是数值，程序会出现问题。3.2节会详细讨论。
// scanf 只管读，不管提示。想给用户提示，必须自己先写一句 printf。 这就像 Python 里把 input 拆成两半：一半是 print("提示")，一半是 input()。