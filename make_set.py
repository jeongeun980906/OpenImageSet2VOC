import pandas as pd
import json
class_dis = pd.read_csv('class.csv')

landmark_names = ['Shelf','Chest of drawers','Kitchen & dining room table','Coffee table','Table','Desk','Gas stove','Chair', #'Person',
        'Sink', 'Couch','Bottle', 'Sofa bed', 'Bed', 'Bookcase','Refrigerator','Piano','Television','Toilet','Cabinetry']
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
count = dict()
image_num = 0
for l in landmark_names:
    count[l]=0
with open("set.txt",'w') as w:
    for i in df.index:
        iid = df['ImageID'][i]
        lname = df['LabelName'][i]
        if lname in lids:
            if iid not in imageids:
                imageids.append(iid)
                count[class_dict[lname]]+=1
                image_num +=1
        if i % 100000==0 and i!=0:
            print(i)
            for imageid in imageids:
                string = "train/" + str(imageid) + "\n"
                w.write(string)
            imageids = [imageids[-1]]

count['total'] = image_num
with open('data.json','w') as jf:
    json.dump(count,jf,indent=4)