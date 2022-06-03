import pandas as pd
import imagesize
from pascal_voc_writer import Writer

class_dis = pd.read_csv('class.csv')
landmark_names = ['Shelf','Chest of drawers','Kitchen & dining room table','Coffee table','Table','Desk','Gas stove','Chair','Person',
        'Sink', 'Couch','Door', 'Sofa bed', 'Bed', 'Bookcase','Refrigerator','Piano','Television','Toilet','Cabinetry']
print(len(landmark_names))

class_dict = {}
lids = []
for i in class_dis.index:
    name = class_dis['name'][i]
    indx = class_dis['id'][i]
    if name in landmark_names:
        class_dict[indx] = name
        lids.append(indx)
print(class_dict)

df = pd.read_csv('annotation_train.csv')

imageids = []
with open('set.txt','r') as f:
    while True:
        a = f.readline()
        if a == '':
            break
        a = a.split('/')[1]
        a = a.split('\n')[0]
        imageids.append(a)

ROOT = '/data/jeongeun/openimage'
for imageid in imageids:
    path = '{}/JPEGImages/{}.jpg'.format(ROOT, imageid)
    width, height = imagesize.get(path)
    annots = df.loc[df['ImageID']==imageid]
    writer = Writer(path, width, height)
    for i in annots.index:
        label = annots['LabelName'][i]
        if label in lids:
            label = class_dict[label]
            Xmin = int(width*annots['XMin'][i])
            Xmax = int(width*annots['XMax'][i])
            Ymin = int(height*annots['YMin'][i])
            Ymax = int(height*annots['YMax'][i])
            writer.addObject(label, Xmin, Ymin, Xmax, Ymax)
    writer.save('{}/Annotations/{}.xml'.format(ROOT,imageid))
    # writer.save('img.xml')

SET = ROOT +'/ImageSets/Main/train.txt'
with open(SET,'w') as f:
    for imageid in imageids:
        f.writelines(imageid+'\n')