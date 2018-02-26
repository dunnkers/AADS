/**
 * Author: 		    Jeroen Overschie
 * S-number:		s2995697
 * Date:			24-02-2018
 * Challenge:	    AKU
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

/*
  PERFORMANCE IMPROVEMENTS
  - exit node creation early when not in index range
  - compute 1-sum at the same time as creating tree
  - tree is symmetric: only compute one side.
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

const int POWTWO_LENGTH = 51;
// Up to 2^50, since n is guaranteed to be lower than 2^50.
const long long int POWTWO[51] = {
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
  1125899906842624
};

void *safeMalloc(int sz) {
  void *p = calloc(sz, 1);
  if (p == NULL) {
    fprintf(stderr, "Fatal error: safeMalloc(%d) failed.\n", sz);
    exit(EXIT_FAILURE);
  }
  return p;
}


/* SYMMETRIC BINARY TREE - we might as well call this a linked list */
typedef struct LinkedList {
    struct LinkedList *next;
    long long int value;
} LinkedList;

// create a new node & set default nodes
LinkedList *newLinkedList(long long int value)
{
    LinkedList* tree = safeMalloc(sizeof(LinkedList));
    tree->value = value;
    tree->next = NULL;
    return tree;
}

int *findTreeHeight(long long int n)
{
    for (int i = 0; i < POWTWO_LENGTH; i++) {
        if (n <= POWTWO[i]) {
            return i == 0 ? 0 : i - 1;
        }
    }

    return -1; // n >= 2^50 // not supported
}

void incrSum(int *depth, int height, long long int l, long long int r, 
  unsigned long long int *sum, long long int value, int *numberOfPasses) {
    // array indices
    int idx = height - *depth < 0 ? 0 : height - *depth;
    long long int levelIdx = POWTWO[idx] - 1, // for depth = 1: 2^(2) - 1 = 3
        increment = POWTWO[idx + 1]; // for depth = 1: 2^(3) = 8
#ifdef TEST
    TRACE_PRINT("DEPTH %d; levelIdx = %lli, incrementing with +%lli:\n    ",
        *depth, levelIdx, increment);
    // for (int i = 0, j = levelIdx; i < POWTWO[*depth]; i++) {
    //     TRACE_PRINT("[%d] ", j);
    //     j += increment;
    // }
#endif

    long long int leftBound = levelIdx,
        rightBound = levelIdx + increment * (POWTWO[*depth] - 1);

    long long int inRangeLIdx = l - leftBound; // distance away from `l`. positive # is left from bound
    inRangeLIdx = inRangeLIdx > 0 ? (long long int)(ceil((double)inRangeLIdx / (double)increment)) : 0;
    inRangeLIdx = leftBound + increment * inRangeLIdx;

    long long int inRangeRIdx = rightBound - r; // distance away from `r`. positive # is right from bound
    inRangeRIdx = inRangeRIdx > 0 ? (long long int)(ceil((double)inRangeRIdx / (double)increment)) : 0;
    inRangeRIdx = rightBound - increment * inRangeRIdx;

    long long int amt = inRangeRIdx - inRangeLIdx;
    amt = amt / increment + 1;
    *sum += amt * value;
    *numberOfPasses += amt;
    TRACE_PRINT("\n    sum += %lli (amt = %lli, value = %lli)\n", amt * value, amt, value);
}

LinkedList *splitNumber(LinkedList *currNode, int *depth, int height, 
  long long int l, long long int r, unsigned long long int *sum, int *numberOfPasses)
{
    // if (*numberOfPasses >= (r - l + 1)) {
    //   TRACE_PRINT("    EXIT EARLY\n");
    //   return currNode;
    // }
    if (currNode->value == 0 || currNode->value == 1) { // exit early.
      TRACE_PRINT("    EXIT RECURSION\n");
      incrSum(depth, height, l, r, sum, currNode->value, numberOfPasses);
      return currNode;
    }

    LinkedList *next = newLinkedList(floor((double) currNode->value / 2.0));
    currNode->value = currNode->value % 2;

    incrSum(depth, height, l, r, sum, currNode->value, numberOfPasses);

    *depth += 1;

    currNode->next = splitNumber(next, depth, height, l, r, sum, numberOfPasses);

    return currNode;
}

void printLinkedList(LinkedList* node)
{
  if (node->next) {
    printLinkedList(node->next);
  }
  TRACE_PRINT("%lli%s", node->value, ", ");
  if (node->next) {
    printLinkedList(node->next);
  }
}

int main(int argc, char *argv[]) {
// Redirect stdin to a test file in case of TEST environment
#ifdef TEST
  freopen("./AKU/6.in", "r", stdin);
#endif
  DEBUG_PRINT("AKU\n");

  long long int n, l, r;
  scanf("%lli %lli %lli\n", &n, &l, &r);
  DEBUG_PRINT("INPUT:\n");
  TRACE_PRINT("    n = %lli, l = %d, r = %d\n", n, l, r);

  DEBUG_PRINT("EXPECTED TREE\n");
  int height = findTreeHeight(n);
  // produces nodes = 0 for n = 0
  // we only need one side of the tree.
  TRACE_PRINT("    Tree height: %d\n", height);
  LinkedList *symmTree = newLinkedList(n);
  int depth = 0, numberOfPasses = 0;
  unsigned long long int sum = 0;
  // correct l and r to represent index instead of position
  LinkedList* res = splitNumber(symmTree, &depth, height, l - 1, r - 1, 
    &sum, &numberOfPasses);
  // DEBUG_PRINT("Linked list:\n");
  // TRACE_PRINT("     [");
  // printLinkedList(res);
  // TRACE_PRINT("]\n");
  TRACE_PRINT("    depth: %lli\n", depth);
  TRACE_PRINT("SUM:\n");
  printf("%llu\n", sum);

  return 0;
}
