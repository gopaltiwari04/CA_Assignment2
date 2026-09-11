#include <iostream>
#include <gem5/m5ops.h>

int main()
{
    static int array[262144];
    volatile long long sum = 0;

    for (int i = 0; i < 262144; i++)
        array[i] = i;

    m5_work_begin(0, 0);

    for (int r = 0; r < 20; r++) {
        for (int i = 0; i < 262144; i++)
            sum += array[i];
    }

    m5_work_end(0, 0);

    std::cout << sum << std::endl;
    return 0;
}