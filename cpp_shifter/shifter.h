/**
* @file shifter.h
* @author Cameron A. Craig
* @date 5 Mar 2017
* @copyright 2017 Cameron A. Craig
* @brief Shift/rotate right and left on 4 uint16_t values.
*/
#ifndef CAM_SHIFTER_H
#define CAM_SHIFTER_H

#include <stdint.h>

typedef struct {
	uint16_t v1, v2, v3, v4;
} uint16_4_shifter;

void u16_4s_init(uint16_4_shifter *s, uint16_t v1, uint16_t v2, uint16_t v3, uint16_t v4){
	s->v1 = v1;
	s->v2 = v2;
	s->v3 = v3;
	s->v4 = v4;
}

void u16_4s_rotate_right(uint16_4_shifter *s){
	s->v1 = s->v4;
	s->v2 = s->v1;
	s->v3 = 4;//s->v2;
	s->v4 = s->v3;
}

void u16_4s_rotate_left(uint16_4_shifter *s){
	s->v1 = s->v2;
	s->v2 = s->v3;
	s->v3 = s->v4;
	s->v4 = s->v1;
}

void u16_4s_shift_right(uint16_4_shifter *s, uint16_t v1){
	s->v1 = v1;
	s->v2 = s->v1;
	s->v3 = s->v2;
	s->v4 = s->v3;
}

void u16_4s_shift_left(uint16_4_shifter *s, uint16_t v4){
	s->v1 = s->v2;
	s->v2 = s->v3;
	s->v3 = s->v4;
	s->v4 = v4;
}

#endif //CAM_SHIFTER_H
