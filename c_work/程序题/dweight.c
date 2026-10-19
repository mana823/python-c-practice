/* Computes the dimendional weight of a 12" * 10"* 8"* box */
#include <stdio.h>
int main(void)
{
    int height, length, width, volume, weight;  //  <-- 同时声明多个变量，用逗号隔开

    height = 8, length = 12, width = 10, volume = height * length * width, weight = (volume + 165) / 166;
// 由于我们要除以166，但是我们的变量类型是int所以如果出现小数会漏掉小数部分，我们要取大，所以加一个165
    printf("Dimensions: %d*%d*%d\n",length, width, height); // 在C语言中双引号("")内的东西编辑器不会计算，全部打印
    printf("Volume (cubic inches): %d\n", volume);          // C语言printf不会默认换行，所以基本都在最后加上\n换行
    printf("Dimensional weight (pounds): %d\n",weight);
    return 0;
}




