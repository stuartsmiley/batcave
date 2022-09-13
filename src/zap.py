from flask import Flask
import RPi.GPIO as GPIO
import time
app = Flask(__name__)

@app.route("/batcave/zap")
def triggerDoor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    GPIO.cleanup()
    return "<h1 style='color:blue'>Batcave Activated</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')