# Leggett & Platt Cloud Connected Remote

This device is a cloud connected via [conduit v1](https://github.com/suyashkumar/conduit) and ESP8266 remote control which automatically raises the head lift of the bed at the set alarm time.

The exact remote used is pictured here: ![alt text][logo]
[remote_picture]: https://github.com/ouwen/remote/blob/master/documentation/remote.jpg "remote picture"

### Hardware
Two servo mounts can be found in `./hardware` as a `.stl` file. These can be 3d printed.
One is pressfit, the other must be glued or screwed onto a board.

The box to store the remote can be lasercut for a press fit as the `pressfit_box.svg`

The servos used are SG90 microservos and can be bought [here](https://www.amazon.com/TowerPro-SG90-Micro-Servo-2pk/dp/B01608II3Q)

### Firmware
Rename `info.sample.h` to `info.h` and fill out the relevant constants.

### Software
TODO

### License 
Copyright (c) 2018 Ouwen Huang
See [LICENSE](https://github.com/ouwen/remote/blob/master/LICENSE) for license text (MIT LICENSE)
