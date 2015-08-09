

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import signal
import threading
import subprocess
import os
from flask import Flask, request, redirect, url_for


#!/usr/bin/env python
import sys
import RPi.GPIO as GPIO
import time
import Image 
import ImageOps
import ImageStat
import threading

def led_print(filename):
        row = [ 7, 11, 12, 13, 15, 16, 18, 22]
            col = [29, 31, 32, 33, 35, 36, 37, 38]

                source_image = Image.open(filename)
                    gray_image = ImageOps.grayscale(source_image)

                        stat = ImageStat.Stat(gray_image)
                            width, height = gray_image.size

                                mean = stat.mean[0]
                                    for i in range(width):
                                                for j in range(height):
                                                                value = gray_image.getpixel((i,j))
                                                                            if int(mean) > value:
                                                                                                gray_image.putpixel((i, j), 0)
                                                                                                            else:
                                                                                                                                gray_image.putpixel((i, j), 255)

                                                                                                                                    dot_image = gray_image.resize((8, 8))
                                                                                                                                        dot_image.save('dot.png')

                                                                                                                                            GPIO.setmode(GPIO.BOARD)

                                                                                                                                                for pin in row:
                                                                                                                                                            GPIO.setup(pin, GPIO.OUT)

                                                                                                                                                                for pin in col:
                                                                                                                                                                            GPIO.setup(pin, GPIO.OUT)
                                                                                                                                                                                global stop_event
                                                                                                                                                                                    print "looping"
                                                                                                                                                                                        stop_event.clear()
                                                                                                                                                                                            while not stop_event.is_set():
                                                                                                                                                                                                        print filename
                                                                                                                                                                                                                for i in range(8):
                                                                                                                                                                                                                                GPIO.output(row[i], True)
                                                                                                                                                                                                                                            for j in range(8):
                                                                                                                                                                                                                                                                value = dot_image.getpixel((j, i))
                                                                                                                                                                                                                                                                                if value == 255:
                                                                                                                                                                                                                                                                                                        GPIO.output(col[j], False)
                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                GPIO.output(col[j], True)
                                                                                                                                                                                                                                                                                                                                                            time.sleep(0.001)
                                                                                                                                                                                                                                                                                                                                                                        GPIO.output(row[i], False)
                                                                                                                                                                                                                                                                                                                                                                                time.sleep(0.01)
                                                                                                                                                                                                                                                                                                                                                                                filename = ""
                                                                                                                                                                                                                                                                                                                                                                                stop_event = threading.Event()

# signal habdler
def signal_handler(num, stack):
        print 'Received signal %d in %s' % (num, threading.currentThread())
            return

        def send_signal():
                print 'Sending signal in', threading.currentThread()
                    os.kill(os.getpid(), signal.SIGUSR1)


                    def wait_for_signal():
                            global filename
                                #cmd = "sudo python matrix.py %s" % (filename)
                                    #subprocess.call( cmd.strip().split(" ")  ) 
                                        global stop_event
                                            #while not stop_event.is_set():
                                                led_print(filename)

                                                def stop():
                                                        global stop_event
                                                            stop_event.set()

                                                            UPLOAD_FOLDER = '/home/pi/fun-fan/flask'
                                                            ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

                                                            app = Flask(__name__)

                                                            sender = threading.Thread(target=send_signal, name='sender')

                                                            flag = False

                                                            def allowed_file(filename):
                                                                    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

                                                                @app.route('/', methods=['GET', 'POST'])
                                                                def upload_file():
                                                                        if request.method == 'POST':
                                                                                    file = request.files['file']
                                                                                            if file and allowed_file(file.filename):
                                                                                                            global filename
                                                                                                                        filename = file.filename
                                                                                                                                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                                                                                                                                                print filename           
                                                                                                                                                            global flag
                                                                                                                                                                        if flag == True:
                                                                                                                                                                                            # kill
                                                                                                                                                                                                            # sender.start()
                                                                                                                                                                                                                            stop()

                                                                                                                                                                                                                                            receiver = threading.Thread(target=wait_for_signal, name='receiver')
                                                                                                                                                                                                                                                            receiver.start()

                                                                                                                                                                                                                                                                        else: 
                                                                                                                                                                                                                                                                                            receiver = threading.Thread(target=wait_for_signal, name='receiver')
                                                                                                                                                                                                                                                                                                            receiver.start()

                                                                                                                                                                                                                                                                                                                            flag = True

                                                                                                                                                                                                                                                                                                                                return '''                                                                                         <!doctype html>
                                                                                                                                                                                                                                                                                                                                    <title>Upload new File</title>
                                                                                                                                                                                                                                                                                                                                        <h1>Upload new File</h1>
                                                                                                                                                                                                                                                                                                                                            <form action="" method=post enctype=multipart/form-data>
                                                                                                                                                                                                                                                                                                                                                <p><input type=file name=file>
                                                                                                                                                                                                                                                                                                                                                    <input type=submit value=Upload>
                                                                                                                                                                                                                                                                                                                                                        </form>
                                                                                                                                                                                                                                                                                                                                                            '''

                                                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                    app.run('0.0.0.0', debug=True)#!/usr/bin/env python
