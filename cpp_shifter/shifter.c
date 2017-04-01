#include "shifter.h"

#include <stdio.h>

int main(int argc, char *argv[]){
	uint16_4_shifter s;
	u16_4s_init(&s, 0, 1, 2, 3);
	printf("Original:\r\n");
	printf("\tshifter: [%d, %d, %d, %d]\r\n", s.v1, s.v2, s.v3, s.v4);

	printf("Rotate right:\r\n");
	u16_4s_rotate_right(&s);
	printf("\tshifter: [%d, %d, %d, %d]\r\n", s.v1, s.v2, s.v3, s.v4);

	printf("Rotate right:\r\n");
	u16_4s_rotate_right(&s);
	printf("\tshifter: [%d, %d, %d, %d]\r\n", s.v1, s.v2, s.v3, s.v4);

	printf("Rotate right:\r\n");
	u16_4s_rotate_right(&s);
	printf("\tshifter: [%d, %d, %d, %d]\r\n", s.v1, s.v2, s.v3, s.v4);
}
