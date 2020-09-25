import eel

import tkinter as tk
from tkinter import filedialog

from PIL import Image

import os

root = tk.Tk()
root.withdraw() # without tkinter window

file = '' # path to a file

@eel.expose
def open_file():
	global file

	file = filedialog.askopenfilename(initialdir = '/')
	expansion = str(file).split('.')

	if file.endswith('.jpg') or file.endswith('.gif') or file.endswith('.png'):
		photo = Image.open(str(file))

		copy = photo.copy()
		copy.save(f'web/media/this.{expansion[-1]}')

		return f'media/this.{expansion[-1]}'

@eel.expose
def left_right(side):
	global file

	path = str(file).split('/')
	filename = path[-1]

	del path[-1]

	data = os.listdir('/'.join(path))

	for f in data:
		if f == filename:
			if side == 'right':
				if data.index(f) >= len(data) - 1:
					filename = data[0]
				else:
					filename = data[data.index(f) + 1]
			else:
				if data.index(f) <= 0:
					filename = data[len(data) - 1]
				else:
					filename = data[data.index(f) - 1]
			break

	path = file = '/'.join(path) + '/' + filename

	expansion = str(path).split('.')

	photo = Image.open(str(path))

	copy = photo.copy()
	copy.save(f'web/media/this.{expansion[-1]}')

	return f'media/this.{expansion[-1]}'


eel.init("web")
eel.start("index.html", size = (1200, 720))
