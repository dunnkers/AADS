/**
 * Author: 		  Jeroen Overschie
 * S-number:		s2995697
 * Date:			  24-02-2018
 * Challenge:	  AKU
 * 
 * The input for this program are three numbers n, l and r. The program
 * then computes how many 1's exist in the range [l, r] of the array 
 * resulting from an operation on n that continues until a number is 
 * either 0 or 1. This operation is for a number x > 0:
 * floor(x), x mod 2, floor(x).
 * 
 * 
 * Time complexity: x
 * n is .... Runs in ..., because
 * 
 * Memory complexity: x
 * Because, ...
 * 
 * Submission link, for own ease of use:
 * http://themis.housing.rug.nl/course/2017-2018/aads/AKU/c
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
    freopen("./GAME/1.in", "r", stdin);
#endif
    DEBUG_PRINT("GAME\n");

    lint n;
    scanf("%lu\n", &n);
    // TRACE_PRINT("    seq = [");
    // for (lint i = 0; i < n; i++) {
    //     TRACE_PRINT("%lu%s", seq[i], i == n - 1 ? "" : ", ");
    // }
    // TRACE_PRINT("]\n");

    DEBUG_PRINT("INPUT:\n");
    TRACE_PRINT("    n = %lu, seq = [", n);
    lint* seq = safeMalloc(MAX_SI * sizeof(lint)); // calloc inits all elems to 0.
    for (lint i = 0; i < n; i++) {
        // lint num;
        scanf("%lu ", &seq[i]);
        TRACE_PRINT("%lu%s", seq[i], i == n - 1 ? "" : ", ");
    }
    TRACE_PRINT("]");

    return 0;
}
