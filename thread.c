/*
 * demo for volatile
 */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

# if defined USE_VOLATILE
volatile int flag;
#else
int flag;
#endif


void threadA(void)
{
	usleep(10);
	printf("\t->%s: flag=%d\n", __func__, flag);
	flag = 0;
	printf("\t->%s: flag=%d\n", __func__, flag);
}

void threadB(void)
{
	int i;

	for (i = 0; i < 5; i++) {
		printf("\t%d %s: flag=%d\n", i, __func__, flag);
		usleep(10);
	};
}

int main()
{
	pthread_t pthA;
	pthread_t pthB;
	int i=0;

	printf("--- demo start ---\n");
        while(1) {
	/*for (i = 0; i < 100; i++) {*/
		printf("%d %s:flag=%d\n", i, __func__, flag);
		flag = 1;
		printf("%d %s:flag=%d\n", i, __func__, flag);

		pthread_create(&pthA, NULL, (void *) threadA, NULL);
		pthread_create(&pthB, NULL, (void *) threadB, NULL);

		int count=0;
		while (flag) {
                        count++;
                        /* if call syscall.then update the flag */
                        /*printf("\t\t\t\t\tcount=%d.\r", count); fflush(NULL);*/
		};		/* test */

		pthread_join(pthA, NULL);
		pthread_join(pthB, NULL);
		printf("%d %s:flag=%d is OK.\n\n", i, __func__, flag);
	};

	printf("--- demo finished.---\n");

	return 0;
}
