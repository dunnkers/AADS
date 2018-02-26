#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>

#define __FILENAME__ (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__)
#ifdef TEST
#define DEBUG_PRINT(fmt, ...) fprintf(stderr, "%s %s %s:%d:%s(): " fmt, \
            __DATE__, __TIME__, __FILENAME__, __LINE__, __func__, ##__VA_ARGS__)
#else
#define DEBUG_PRINT(fmt, ...)
#endif

void setup(int argc, char *argv[])
{
    #ifdef TEST
        freopen("./AKU/1.in", "r", stdin);
    #endif
}

void *safeMalloc(int sz)
{
    void *p = calloc(sz, 1);
    if (p == NULL)
    {
        fprintf(stderr, "Fatal error: safeMalloc(%d) failed.\n", sz);
        exit(EXIT_FAILURE);
    }
    return p;
}

int *makeIntArray(int n)
{
    /* allocates dynamic int array of size/length n */
    return safeMalloc(n * sizeof(int));
}

void destroyArray(void *p)
{
    free(p);
}

void printIntArray(int length, int *arr)
{
    printf("[");
    if (length > 0)
    {
        printf("%d", arr[0]);
        for (int i = 1; i < length; i++)
        {
            printf(",%d", arr[i]);
        }
    }
    printf("]\n");
}


int main(int argc, char *argv[])
{
    setup(argc, argv);
    DEBUG_PRINT("AKU\n");

    int n, l, r;
    scanf("%d %d %d\n", &n, &l, &r);

    printf("%d\n", n);
    printf("%d\n", l);
    printf("%d\n", r);

    return 0;
}
