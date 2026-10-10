import machine
import _thread
from machine import I2C,Pin,PWM
from sx1262 import SX1262
import time
import ssd1306

sw=Pin(2,Pin.IN)

lr=PWM(8, freq=50000)
lg=PWM(7, freq=50000)
lb=PWM(9, freq=50000)

lr.duty_u16(65535)

sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=13, irq=14, rst=15, gpio=16)

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

lr.duty_u16(0)
lb.duty_u16(0)
display.text("Suraksha",0,2)
display.text("Kavach",0,10)
display.text("Initialising...",0,22)
display.show()
time.sleep(2)

x="lol"
led.value(0)
packets=1
while True:
    if sw.value()==1:
        lb.duty_u16(65535)
        display.text("Clear Triggered",0,2)
        sx.send(b'Stop')
        lb.duty_u16(0)
        time.sleep(1)
    else:
        msg, err = sx.recv()
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
            cap=x.split(",")
            display.text("Battery : {}.2f".format(cap[6]),0,18)
            display.text("RX Pkts : "+str(packets),0,34)
            display.text("Tx Pkts : "+str(cap[13]),0,50)
            display.show()
            packets=packets+1
        else :
            pass
