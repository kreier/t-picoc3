# Add Circuitpython support for LilyGO T-PicoC3

Steps to follow:

## Upload generic firmware

The Raspberry Pico firmware works out of the box, with the reset button down during power on the drive that appears is RP-BOOT. Drop the `firmware.uf2` into this drive and the firmware is installed!

## Get display to work

The regular rp2040 firmware works, but needs a dedicated driver for the display. With the firmware for the T-Display rp2040 the display works, but this firmware currently misses a PID to be published. And the RX, TX, CTS and RTS pins have to be assigned specifically. An independent build for the T-PicoC3 would be beneficial.

