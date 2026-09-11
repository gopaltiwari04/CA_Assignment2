#include <iostream>
#include <gem5/m5ops.h>

int main()
{
    volatile double a = 1.1, b = 1.2, c = 1.3, d = 1.4;

    m5_work_begin(0, 0);

    for (long long i = 0; i < 1000000; i++) {
        a = a * 1.000001 + 0.1;
        b = b * 1.000002 + 0.2;
        c = c * 1.000003 + 0.3;
        d = d * 1.000004 + 0.4;
    }

    m5_work_end(0, 0);

    std::cout << a << " " << b << " " << c << " " << d << std::endl;
    return 0;
}