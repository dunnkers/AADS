/**
 * Author: 		    Jeroen Overschie
 * S-number:		s2995697
 * Date:			24-02-2018
 * Challenge:	    TABLE
 * 
 * The input for this program are three numbers n, m and k. The program
 * then computes the k-th largest number in the multiplication table of
 * up to n * m.
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define __FILENAME__ \
    (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__)
#ifdef TEST
#define DEBUG_PRINT(fmt, ...)                                                   \
    fprintf(stderr, "%s %s %s:%d:%s(): " fmt, __DATE__, __TIME__, __FILENAME__, \
        __LINE__, __func__, ##__VA_ARGS__)
#define TRACE_PRINT(fmt, ...) fprintf(stderr, fmt, ##__VA_ARGS__)
#else
#define DEBUG_PRINT(fmt, ...)
#define TRACE_PRINT(fmt, ...)
#endif

#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define MAX(a, b) (((a) > (b)) ? (a) : (b))

typedef unsigned long int lint; // shorthand

lint getKthLargestNumber(lint n, lint m, lint k)
{
    lint smallest = 1, largest = m * n;

    while (smallest < largest) {
        lint newMin = smallest + (largest - smallest) / 2;

        if (!isSufficient(n, m, k, newMin)) {
            smallest = newMin + 1;
        } else {
            largest = newMin;
        }
    }

    return smallest;
}

int isSufficient(lint n, lint m, lint k, lint x)
{
    lint count = 0;
    for (lint i = 1; i <= m; i++) {
        count += MIN(x / i, n);
    }
    return count >= k;
}

int main(int argc, char* argv[])
{
// Redirect stdin to a test file in case of TEST environment
#ifdef TEST
    freopen("./TABLE/2.in", "r", stdin);
#endif
    DEBUG_PRINT("TABLE\n");

    lint n, m, k;
    scanf("%lu %lu %lu\n", &n, &m, &k);
    DEBUG_PRINT("Scanned numbers:\n");
    TRACE_PRINT("%d\n", n);
    TRACE_PRINT("%d\n", m);
    TRACE_PRINT("%d\n", k);

    lint l = getKthLargestNumber(n, m, k);
    printf("%lu\n", l);

    return 0;
}
