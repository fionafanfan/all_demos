#include <stdio.h>

/* Maximum value between x and y */
#define Py_MAX(x, y) (((x) > (y)) ? (x) : (y))


int hello(void) {
	printf("hello world");
	return 0;
}

int max(void) {
	int a = 10;
	int b = 20;
	int max_value = Py_MAX(a, b);
	printf("\n最大值是：%d\n", max_value);
	return max_value;
}
int main(void) {
	hello();
	max();
}