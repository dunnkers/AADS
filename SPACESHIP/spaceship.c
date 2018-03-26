//file: spaceship.c
//author: Rutger Berghuis s2765071 (r.a.berghuis@student.rug.nl)
/* date: Mar 21 2018 */
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

int counter = 1;
int maxCounter = 0;
int checkCounter = 0;
int gateCounter = 0;
int K = 0;

struct Node {
    int data;
    int gate;
    struct Node* next;
};
typedef struct Node* Node;

Node addItem(int data, int gate, Node n)
{
    struct Node* new;
    new = (struct Node*)malloc(sizeof(struct Node));
    new->data = data;
    new->gate = gate;
    new->next = n;
    return new;
}

void checkPressure(Node* nodeArray, int* checkArray, int vertex)
{
    Node N = nodeArray[vertex];
    checkArray[vertex] = 1;
    while (N != NULL) {
        if (checkArray[N->data] == 0) {
            //printf("data:%d\n", N->data);
            checkCounter++;
            if (checkCounter + counter > K) {
                return;
            }
            checkPressure(nodeArray, checkArray, N->data);
        }
        N = N->next;
    }
    return;
}

void traverseGraph(Node* nodeArray, int* visitedArray, int* gatesArray, int vertex)
{
    Node N = nodeArray[vertex];
    visitedArray[vertex] = 1;
    int* checkArray = visitedArray;
    while (N != NULL) {
        if (visitedArray[N->data] == 0) {
            if (N->gate == 0) {
                counter++;
                if (counter > K) {
                    return;
                }
                traverseGraph(nodeArray, visitedArray, gatesArray, N->data);
            }
            if (N->gate == 1) {
                checkCounter = 1;
                checkPressure(nodeArray, checkArray, N->data);
                //printf("checkCounter: %d\n", checkCounter);
                maxCounter += checkCounter;
                gatesArray[gateCounter] = checkCounter;
                gateCounter++;
            }
        }
        N = N->next;
    }
    return;
}

void merge(int* a, int n, int m)
{
    int i, j, k;
    int* x = malloc(n * sizeof(int));
    for (i = 0, j = m, k = 0; k < n; k++) {
        x[k] = j == n ? a[i++]
                      : i == m ? a[j++]
                               : a[j] < a[i] ? a[j++]
                                             : a[i++];
    }
    for (i = 0; i < n; i++) {
        a[i] = x[i];
    }
    free(x);
}

void merge_sort(int* a, int n)
{
    if (n < 2)
        return;
    int m = n / 2;
    merge_sort(a, m);
    merge_sort(a + m, n - m);
    merge(a, n, m);
}

int main(int argc, char* argv[])
{
    freopen("./SPACESHIP/myown.in", "r", stdin);
    int N, a, b, c, answer = 0;
    scanf("%d %d", &N, &K);
    Node nodeArray[N + 1];
    int visitedArray[N + 1];
    int gatesArray[N + 1];
    for (int i = 0; i < N + 1; i++) {
        nodeArray[i] = NULL;
        visitedArray[i] = 0;
        gatesArray[N + 1] = 89238923892;
    }
    for (int j = 0; j < N - 1; j++) {
        scanf("%d %d %d", &a, &b, &c);
        nodeArray[b] = addItem(a, c, nodeArray[b]);
        nodeArray[a] = addItem(b, c, nodeArray[a]);
    }
    traverseGraph(nodeArray, visitedArray, gatesArray, 1);
    int gatesArray2[gateCounter];
    for (int i = 0; i < gateCounter; i++) {
        gatesArray2[i] = gatesArray[i];
        //printf("array %d\n", gatesArray2[i]);
    }
    merge_sort(gatesArray2, gateCounter);
    //printf("counter: %d gateCounter %d\n", counter, gateCounter);
    if (counter > K) {
        printf("%d\n", -1);
    } else {
        maxCounter = maxCounter + counter;
        //printf("maxCouner:%d\n", maxCounter);
        while (maxCounter > K) {
            //printf("ar: %d\n", gatesArray2[gateCounter-1]);
            maxCounter -= gatesArray2[gateCounter - 1];
            //printf("maxCouner:%d\n", maxCounter);
            answer++;
            gateCounter--;
        }
        printf("%d\n", answer);
    }

    return 0;
}
