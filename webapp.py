import streamlit as st
import time
import numpy as np
import os
import tempfile
import random

st.write("## Hello Please Upload")
file = st.file_uploader('File uploader')

if st.button("Detect Now") and file:
	with st.spinner('Wait for it...'):
		tfile = tempfile.NamedTemporaryFile(dir="tempvideos",delete=False)
		tfile.write(file.read())
		st.write(tfile.name)
		outputdarknetFile = "tempvideo"+str(random.randint(1, 100))+".avi"
		outputFile = "tempvideo"+str(random.randint(1, 100))+".mp4"
		st.write("Upload Completed ! Hang Tight")
		os.system(f"python darknet_video.py --input={tfile.name} --ext_output --out_filename={outputdarknetFile} --weights=mask_detection.weights --config_file yolov4_custom_test.cfg --data=cfg/coco.data --dont_show")
		#print(dir(file))
		st.write("Video Processed... Converting Now to Web Format")
		os.system(f"ffmpeg -y -i {outputdarknetFile} -vcodec libx264 {outputFile}")
		st.video(outputFile)
		print(outputFile)
# Streamlit widgets automat