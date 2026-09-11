#include <iostream>
#include <gem5/m5ops.h>

int main()
{
    static double a[32768], b[32768];
    for (int i = 0; i < 32768; i++) { a[i] = i * 0.5; b[i] = i * 1.5; }
    volatile double sum = 0.0;

    m5_work_begin(0, 0);
    for (int r = 0; r < 20; r++)
        for (int i = 0; i < 32768; i++)
            sum += a[i] * b[i] + 1.0;
    m5_work_end(0, 0);

    std::cout << sum << std::endl;
    return 0;
}
