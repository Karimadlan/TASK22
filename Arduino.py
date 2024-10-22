import RPi.GPIO as GPIO
import time

# تحديد الدبابيس المستخدمة
TRIG = 12
ECHO = 11

# إعداد الدبابيس
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # إرسال نبضة قصيرة على دبوس TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # انتظار استقبال النبضة العائدة
    pulse_start = time.time()
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    # حساب المسافة
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

if __name__ == "__main__":
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # عند الضغط على Ctrl+C لإنهاء البرنامج
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()