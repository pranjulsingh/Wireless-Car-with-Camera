#!/usr/bin/env python
# Author: Pranjul Singh
# Date: 15, October, 2017
# Time: 01:02 am

from flask import Flask, render_template, Response, request, url_for, redirect
from camera import Camera
from command import command
from db_init import Database


app = Flask(__name__)


@app.route('/reqTest/', methods=["GET", "POST"])
def reqTest():
    cd = command()
    device = request.args.get('device', '')
    direction = request.args.get('value', '')
    print device
    print direction
    return request.args.get('value', 'none')


@app.route('/dircontrol', methods=["GET", "POST"])
def dirControl():
    device = request.args.get('device', '')
    direction = request.args.get('value', '')
    db = Database()
    db.database_connect()
    db.update_direction(device, direction)
    db.close_connection()
    print device
    print direction
    return request.args.get('value', 'none')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        # yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')
        ak = bytes('--frame\r\n' + 'Content-Type: image/jpeg\r\n\r\n' + frame + '\r\n')
        yield (ak)


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
