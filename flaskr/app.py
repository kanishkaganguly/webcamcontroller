#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import sys
import subprocess as sp

def set_camera_settings(cmd, val):
    run_string = "v4l2-ctl -d /dev/video0 --set-ctrl="
    if "brightness" in cmd:
        run_string += f"brightness={val}"
    elif "contrast" in cmd:
        run_string += f"contrast={val}"
    elif "saturation" in cmd:
        run_string += f"saturation={val}"
    elif "autofocus" in cmd:
        run_string += f"focus_auto={'1' if val == 'true' else '0'}"
    elif "fixedfocus" in cmd:
        run_string += f"focus_absolute={val}"
    
    print(f"Command: {run_string}", file=sys.stdout)
    sp.run(run_string, shell=True)

def get_camera_details():
    run_string = "v4l2-ctl --list-devices"
    print(f"Command: {run_string}", file=sys.stdout)
    proc = sp.Popen(run_string, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    out, err = proc.communicate()
    details = out.decode().split('\n')
    cam_name = details[0].split(' (')[0]
    cam_devs = []
    for items in details[1:]:
        cam_devs.append(items.replace('\t', '')) if items != '' else None
    print(cam_name, file=sys.stdout)
    print(cam_devs, file=sys.stdout)
    return cam_name, cam_devs
    

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/brightness/<jsdata>')
def get_brightness(jsdata):
    print("Brightness: " + jsdata, file=sys.stdout)
    set_camera_settings('brightness', jsdata)
    return jsonify(success=True)

@app.route('/contrast/<jsdata>')
def get_contrast(jsdata):
    print("Contrast: " + jsdata, file=sys.stdout)
    set_camera_settings('contrast', jsdata)
    return jsonify(success=True)

@app.route('/saturation/<jsdata>')
def get_saturation(jsdata):
    print("Saturation: " + jsdata, file=sys.stdout)
    set_camera_settings('saturation', jsdata)
    return jsonify(success=True)

@app.route('/autofocus/<jsdata>')
def get_autofocus(jsdata):
    print("Auto Focus: " + jsdata, file=sys.stdout)
    set_camera_settings('autofocus', jsdata)
    return jsonify(success=True)

@app.route('/fixedfocus/<jsdata>')
def get_fixedfocus(jsdata):
    print("Fixed Focus: " + jsdata, file=sys.stdout)
    set_camera_settings('fixedfocus', jsdata)
    return jsonify(success=True)

@app.route('/camera/devices')
def get_devices():
    cam_name, cam_devs = get_camera_details()
    return jsonify(success=True, cam_name=cam_name, cam_devs=cam_devs)