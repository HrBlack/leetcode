# temp是异或，相加各位的值，不算进位
# num2是carry进位，通过与运算来做，并需要做左移
# 然后再将两者“相加”
class Solution {
public:
    int Add(int num1, int num2)
    {
        while (num2 != 0){
            int temp = num1 ^ num2;
            num2 = (num1 & num2) << 1;
            num1 = temp;
        }
        return num1;
    }
};
