/**
 * Author: 		    Jeroen Overschie
 * S-number:		s2995697
 * Date:			16-02-2018
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

const int POWTWO_LENGTH = 50;
// Up to 2^49, since n is guaranteed to be lower than 2^50.
const long long int POWTWO[50] = {
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
  562949953421312
};

void *safeMalloc(int sz) {
  void *p = calloc(sz, 1);
  if (p == NULL) {
    fprintf(stderr, "Fatal error: safeMalloc(%d) failed.\n", sz);
    exit(EXIT_FAILURE);
  }
  return p;
}

/* BINARY TREE */
typedef struct node {
  struct node *l, *r;
  int value;
} node;

// create a new node & set default nodes
node *newTree(int value) {
  node *n = safeMalloc(sizeof(node));
  n->value = value;
  n->l = n->r = NULL;
  return n;
}

/* SYMMETRIC BINARY TREE - we might as well call this a linked list */
typedef struct SymmetricTree {
    struct SymmetricTree *next;
    long long int value;
} SymmetricTree;

// create a new node & set default nodes
SymmetricTree *newSymmetricTree(long long int value)
{
    SymmetricTree* tree = safeMalloc(sizeof(SymmetricTree));
    tree->value = value;
    tree->next = NULL;
    return tree;
}

node *splitIntoNodes(node *currNode, int *steps) {
  int x = currNode->value;
  int left = floor(x / 2);
  int rem = x % 2;
  int right = floor(x / 2);
  *steps += 1;

  currNode->value = rem;

  node *l = newTree(left);
  if (!(left == 0 || left == 1)) {
    // TRACE_PRINT("left=%d\n",left);
    currNode->l = splitIntoNodes(l, steps);
  } else {
    l->value = left;
    currNode->l = l;
  }

  node *r = newTree(right);
  if (!(right == 0 || right == 1)) {
    // TRACE_PRINT("right=%d\n", right);
    currNode->r = splitIntoNodes(r, steps);
  } else {
    r->value = right;
    currNode->r = r;
  }

  return currNode;
}

void computeSum(node* tree, int l, int r, int *curr, int *sum)
{
    if (tree->l) {
        computeSum(tree->l, l, r, curr, sum);
    }

    // TRACE_PRINT("[%d] = %d\n", *curr, tree->value);
    if (*curr >= l && *curr <= r) {
        *sum += tree->value;
        // TRACE_PRINT("sum += %d (curr=%d)\n", tree->value, *curr);
    }
    *curr += 1;

    if (tree->r) {
        computeSum(tree->r, l, r, curr, sum);
    }
}

int getSum(node* tree, int l, int r)
{
    int curr = 1, sum = 0;
    computeSum(tree, l, r, &curr, &sum);
    return sum;
}

