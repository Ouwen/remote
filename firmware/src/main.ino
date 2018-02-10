#include <Arduino.h> 
#include <Conduit.h>
#include <remote_servo.h> 
#include <info.h>

Remote_Servo head_servo(D4, true);
Remote_Servo foot_servo(D3, false);
Remote_Servo head_massage_servo(D2, true);
Remote_Servo foot_massage_servo(D1, false);

const int bed_switch_constant = 45;
const int massage_switch_constant = 40;
const int massage_delay_milliseconds = 300;

Conduit conduit(CONDUIT_INFO::device_name, CONDUIT_INFO::server_url, CONDUIT_INFO::api_key);

void setup(void){
  conduit.startWIFI(WIFI_INFO::ssid, WIFI_INFO::password);
  conduit.init();

  conduit.addHandler("head_on", ([]() -> int { head_servo.toggle(true, bed_switch_constant); }));
  conduit.addHandler("head_off", ([]() -> int { head_servo.toggle(false, bed_switch_constant); }));
  conduit.addHandler("head_stop", ([]() -> int { head_servo.stop(); }));

  conduit.addHandler("foot_on", ([]() -> int { foot_servo.toggle(true, bed_switch_constant); }));
  conduit.addHandler("foot_off", ([]() -> int { foot_servo.toggle(false, bed_switch_constant); }));
  conduit.addHandler("foot_stop", ([]() -> int { foot_servo.stop(); }));

  conduit.addHandler("head_massage_on", ([]() -> int { head_massage_servo.toggle(true, massage_switch_constant, massage_delay_milliseconds); }));
  conduit.addHandler("head_massage_off", ([]() -> int { head_massage_servo.toggle(false, massage_switch_constant, massage_delay_milliseconds); }));

  conduit.addHandler("foot_massage_on", ([]() -> int { foot_massage_servo.toggle(true, massage_switch_constant, massage_delay_milliseconds); }));
  conduit.addHandler("foot_massage_off", ([]() -> int { foot_massage_servo.toggle(false, massage_switch_constant, massage_delay_milliseconds); }));
}

void loop(void){
  conduit.handle();
}
