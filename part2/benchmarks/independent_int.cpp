#include <iostream>
#include <gem5/m5ops.h>

int main()
{
    volatile long long a = 1, b = 2, c = 3, d = 4;

    m5_work_begin(0, 0);

    for (long long i = 0; i < 1000000; i++) {
        a += 3;
        b += 5;
        c += 7;
        d += 11;
    }

    m5_work_end(0, 0);

    std::cout << a << " " << b << " " << c << " " << d << std::endl;
    return 0;
}