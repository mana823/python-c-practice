// break语句不能直接退出嵌套循环，而我们又不想用goto语句，所以用return语句，这条语句将可以使程序终止并且返回操作系统

#include <stdio.h>

int main(void)
{
    int cmd;
    float balance = 0.0f, credit, debit;

    printf("****AXME checkbook-balancing proguam ***\n");
    printf("Commands: 0=clear, 1=cresit, 2=debit, ");
    printf("3=balance, 4=exit\n\n");
    for (; ;) {     // <-- 无限循环，需要自行退出
        printf("Enter command: ");
        scanf("%d", &cmd);
        switch (cmd) {
            case 0:
            balance = 0.0f; break;
            case 1:
            printf("Enter amount of credit: ");
            scanf("%f", &credit);
            balance += credit; break;
            case 2:
            printf("Enter amount of debit: ");
            scanf("%f", &debit);
            balance -= debit; break;
            case 3:
            printf("Currnet balance: $%.2f\n", balance); break;
            case 4:
            return 0;     // <-- return语句后面没有break语句。紧跟在return语句后的break语句永远不会执行
            default:
            printf("Commands: 0=clear, 1=cresit, 2=debit, ");
            printf("3=balance, 4=exit\n\n"); break;
        }

    }
    return 0;
}