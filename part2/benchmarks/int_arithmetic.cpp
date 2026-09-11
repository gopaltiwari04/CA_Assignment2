#include <iostream>
#include <gem5/m5ops.h>

int main()
{
    volatile long long a = 1, b = 2, c = 3, d = 4;

    m5_work_begin(0, 0);

    for (long long i = 0; i < 1000000; i++) {
        a = (a + b) % 1000000;
        b = (b + c) % 1000000;
        c = (c + d) % 1000000;
        d = (d + a) % 1000000;
    }

    m5_work_end(0, 0);

    std::cout << a << " " << b << " " << c << " " << d << std::endl;
    return 0;
}