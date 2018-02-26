/**
 * Author: 		  Jeroen Overschie
 * S-number:	  s2995697
 * Date:		  24-02-2018
 * Challenge:	  GAME
 * 
 * The input for this program is a number n on the first line, with n numbers on
 * the second line. All input numbers are between 1 and 10^5.
 * 
 * 
 * Time complexity: x
 * n is .... Runs in ..., because
 * 
 * Memory complexity: x
 * Because, ...
 * 
 * Submission link, for own ease of use:
 * http://themis.housing.rug.nl/course/2017-2018/aads/GAME/c
 */

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>

/* DEBUGGING */
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

typedef unsigned long int lint; // shorthand
const lint MAX_SI = 100000;

void* safeMalloc(int sz)
{
    void* p = calloc(sz, 1);
    if (p == NULL) {
        fprintf(stderr, "Fatal error: safeMalloc(%d) failed.\n", sz);
        exit(EXIT_FAILURE);
    }
    return p;
}

int main(int argc, char* argv[])
{
// Redirect stdin to a test file in case of TEST environment
#ifdef TEST
    freopen("./GAME/2.in", "r", stdin);
#endif
    DEBUG_PRINT("GAME\n");

    lint n;
    scanf("%lu\n", &n);

    DEBUG_PRINT("INPUT:\n");
    TRACE_PRINT("    n = %lu", n);
    lint* count = safeMalloc(MAX_SI * sizeof(lint)); // calloc inits all elems to 0.
    lint max = 1;
    // TODO record exactly what numbers were found in dynamic array.
    for (lint i = 0; i < n; i ++) {
        lint num;
        scanf("%lu ", &num);
        count[num - 1] ++; // [num - 1] because numbers start at 1, but the arr at 0.

        if (num > max) {
            max = num;
        }
    }

    TRACE_PRINT("    count = [");
    for (lint i = 0; i < max; i ++) {
        TRACE_PRINT("%lux%s", count[i], i == max - 1 ? "" : ", ");
    }
    TRACE_PRINT("]\n");

    return 0;
}
