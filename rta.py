import sys
import subprocess

def install(package):
    print("Install", package)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_reqModules():
    try:
        with open('requirementModule.txt') as f:
            requirements = f.read().splitlines()
            
        for r in requirements:
            print("Inatall ", r)
            install(r)
    except FileNotFoundError:
        print("There is not 'requirementModule.txt'")

#check_reqModules()

#try:
#    import cv2
#except ModuleNotFoundError:
#    install ('opencv-python')
#    import cv2

try:
    import pandas as pd
except ModuleNotFoundError:
    install ('pandas')
    import pandas

try:
    import openpyxl
except ModuleNotFoundError:
    install ('openpyxl')
    import openpyxl

try:
    import ffmpeg
except ModuleNotFoundError:
    install ('ffmpeg')
    import ffmpeg


def extractVideoInfo(videoPath):
    try:
        probe = ffmpeg.probe(videoPath)
        videoStream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        
        if videoStream is None:
            return None
        
        return {
            'fileName': os.path.basename(videoPath),
            'fps': videoStream['r_frame_rage'],
            'width': videoStream['widht'],
            'height': videoStream['height'],
            'tsd': videoStream.get('tags', {}).get('pkt_dts_time'),
            'psd': videoStream.get('tags', {}).get('pkt_psd_time')
        }
    except Exception as e:
        print(f"Error processing {videoPath}: {e}")
        return None