# -*- coding: utf-8 -*-


                                                                                                                                                                                                                                                                                                                                                                    import signal
                                                                                                                                                                                                                                                                                                                                                                    import threading
                                                                                                                                                                                                                                                                                                                                                                    import subprocess
                                                                                                                                                                                                                                                                                                                                                                    import os
                                                                                                                                                                                                                                                                                                                                                                    from flask import Flask, request, redirect, url_for


#!/usr/bin/env python
import sys
import RPi.GPIO as GPIO
import time
import Image 
import ImageOps
import ImageStat
import threading

def led_print(filename):
        row = [ 7, 11, 12, 13, 15, 16, 18, 22]
            col = [29, 31, 32, 33, 35, 36, 37, 38]

                source_image = Image.open(filename)
                    gray_image = ImageOps.grayscale(source_image)

                        stat = ImageStat.Stat(gray_image)
                            width, height = gray_image.size

                                mean = stat.mean[0]
                                    for i in range(width):
                                                for j in range(height):
                                                                value = gray_image.getpixel((i,j))
                                                                            if int(mean) > value:
                                                                                                gray_image.putpixel((i, j), 0)
                                                                                                            else:
                                                                                                                                gray_image.putpixel((i, j), 255)

                                                                                                                                    dot_image = gray_image.resize((8, 8))
                                                                                                                                        dot_image.save('dot.png')

                                                                                                                                            GPIO.setmode(GPIO.BOARD)

                                                                                                                                                for pin in row:
                                                                                                                                                            GPIO.setup(pin, GPIO.OUT)

                                                                                                                                                                for pin in col:
                                                                                                                                                                            GPIO.setup(pin, GPIO.OUT)
                                                                                                                                                                                global stop_event
                                                                                                                                                                                    print "looping"
                                                                                                                                                                                        stop_event.clear()
                                                                                                                                                                                            while not stop_event.is_set():
                                                                                                                                                                                                        print filename
                                                                                                                                                                                                                for i in range(8):
                                                                                                                                                                                                                                GPIO.output(row[i], True)
                                                                                                                                                                                                                                            for j in range(8):
                                                                                                                                                                                                                                                                value = dot_image.getpixel((j, i))
                                                                                                                                                                                                                                                                                if value == 255:
                                                                                                                                                                                                                                                                                                        GPIO.output(col[j], False)
                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                GPIO.output(col[j], True)
                                                                                                                                                                                                                                                                                                                                                            time.sleep(0.001)
                                                                                                                                                                                                                                                                                                                                                                        GPIO.output(row[i], False)
                                                                                                                                                                                                                                                                                                                                                                                time.sleep(0.01)
                                                                                                                                                                                                                                                                                                                                                                                filename = ""
                                                                                                                                                                                                                                                                                                                                                                                stop_event = threading.Event()

# signal habdler
def signal_handler(num, stack):
        print 'Received signal %d in %s' % (num, threading.currentThread())
            return

        def send_signal():
                print 'Sending signal in', threading.currentThread()
                    os.kill(os.getpid(), signal.SIGUSR1)


                    def wait_for_signal():
                            global filename
                                #cmd = "sudo python matrix.py %s" % (filename)
                                    #subprocess.call( cmd.strip().split(" ")  ) 
                                        global stop_event
                                            #while not stop_event.is_set():
                                                led_print(filename)

                                                def stop():
                                                        global stop_event
                                                            stop_event.set()

                                                            UPLOAD_FOLDER = '/home/pi/fun-fan/flask'
                                                            ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

                                                            app = Flask(__name__)

                                                            sender = threading.Thread(target=send_signal, name='sender')

                                                            flag = False

                                                            def allowed_file(filename):
                                                                    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

                                                                @app.route('/', methods=['GET', 'POST'])
                                                                def upload_file():
                                                                        if request.method == 'POST':
                                                                                    file = request.files['file']
                                                                                            if file and allowed_file(file.filename):
                                                                                                            global filename
                                                                                                                        filename = file.filename
                                                                                                                                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                                                                                                                                                print filename           
                                                                                                                                                            global flag
                                                                                                                                                                        if flag == True:
                                                                                                                                                                                            # kill
                                                                                                                                                                                                            # sender.start()
                                                                                                                                                                                                                            stop()

                                                                                                                                                                                                                                            receiver = threading.Thread(target=wait_for_signal, name='receiver')
                                                                                                                                                                                                                                                            receiver.start()

                                                                                                                                                                                                                                                                        else: 
                                                                                                                                                                                                                                                                                            receiver = threading.Thread(target=wait_for_signal, name='receiver')
                                                                                                                                                                                                                                                                                                            receiver.start()

                                                                                                                                                                                                                                                                                                                            flag = True

                                                                                                                                                                                                                                                                                                                                return '''                                                                                         <!doctype html>
                                                                                                                                                                                                                                                                                                                                    <title>Upload new File</title>
                                                                                                                                                                                                                                                                                                                                        <h1>Upload new File</h1>
                                                                                                                                                                                                                                                                                                                                            <form action="" method=post enctype=multipart/form-data>
                                                                                                                                                                                                                                                                                                                                                <p><input type=file name=file>
                                                                                                                                                                                                                                                                                                                                                    <input type=submit value=Upload>
                                                                                                                                                                                                                                                                                                                                                        </form>
                                                                                                                                                                                                                                                                                                                                                            '''

                                                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                    app.run('0.0.0.0', debug=True)