int getTreeHeight(long long int n)
{
    for (int i = 0; i < POWTWO_LENGTH; i++) {
        if (n <= POWTWO[i]) {
            // TRACE_PRINT("n = %lli <= 2^%d = %lli\n", n, i, POWTWO[i]);
            return i == 1 ? 0 : i - 1;
        }
    }

    return -1; // n >= 2^50 // not supported
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

void incrSum() {

}

SymmetricTree *splitNumber(SymmetricTree* currNode, int* depth, int height, 
  int l, int r, int *sum)
{
    if (currNode->value == 0 || currNode->value == 1) { // exit early.
      TRACE_PRINT("EARLY EXIT");
        *sum += currNode->value;
        return currNode;
    }

    SymmetricTree *next = newSymmetricTree(floor(currNode->value / 2));
    currNode->value = currNode->value % 2;
    // *sum += currNode->value * POWTWO[*depth];
    TRACE_PRINT("*sum += %d*%d\n", currNode->value, POWTWO[*depth]);

    // array indices
    int levelIdx = POWTWO[height - *depth] - 1, // for depth = 1: 2^(2) - 1 = 3
        increment = POWTWO[height - *depth + 1]; // for depth = 1: 2^(3) = 8
    TRACE_PRINT("DEPTH %d; levelIdx = %d, incrementing with +%d:\n", 
      *depth, levelIdx, increment);
    for (int i = 0, j = levelIdx; i < POWTWO[*depth]; i++) {
      TRACE_PRINT("[%d] ", j);
      j += increment;
    }

    int leftBound = levelIdx,
        rightBound = levelIdx + increment * (POWTWO[*depth] - 1);
    // int relativeLPosition = ((leftBound + 1) - l) % increment;
    // int relativeRPosition = (rightBound + 1) - r;
    // int num = ((r+relativeRPosition)-(l+relativeLPosition)) / 8;
    // int lefty = relativeLPosition + l;
    // int righty = relativeRPosition + r;

    // double spaceL = ceil((double) (leftBound - l) / (double) increment);
    // double spaceR = ceil((rightBound - r) / increment);
    // int relatiLBound = abs((int) spaceL);
    // // if (relatiLBound < 0) { relatiLBound *= -1; }
    // int relatiRBound = abs((int) spaceR);
    // // if (relatiRBound < 0) { relatiRBound *= -1; }
    // relatiLBound = leftBound + increment * relatiLBound;
    // relatiRBound = rightBound - increment * relatiRBound;

    int dude1 = l - leftBound; // distance away from `l`. positive # is left from bound
    int multipls = dude1 > 0 ? (int)(ceil((double)dude1 / (double)increment)) : 0;
    int okduder = leftBound + increment * multipls;

    int dude2 = rightBound - r; // distance away from `r`. positive # is right from bound
    int multipls2 = dude2 > 0 ? (int)(ceil((double)dude2 / (double)increment)) : 0;
    int okduder2 = rightBound -  increment * multipls2;

    int amt = okduder2 - okduder;
    int final = amt / increment + 1;
    *depth += 1;
    // *sum += final * 
    // if (relativeLPosition >= 0) { // it hit the pole
    //   *sum += 1;
    // }
    // if (relativeRPosition <= 0) { // it hit the pole
    //   *sum += 1;
    // }
    // int conclusion = (righty - lefty) / increment;
    // TRACE_PRINT("\n");
    // TRACE_PRINT("IDX RANGE [%d, %d]\n", leftBound, rightBound);
    // TRACE_PRINT("\n");

    // if (l >= leftBound && l <= rightBound && r >= leftBound && r <= rightBound) {
    //   TRACE_PRINT("Within bounds at depth %d\n", *depth);
    // }

    // if (next->value <= 1) { // we can stop recursion now.
    //   currNode->next = next;
    //   // *sum += next->value * POWTWO[*depth];
    //   // TRACE_PRINT("*sum += %d\n", next->value * POWTWO[*depth]);
    // } else {
    //   currNode->next = splitNumber(next, depth, height, l, r, sum);
    // }
    currNode->next = splitNumber(next, depth, height, l, r, sum);

    return currNode;
}

// void printSymmetricTree(SymmetricTree *head)
// {
//   SymmetricTree* cursor = head;
//   while (cursor != NULL) {
//     TRACE_PRINT("%lli%s", cursor->value, cursor->next == NULL ? "" : "->");
//     cursor = cursor->next;
//   }
// }

void printSymmetricTree(SymmetricTree* node)
{
  if (node->next) {
    printSymmetricTree(node->next);
  }
  TRACE_PRINT("%lli%s", node->value, ", ");
  if (node->next) {
    printSymmetricTree(node->next);
  }
}

int main(int argc, char *argv[]) {
// Redirect stdin to a test file in case of TEST environment
#ifdef TEST
  freopen("./AKU/2.in", "r", stdin);
#endif
  DEBUG_PRINT("AKU\n");

  long long int n;
  int l, r;
  scanf("%lli %d %d\n", &n, &l, &r);
  DEBUG_PRINT("INPUT:\n");
  TRACE_PRINT("n = %lli, l = %d, r = %d\n", n, l, r);

  DEBUG_PRINT("EXPECTED TREE\n");
  int height = findTreeHeight(n);
  // produces nodes = 0 for n = 0
  // we only need one side of the tree.
  long long int nodes = POWTWO[height] - 1;
  TRACE_PRINT("Tree height: %d\n", height);
  // (also called, if stored in array; array size)
  TRACE_PRINT("Max. nodes of one side of the tree: %d\n", nodes);
  SymmetricTree *symmTree = newSymmetricTree(n);
  int depth = 0, summy = 0; // correct l and r to represent index instead of position
  SymmetricTree* res = splitNumber(symmTree, &depth, height, l - 1, r - 1, &summy);
  DEBUG_PRINT("Linked list:\n");
  TRACE_PRINT("[");
  printSymmetricTree(res);
  TRACE_PRINT("]\n");
  DEBUG_PRINT("depth: %d\n", depth);
  TRACE_PRINT("summy: %d\n", summy);

  int steps = 0;
  node *root = newTree(n);
  node *tree = splitIntoNodes(root, &steps);

  DEBUG_PRINT("SUM:\n");
  int sum = getSum(tree, l, r);
  printf("%d\n", sum);

  DEBUG_PRINT("In %d steps\n", steps);

  return 0;
}
