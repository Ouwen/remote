# Leggett & Platt Cloud Connected Remote

Have you ever wanted the luxury of being forced out of bed at a certain time automatically? I certainly did.

This device is a cloud connected (via [conduit v1](https://github.com/suyashkumar/conduit)) ESP8266 chip which automatically raises the head of your Leggett & Platt bed at the set alarm time allowing the user to feel very uncomfortable.

The exact remote used is pictured [here](https://github.com/ouwen/remote/blob/master/documentation/remote.jpg): 

### Hardware
![alt text](https://github.com/ouwen/remote/blob/master/documentation/remote_click.gif "yes this is jank")

Two servo mounts can be found in `./hardware` as a `.stl` file. These can be 3d printed.
One is pressfit, the other must be glued or screwed onto a board.

The box to store the remote can be lasercut for a press fit as the `pressfit_box.svg`

The servos used are SG90 microservos and can be bought [here](https://www.amazon.com/TowerPro-SG90-Micro-Servo-2pk/dp/B01608II3Q)

### Firmware
Rename `info.sample.h` to `info.h` and fill out the relevant constants.
Run the following commands after connecting your ESP8266 microcontroller

```
  git clone https://github.com/Ouwen/remote.git
  cd firmware
  pio run
  pio run --target="upload"
```

### Software
 - TODO

### License 
Copyright (c) 2018 Ouwen Huang
See [LICENSE](https://github.com/ouwen/remote/blob/master/LICENSE) for license text (MIT LICENSE)
