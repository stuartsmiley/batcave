from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
app = Flask(__name__,
            static_url_path='',
            static_folder='html')


@app.route("/batcave/zap")
def triggerDoor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    GPIO.cleanup()
    return render_template('activated.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')