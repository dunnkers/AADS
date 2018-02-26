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
#include <string.h>

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

typedef struct Item {
    lint idx;
    lint amount;
    struct Item *left, *right; // neighbors
} Item;

Item* newItem(lint idx, lint amount)
{
    Item* item = safeMalloc(sizeof(Item));
    item->idx = idx;
    item->amount = amount;
    item->left = item->right = NULL;
    return item;
}

void printItemList(Item** items, lint n)
{
    TRACE_PRINT("[");
    for (lint i = 0; i < n; i++) {
        TRACE_PRINT("%lux%s", items[i]->amount, i == n - 1 ? "" : ", ");
    }
    TRACE_PRINT("]\n");
}

/*
    sorts an item list based on amount.
*/
void quick_sort(lint arr[], int first_index, int last_index)
{
    // declaring index variables
    int pivotIndex, temp, index_a, index_b;

    if (first_index < last_index) {
        // assigning first element index as pivot element
        pivotIndex = first_index;
        index_a = first_index;
        index_b = last_index;

        // Sorting in Descending order with quick sort
        while (index_a < index_b) {
            while (arr[index_a] <= arr[pivotIndex] && index_a < last_index) {
                index_a++;
            }
            while (arr[index_b] > arr[pivotIndex]) {
                index_b--;
            }

            if (index_a > index_b) {
                // Swapping operation
                temp = arr[index_a];
                arr[index_a] = arr[index_b];
                arr[index_b] = temp;
            }
        }

        // At the end of first iteration, swap pivot element with index_b element
        temp = arr[pivotIndex];
        arr[pivotIndex] = arr[index_b];
        arr[index_b] = temp;

        // Recursive call for quick sort, with partitioning
        quick_sort(arr, first_index, index_b - 1);
        quick_sort(arr, index_b + 1, last_index);
    }
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
    lint* stack = safeMalloc(MAX_SI * sizeof(lint)); // calloc inits all elems to 0.
    lint max = 1;
    Item** stackk = safeMalloc(MAX_SI * sizeof(Item));
    // TODO record exactly what numbers were found in dynamic array.
    for (lint i = 0; i < n; i ++) {
        lint num;
        scanf("%lu ", &num);
        lint idx = num - 1;

        if (stack[idx] == 0) {
            Item *item = newItem(idx, 0);
            // add left and right..
            stackk[idx] = item;
        }

        // count[num - 1] ++; // [num - 1] because numbers start at 1, but the arr at 0.
        stack[idx] += num;
        stackk[idx]->amount += num;

        if (num > max) {
            max = num;
        }
    }

    TRACE_PRINT("    stack = [");
    for (lint i = 0; i < max; i ++) {
        TRACE_PRINT("%lux%s", stack[i], i == max - 1 ? "" : ", ");
    }
    TRACE_PRINT("]\n");

    quick_sort(stack, 0, max - 1);
    TRACE_PRINT("    sorted stack = [");
    for (lint i = 0; i < max; i ++) {
        TRACE_PRINT("%lux%s", stack[i], i == max - 1 ? "" : ", ");
    }
    TRACE_PRINT("]\n");

    TRACE_PRINT("    item list = ");
    printItemList(stackk, max);

    return 0;
}
