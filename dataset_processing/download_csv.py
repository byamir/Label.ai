import requests
import os

os.makedirs('./dataset_processing/csv/downloads/', exist_ok=True)

downloads = [
    {'path': './dataset_processing/csv/downloads/labels.csv', 'url': 'https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv'},
    {'path': './dataset_processing/csv/downloads/classifications.csv', 'url': 'https://storage.googleapis.com/openimages/v5/test-annotations-machine-imagelabels.csv'},
    {'path': './dataset_processing/csv/downloads/images.csv', 'url': 'https://storage.googleapis.com/openimages/2018_04/test/test-images-with-rotation.csv'},
]

for val in downloads:
    req = requests.get(val['url'])
    url_content = req.content
    csv_file = open(val['path'], 'wb')

    csv_file.write(url_content)
    csv_file.close()


# Prepend header to label-descriptions
with open('./dataset_processing/csv/downloads/labels.csv', 'r') as original: data = original.read()
with open('./dataset_processing/csv/downloads/labels.csv', 'w') as modified: modified.write('ID,Name\n' + data)
