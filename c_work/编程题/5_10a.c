// ============================================================
// 第5章 第10题：用 switch 把数字成绩转换为字母等级
// 题目：
//   Enter numerical grade: 84
//   Letter grade: B
//
//   等级规则：
//     A：90~100
//     B：80~89
//     C：70~79
//     D：60~69
//     F：0~59
//   高于 100 或低于 0 显示出错消息。
//
//   提示：把成绩拆分成 2 个数字，
//         然后使用 switch 语句判定十位上的数字。
// ============================================================

// * 你的原始代码（微调：只给 printf 补了 \n，逻辑结构没动）：
#include <stdio.h>

int main(void)
{
    int num;
    printf("Enter numerical grade: ");
    scanf("%d", &num);
    if (num > 100 || num < 0) { printf("Error!\n"); return 0; }     // 卫语句,如果不用的话排除错误选项还得if筛选里面嵌套

    switch (num / 10) {
        // ✅ num / 10 取十位数字，符合题目提示。
        case 9: case 10: printf("Letter grade: A\n"); break;   // 90~100 → 9 或 10 → A
        case 8: printf("Letter grade: B\n"); break;            // 80~89 → 8 → B
        case 7: printf("Letter grade: C\n"); break;            // 70~79 → 7 → C
        case 6: printf("Letter grade: D\n"); break;            // 60~69 → 6 → D
        default: printf("Letter grade: F\n"); break;           // 0~59 → 十位 0~5 → F
    }

    return 0;
}

// ============================================================
// 批改总结：
// ✅ 完全正确。
//   - 卫语句先排除非法成绩，避免了主逻辑嵌套。
//   - num / 10 取十位数字，符合题目提示。
//   - 90~100 → 9 或 10 → A，case 9 和 case 10 共用，正确。
//   - 80~89 → 8 → B，70~79 → 7 → C，60~69 → 6 → D，正确。
//   - 0~59 → 十位 0~5，走 default → F，正确。
//   - 每个 case 后都有 break，不会贯穿。
//   - 因为卫语句已排除 <0 和 >100，default 只会接住 0~59，结果正确。
// * 只做了微调：给 printf 补了 \n，其余没动。
// ============================================================