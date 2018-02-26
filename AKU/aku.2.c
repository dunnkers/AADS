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
#endif

/* ARRAYS */
void *safeMalloc(int sz) {
  void *p = calloc(sz, 1);
  if (p == NULL) {
    fprintf(stderr, "Fatal error: safeMalloc(%d) failed.\n", sz);
    exit(EXIT_FAILURE);
  }
  return p;
}

int *makeIntArray(int n) {
  /* allocates dynamic int array of size/length n */
  return safeMalloc(n * sizeof(int));
}

void destroyArray(void *p) { free(p); }

void printIntArray(int length, int *arr) {
  printf("[");
  if (length > 0) {
    printf("%d", arr[0]);
    for (int i = 1; i < length; i++) {
      printf(",%d", arr[i]);
    }
  }
  printf("]\n");
}

/* BINARY TREE */
typedef struct node {
  struct node *l, *r;
  int value;
} node;

// [ left, visit, right ] // this are actually in-order tree visits
void printTree(node *n) {
  if (n->l)
    printTree(n->l);
  TRACE_PRINT("%d ", n->value);
  if (n->r)
    printTree(n->r);
}

// create a new node & set default nodes
node *newTree(int value) {
  node *n = malloc(sizeof(node));
  n->value = value;
  n->l = n->r = NULL;
  return n;
}

// recursive insertion from the tree root
void insertNode(node **root, node *child) {
  if (!*root)
    *root = child; // tree root not exists
  else
    insertNode(child->value <= (*root)->value ? &(*root)->l : &(*root)->r,
               child); // recursive call
}

// recursive search of a node
node *searchTree(node *root, int value) {
  return !root
             ? NULL
             : root->value == value
                   ? root
                   : searchTree(value > root->value ? root->r : root->l, value);
}

/* PROGRAM */
// Always returns 3 ints
/* Observations:
    an even int will:
    - produce as a middle element 0.

    an uneven int will:
    - produce as a middle element 1
*/
int *split(int x) {
  int *res = makeIntArray(3);
  res[0] = floor(x / 2);
  res[1] = x % 2;
  res[2] = ceil(x / 2);

  if (!(res[0] == 0 || res[0] == 1)) {
    int *l = split(res[0]);
    printIntArray(3, l);
  }

  if (!(res[2] == 0 || res[2] == 1)) {
    int *r = split(res[2]);
    printIntArray(3, r);
  }

  return res;
}

node *splitIntoNodes(node *currNode) {
  int x = currNode->value;
  int flo = floor(x / 2);
  int rem = x % 2;
  int cei = ceil(x / 2);

  currNode->value = rem;

  node *l = newTree(flo);
  if (!(flo == 0 || flo == 1)) {
    // DEBUG_PRINT("flo=%d\n",flo);
    currNode->l = splitIntoNodes(l);
  } else {
    l->value = flo;
    currNode->l = l;
  }

  node *r = newTree(cei);
  if (!(cei == 0 || cei == 1)) {
    // DEBUG_PRINT("cei=%d\n", flo);
    currNode->r = splitIntoNodes(r);
  } else {
    r->value = cei;
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

int main(int argc, char *argv[]) {
// Redirect stdin to a test file in case of TEST environment
#ifdef TEST
  freopen("./AKU/1.in", "r", stdin);
#endif
  DEBUG_PRINT("AKU\n");

  int n, l, r;
  scanf("%d %d %d\n", &n, &l, &r);
  DEBUG_PRINT("Scanned numbers:\n");
  TRACE_PRINT("%d\n", n);
  TRACE_PRINT("%d\n", l);
  TRACE_PRINT("%d\n", r);

  int *arr = makeIntArray(1);
  arr[0] = n;
  int *splitted = split(n);
  printIntArray(3, splitted);

  node *root = newTree(n);
  node *tree = splitIntoNodes(root);
  DEBUG_PRINT("IN\n");
  printTree(tree);

  DEBUG_PRINT("\n\n");
  DEBUG_PRINT("1's in range\n");
  int sum = getSum(tree, l, r);
  printf("%d\n", sum);

  return 0;
}
