//file: color.c
//author: Rutger Berghuis s2765071 (r.a.berghuis@student.rug.nl)
/* date: Mar 14 2018 */
#include <stdio.h>
#include <stdlib.h>

int red=0;
int blue=0;
int false=0;

struct Node {
    int data;
    struct Node *next;
};
typedef struct Node *Node;

Node addItem(int data, Node n){
	struct Node *new;
	new = (struct Node*)malloc(sizeof(struct Node));
	new->data = data;
	new->next = n;
	return new;
}

void check(Node *nodeArray, int *colorArray, int N){
	for(int i=1; i<N+1; i++){
		while(nodeArray[i] != NULL){
			if(colorArray[nodeArray[i]->data]==colorArray[i]){
				false=1;
				break;
			}
			nodeArray[i]=nodeArray[i]->next;
		}
	}
return;
}

void traverseGraph(Node *nodeArray, int *visitedArray, int *colorArray, int vertex, int colorSwitch){
	Node N = nodeArray[vertex];
	visitedArray[vertex]=1;
	//printf("vertex: %d\n", vertex);
	if(colorSwitch==1){
		colorSwitch=2;
		red++;
		colorArray[vertex]=1;
	} else{
		colorSwitch=1;
		blue++;
		colorArray[vertex]=2;
	}
	while(N!=NULL){
		if(visitedArray[N->data]==0){
			traverseGraph(nodeArray, visitedArray, colorArray, N->data, colorSwitch);
		}
		N=N->next;
	}
	//printf("red %d\n", red);
	return;
}


int main(int argc, char *argv[]) {
    freopen("./COLOR/3.in", "r", stdin);
	int T, N, M, a, b;
	scanf("%d", &T);
	int answerArray[T];
	for(int k=0; k<T; k++){
		scanf("%d %d", &N, &M);
		Node nodeArray[N+1];
		int visitedArray[N];
		int colorArray[N];
		for(int i=0; i<N+1; i++){
			nodeArray[i]=NULL;
			visitedArray[i]=0;
			colorArray[i]=0;
		}
		for(int j=0; j<M; j++){
			scanf("%d %d", &a, &b);
			nodeArray[b]=addItem(a, nodeArray[b]);
			nodeArray[a]=addItem(b, nodeArray[a]);
		}
		/*for(int j=1; j<N+1; j++){
			printf("%d:",j);
			printList(nodeArray[j]);
		}*/
		int vertex=1;
		while(nodeArray[vertex]==NULL){
			vertex++;
		} 
		red=0;
		blue=0;
		false=0;
		traverseGraph(nodeArray, visitedArray, colorArray, vertex, 1);
		if(red<blue){
			red=blue;
		}
		blue=red;
		for(int j=1; j<N+1; j++){
			if(visitedArray[j]==0){
				if(nodeArray[j]!=NULL){
					traverseGraph(nodeArray, visitedArray, colorArray, j, 1);
					if(red<blue){
						red=blue;
					}
					blue=red;
				}
			}
		}
		check(nodeArray, colorArray, N);
		if(false==1){
			answerArray[k]=-1;
		} else{
			for(int j=1; j<N+1; j++){
				if(visitedArray[j]==0){
					red++;
				}
			}
			answerArray[k]=red;
		}
	}
for(int k=0; k<T; k++){
	printf("%d\n", answerArray[k]);
}
return 0;
}
