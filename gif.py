from moviepy.editor import *

start = 0.0
end = 10.0
width = 500
fps = 20
speedx = 2

file_in = "vid/vikas.avi"
file_out = "vid/img.gif"

clip = (VideoFileClip(file_in).subclip((0,start),(0,end)).resize(width=width))
clip.speedx(speedx).write_gif(file_out, fps=fps)