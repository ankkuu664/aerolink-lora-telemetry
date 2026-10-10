import machine,ssd1306,time
from machine import I2C,Pin,PWM
from sx1262 import SX1262

lr=PWM(8, freq=50000)
lg=PWM(7, freq=50000)
lb=PWM(9, freq=50000)

lr.duty_u16(65535)

sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=13, irq=14, rst=15, gpio=16)

# LoRa
sx.begin(freq=868, bw=250.0, sf=12, cr=5, syncWord=0x12,
         power=22, currentLimit=140.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)
lr.duty_u16(16384)
lb.duty_u16(65535)

i2c = I2C(0,sda=0, scl=1)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
led=Pin(25,Pin.OUT)



while True:
    while True:
        start=time.ticks_ms()
        msg, err = sx.recv()
        stop=time.ticks_ms()
        if len(msg) > 0:
            display.fill(0)
            led.toggle()
            lb.duty_u16(65535)
            error = SX1262.STATUS[err]
            print(msg)
            x = str(msg)
            p = sx.getRSSI()
            lb.duty_u16(0)
            display.text("RSSI "+str(p)+" dBi",0,2)
            display.show()
            print(stop-start)