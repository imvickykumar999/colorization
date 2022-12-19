
# step 1
# video into frame

# # https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames/33399711#33399711

# import cv2
# vidcap = cv2.VideoCapture('vid/oldsong.mp4')
# success,image = vidcap.read()
# count = 0

# while success:
#   cv2.imwrite(f"vid_out/{str(count).zfill(6)}.jpg", image)     # save frame as JPEG file      
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1

# ---------------------------------

# step 2
# # python video_colorization.py -i input.jpg -o output.jpg

import argparse, os
import matplotlib.pyplot as plt
from colorizers import *

def magic(input_path, output_path):
	parser = argparse.ArgumentParser()
	parser.add_argument('--use_gpu', action='store_true', help='whether to use GPU')
	opt = parser.parse_args()

	colorizer_eccv16 = eccv16(pretrained=True).eval()
	colorizer_siggraph17 = siggraph17(pretrained=True).eval()
	if(opt.use_gpu):
		colorizer_eccv16.cuda()
		colorizer_siggraph17.cuda()

	img = load_img(input_path)
	(tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
	if(opt.use_gpu):
		tens_l_rs = tens_l_rs.cuda()

	img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig), dim=1))
	out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
	plt.imsave(output_path, out_img_eccv16)

	# out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())
	# plt.imsave(output_path, out_img_siggraph17)



images = [img for img in os.listdir('vid_out')
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]

# for i in images:
# 	magic(f'vid_out/{i}', f'bw_vid_out/{i}')


# ------------------------------

# step 3
# merge frame into video

# https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/

# from PIL import Image

# # print(os.getcwd())
# os.chdir(r"C:\Users\Vicky\Desktop\Repository\colorization\bw_vid_out")
# path = r"C:\Users\Vicky\Desktop\Repository\colorization\bw_vid_out"

# mean_height = 0
# mean_width = 0

# num_of_images = len(os.listdir('.'))
# # print(num_of_images)

# for file in os.listdir('.'):
# 	im = Image.open(os.path.join(path, file))
# 	width, height = im.size
# 	mean_width += width
# 	mean_height += height

# mean_width = int(mean_width / num_of_images)
# mean_height = int(mean_height / num_of_images)

# for file in os.listdir('.'):
# 	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
# 		im = Image.open(os.path.join(path, file))

# 		width, height = im.size
# 		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
# 		imResize.save( file, 'JPEG', quality = 95)
# 		print(im.filename.split('\\')[-1], " is resized")

# def generate_video():
# 	image_folder = r'C:\Users\Vicky\Desktop\Repository\colorization\bw_vid_out'
# 	video_name = 'mygeneratedvideo.avi'
# 	os.chdir(r"C:\Users\Vicky\Desktop\Repository\colorization\bw_vid_out")
	
# 	images = [img for img in os.listdir(image_folder)
# 			if img.endswith(".jpg") or
# 				img.endswith(".jpeg") or
# 				img.endswith("png")]
	
# 	frame = cv2.imread(os.path.join(image_folder, images[0]))
# 	height, width, layers = frame.shape
# 	video = cv2.VideoWriter(video_name, 0, 1, (width, height))

# 	for image in images:
# 		video.write(cv2.imread(os.path.join(image_folder, image)))
	
# 	cv2.destroyAllWindows()
# 	video.release()

# generate_video()

# -----------------------------------

# waiting 

# import time
# print("Print now")
# time.sleep(2)
# print("Printing after 2 seconds")

# ----------------------------------------

# move file

# os.replace("bw_vid_out/mygeneratedvideo.avi", "vid/mygeneratedvideo.avi")

# ---------------------------------

# video speed change

# https://stackoverflow.com/questions/63631973/how-can-i-use-python-to-speed-up-a-video-without-dropping-frames/63632689#63632689

# from moviepy.editor import VideoFileClip, AudioFileClip
# import moviepy.video.fx.all as vfx

# in_loc = 'vid/mygeneratedvideo.avi'
# out_loc = 'vid/dummy_out.mp4'

# # Import video clip
# clip = VideoFileClip(in_loc)
# print("fps: {}".format(clip.fps))

# # Modify the FPS
# clip = clip.set_fps(clip.fps * 3)

# # Apply speed up
# final = clip.fx(vfx.speedx, 25)
# print("fps: {}".format(final.fps))

# # getting only first 5 seconds
# # clip = clip.subclip(0, 5)

# # https://zulko.github.io/moviepy/getting_started/audioclips.html
# # loading audio file
# audioclip = AudioFileClip("vid/oldsong.mp4")

# # adding audio to the video clip
# videoclip = final.set_audio(audioclip)

# # showing video clip
# # videoclip.ipython_display()

# # Save video clip
# videoclip.write_videofile(out_loc)
