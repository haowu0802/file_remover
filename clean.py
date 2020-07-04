import os

from pathlib import Path

exts = ['*.gif', '*.js', 'js','*.css', '*.download', '*.png', '*.html']

for ext in exts:
    #for file in Path('../seeds').rglob(ext):
    for file in Path('../_tmp').rglob(ext):
        #print(file)
        os.remove(file)