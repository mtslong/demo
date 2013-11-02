/*
 * demo for get stack address
 */

#include <stdio.h>
#include <stdlib.h>
#include <execinfo.h>

/*#define get_addr(x) __builtin_return_address(x)  */
#define get_addr(x) __builtin_frame_address(x)   /* get stack */

void get_ebp(unsigned long *ebp)
{
        __asm__ __volatile__("mov %%ebp, %0 \r\n"
							:"=m"(*ebp)
                            ::"memory");
}

void print_ebp(void)
{
        unsigned int *pt;
        unsigned long ebp = 0;
        get_ebp(&ebp);
        ebp=*(unsigned long *)ebp;
        pt=(unsigned int *)ebp;
        printf("ebp=%08X , addr=%08x\n",(int)*(pt),(unsigned int)pt);
}

void f1(int a,int b,int c)
{
        print_ebp();

        printf("%s:%p,  father:%p\n",__func__,(void *)get_addr(0),(void *)get_addr(1));
        {
                unsigned int *tv;
                tv=__builtin_frame_address(0);
                tv=tv+2;
                printf("-->self.stack.address=0x%08x\n",(unsigned int)(tv));
                printf("-->self.argv[1]=0x%08x\n",(*tv));
                unsigned int value;
                value=*tv;
                printf("-->self.argv[1]=0x%08x\n\n",(value));
        }
        {
                unsigned int *tv;
                tv=__builtin_frame_address(1);
                tv=tv+2;
                printf("-->father.stack.address=0x%08x\n",(unsigned int)(tv));
                printf("-->father.argv[1]=0x%08x\n",(*tv));
                unsigned int value;
                value=*tv;
                printf("-->father.argv[1]=0x%08x\n\n",(value));
        }

        unsigned int *pt=get_addr(0);
        int i;
        for (i = 0; i < 64; i++) {
                if ( i % 8 == 0 ){
                        printf("\n0x %08X: ",(unsigned int)pt);
                };
                printf("%08X ",(int)*(pt++));
        };
        printf("\n");
}

void test(int a,int b)
{
        print_ebp();
        printf("%s:%p,  father:%p\n",__func__,get_addr(0),get_addr(1));
        printf("a+b=%d\n",a+b);
        f1(0x11,0x22,0x33);
}

int main()
{
        printf("main:\t%p\n",main);
        printf("test:\t%p\n",test);
        printf("f1:\t%p\n",f1);

        printf("%s:%p\n",__func__,get_addr(0));

        test(0x55,0x88);
        return 0;
}
