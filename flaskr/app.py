#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import sys
import subprocess as sp

def run_cmd(cmd, val):
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


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/brightness/<jsdata>')
def get_brightness(jsdata):
    print("Brightness: " + jsdata, file=sys.stdout)
    run_cmd('brightness', jsdata)
    return jsonify(success=True)

@app.route('/contrast/<jsdata>')
def get_contrast(jsdata):
    print("Contrast: " + jsdata, file=sys.stdout)
    run_cmd('contrast', jsdata)
    return jsonify(success=True)

@app.route('/saturation/<jsdata>')
def get_saturation(jsdata):
    print("Saturation: " + jsdata, file=sys.stdout)
    run_cmd('saturation', jsdata)
    return jsonify(success=True)

@app.route('/autofocus/<jsdata>')
def get_autofocus(jsdata):
    print("Auto Focus: " + jsdata, file=sys.stdout)
    run_cmd('autofocus', jsdata)
    return jsonify(success=True)

@app.route('/fixedfocus/<jsdata>')
def get_fixedfocus(jsdata):
    print("Fixed Focus: " + jsdata, file=sys.stdout)
    run_cmd('fixedfocus', jsdata)
    return jsonify(success=True)

