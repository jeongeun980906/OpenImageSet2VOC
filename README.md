# OpenImageSet2VOC

This repository is for preprocessing OpenImageSet Detection data to Pascal VOC format.

You can make VOC formatted detection dataset on OpenImage by specifying the class labels! :)

You can download annotation file and class names (.csv) from this [url](https://storage.googleapis.com/openimages/web/download.html#download_manually)

I edited class name files by adding id and name like this
```
id,name
/m/011k07,Tortoise
/m/011q46kg,Container
/m/012074,Magpie
/m/0120dh,Sea turtle
/m/01226z,Football
/m/012n7d,Ambulance
/m/012w5l,Ladder
```

### Dependencies
```
pandas
boto3
tqdm
imagesize
pascal_voc_writer
```

### Run

```
python make_set.py
```
This code makes set.txt file containing which image to download

```
python downloader.py set.txt --download_folder=[your path] --num_processes=5
```
This code download the images

```
python annot.py
```
Please change the ROOT path variable. This code makes the annotation file