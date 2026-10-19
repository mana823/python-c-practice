/* 根据用户提供的输入，计算一个箱子的体积重量*/

#include <stdio.h>

int main(void)
{
    int height, length, width, volume,  weight;
    printf("Enter height of box: ");
    scanf("%d", &height);   // <-- scanf不负责换行，不过输入数字后你要回车，终端就执行换行了(并非scanf执行)
    printf("Enter length of box: ");
    scanf("%d", &length);   // <-- 和Python中input一样，都是强行暂停目前代码运行，等用户输入
// 只有一种情况：输入流里已经有现成的数据了。
// 比如，你在前面输入了 12 34，但 scanf 第一次只读了 12，那个 34 还残留在输入缓冲区里。
// 这时候你执行第二个 scanf，它一看缓冲区里有 34，直接拿走，就不等你了

// scanf 里的 \n 不是“换行”，而是“跳过空白字符直到遇到非空白字符”。它会导致程序“假死”或“吃错数据”。
    printf("Enter width of box: ");
    scanf("%d", &width);
    volume = height * length * width;
    weight = (volume + 165) / 166;

    printf("Volume (cubic inches) : %d\n", volume);
    printf("Dimensional weight (pounds): %d\n", weight);
    return 0;
}
// 存在一个问题:如果用户输入的不是数值，程序会出现问题。3.2节会详细讨论。
// scanf 只管读，不管提示。想给用户提示，必须自己先写一句 printf。 这就像 Python 里把 input 拆成两半：一半是 print("提示")，一半是 input()。