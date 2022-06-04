import os


imageids = []
with open('set.txt','r') as f:
    while True:
        a = f.readline()
        if a == '':
            break
        a = a.split('/')[1]
        a = a.split('\n')[0]
        imageids.append(a)
images = os.listdir("/data/jeongeun/openimage/JPEGImages/")
images = [image.split('.')[0] for image in images]

imageids = set(imageids)
images = set(images)
print(len(images),len(imageids))
elements = imageids-images

with open("set2.txt",'w') as f:
    for e in elements:
        f.write("train/"+str(e)+"\n")