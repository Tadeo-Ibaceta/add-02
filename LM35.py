from machine import ADC
from time import sleep

adc = ADC(27)
 
while 1 != 3:
    
    val = adc.read_u16()
    
    val = 3.3 * val / 65535
    
    T = val * 1 / 0.01
    
    print ("El valor de temperatura es: {:.2f}".format(T))
    sleep(.5)


    
    