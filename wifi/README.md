# Connection between rp2040 and esp32c3

I would like to use the integrated [Circuitpython Web Workflow Code Editor](https://learn.adafruit.com/getting-started-with-web-workflow-using-the-code-editor) with my students. And the T-PicoC3 has an esp32c3 wifi module build in, connected over UART to the rp2040. Is it possible to get it to work? Or is a SPI connection necessary? A different firmware on the C3 could reconfigure the pins to work as SPI2 pins, but first things first.

- [Schematic T-PicoC3](https://github.com/Xinyuan-LilyGO/T-PicoC3/blob/main/Schematic/T-PicoC3.pdf)
- [Datasheet rp2040](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
- [Datasheet esp32c3](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)

## Pinmap rp

That's what I figured out from the documentation provided by LilyGO:

```
_______________  chip         chip  ___________________
rp2040  GPIO8  |- 11 -- TX  -- 12 -| MTCK  esp32c3  
        GPIO9  |- 12 -- RX  -- 13 -| MTDO
        GPIO10 |- 13 -- CTS --  9 -| MTMS
        GPIO11 |- 14 -- RTS -- 10 -| MTDI
_______________|          1 -- 15 -| IO9     10k to VCC
                          2 -- 14 -| IO8     10k to VCC
                          3 --  6 -| IO2
                          4 --  7 -| RST     10k to VCC
                                   |___________________
```

On the rp2040 side it uses pins 8, 9, 10 and 11. They are used by SPI1 as RX, CSn, SCK and TX. The display is connected on pin 0, 1, 2, 3, 4, 5 for RX, CSn, SCK, TX, RX and CSn of SPI0 (RST, DC, SCLK, MOSI, BL and CS). Display and wifi can work on different SPI busses.

The 10 kiloOhm resistors to VCC for pin IO8, IO9 and RST are part of the bootstrap setup to ensure correct boot sequence.

The protocol running is AT with 115200 bps. Not sure how the two other boards with attached Wifi module do it:

### Challenger

TBD.

### Raspberry Pi Pico W

TBD  
