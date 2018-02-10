#include "remote_servo.h"

Remote_Servo::Remote_Servo(int pin_, bool axis_is_right_) : pin(pin_), axis_is_right(axis_is_right_) {
	Servo::attach(pin);
	Servo::write(90);
}

void Remote_Servo::toggle(bool on, int rotation) {
	if (axis_is_right){
		rotation = rotation*(-1);
	}
	if (!on){
		rotation = rotation*(-1);
	}	
	Servo::write(90 + rotation);
}

void Remote_Servo::toggle(bool on, int rotation, int milliseconds) {
	if (axis_is_right){
		rotation = rotation*(-1);
	}
	if (!on){
		rotation = rotation*(-1);
	}
	Servo::write(90 + rotation);
	delay(milliseconds);
	Servo::write(90);
}

void Remote_Servo::stop() {
	Servo::write(90);
}