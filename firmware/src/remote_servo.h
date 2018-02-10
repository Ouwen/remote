#ifndef REMOTE_SERVO
#define REMOTE_SERVO

#include <Servo.h> 

class Remote_Servo: public Servo
{
	private:
        int pin;
        bool axis_is_right; // axis is either on the left or the right
	public:
		Remote_Servo(int, bool);
		void toggle(bool, int);
		void toggle(bool, int, int);
		void stop();
};

#endif