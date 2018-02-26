/**
 * Author: 		    Jeroen Overschie
 * S-number:		s2995697
 * Date:		    24-02-2018
 * Challenge:	    AKU
 * 
 * The input for this program are three numbers n, l and r. The program
 * then computes how many 1's exist in the range [l, r] of the array 
 * resulting from an operation on n that continues until a number is 
 * either 0 or 1. This operation is for a number x > 0:
 * floor(x), x mod 2, floor(x).
 */

#include <math.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* DEBUGGING */
#define __FILENAME__                                                           \
  (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__)
#ifdef TEST
#define DEBUG_PRINT(fmt, ...)                                                  \
  fprintf(stderr, "%s %s %s:%d:%s(): " fmt, __DATE__, __TIME__, __FILENAME__,  \
          __LINE__, __func__, ##__VA_ARGS__)
#define TRACE_PRINT(fmt, ...) fprintf(stderr, fmt, ##__VA_ARGS__)
#else
#define DEBUG_PRINT(fmt, ...)
#define TRACE_PRINT(fmt, ...)
#endif

typedef long long int llint; // shorthand

// Up to 2^50, since n is guaranteed to be lower than 2^50
const int POWTWO_LENGTH = 51;
const llint POWTWO[51] = {
  1, // 2^0
  2,
  4,
  8,
  16,
  32,
  64,
  128,
  256,
  512,
  1024,
  2048,
  4096,
  8192,
  16384,
  32768,
  65536,
  131072,
  262144,
  524288,
  1048576,
  2097152,
  4194304,
  8388608,
  16777216,
  33554432,
  67108864,
  134217728,
  268435456,
  536870912,
  1073741824,
  2147483648,
  4294967296,
  8589934592,
  17179869184,
  34359738368,
  68719476736,
  137438953472,
  274877906944,
  549755813888,
  1099511627776,
  2199023255552,
  4398046511104,
  8796093022208,
  17592186044416,
  35184372088832,
  70368744177664,
  140737488355328,
  281474976710656,
  562949953421312,
  1125899906842624 // 2^50
};

int *findTreeHeight(llint n)
{
    for (int i = 0; i < POWTWO_LENGTH; i++) {
        if (n <= POWTWO[i]) {
            return i == 0 ? 0 : i - 1;
        }
    }

    return -1; // n >= 2^50 not supported
}

llint incrSum(int *depth, int height, llint l, llint r) {
    int idx = height - *depth < 0 ? 0 : height - *depth;
    llint leftBound = POWTWO[idx] - 1,
          increment = POWTWO[idx + 1],
          rightBound = leftBound + increment * (POWTWO[*depth] - 1);

    TRACE_PRINT("DEPTH %d; leftBound = %lli, increment = %lli:\n    ",
        *depth, leftBound, increment);

    llint inRangeLIdx = l - leftBound; // distance away from `l`. positive # is left from bound
    inRangeLIdx = inRangeLIdx > 0 ? (llint)(ceil((double)inRangeLIdx / (double)increment)) : 0;
    inRangeLIdx = leftBound + increment * inRangeLIdx;

    llint inRangeRIdx = rightBound - r; // distance away from `r`. positive # is right from bound
    inRangeRIdx = inRangeRIdx > 0 ? (llint)(ceil((double)inRangeRIdx / (double)increment)) : 0;
    inRangeRIdx = rightBound - increment * inRangeRIdx;

    llint amt = inRangeRIdx - inRangeLIdx;
    amt = amt / increment + 1;
    TRACE_PRINT("\n    sum += %lli*value\n", amt);
    return amt;
}

llint splitNumber(llint n, int* depth, int height, llint l, llint r, llint* sum)
{
    if (n == 0 || n == 1) { // recursion guard
      TRACE_PRINT("    EXIT RECURSION\n");
      *sum += incrSum(depth, height, l, r) * n;
      return *sum;
    }

    llint children = (llint) floor((double) n / 2.0);
    n = n % 2;
    *sum += incrSum(depth, height, l, r) * n;
    *depth += 1;

    return splitNumber(children, depth, height, l, r, sum);
}

llint fightAku(llint n, llint l, llint r)
{
    int height = findTreeHeight(n), depth = 0;
    llint sum = 0;
  
    TRACE_PRINT("    Tree height: %d\n", height);

    // subtract 1 from l and r to represent index instead of position
    return splitNumber(n, &depth, height, l - 1, r - 1, &sum);
}

int main(int argc, char *argv[]) {
// Redirect stdin to a test file in case of TEST environment
#ifdef TEST
    freopen("./AKU/7.in", "r", stdin);
#endif
    DEBUG_PRINT("AKU\n");

    llint n, l, r;
    scanf("%lli %lli %lli\n", &n, &l, &r);
    DEBUG_PRINT("INPUT:\n");
    TRACE_PRINT("    n = %lli, l = %d, r = %d\n", n, l, r);

    llint sum = fightAku(n, l, r);
    TRACE_PRINT("SUM:\n");
    printf("%llu\n", sum);

    return 0;
}
