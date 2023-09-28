import dtlpy as dl
dl.login()

#Accessing the project and dataset
project = dl.projects.get(project_id='ee06dd20-8c7e-4933-a67b-02b4de998a74')
dataset = project.datasets.get(dataset_name='new_dataset')


dataset.items.upload(local_path=r'C:/Users/asad.abbas/images_folder',
                     local_annotations_path=r'C:/Users/asad.abbas/json_folder_1')


# Python program to read
# json file

import json

# Opening JSON file
f = open(r'C:/Users/asad.abbas/json_folder_1/test_json_file_assessment.json')

# returns JSON object as
# a dictionary
data = json.load(f)

new_json={}
new_json_1={}

for key,val in data.items():
    new_annotations=[]
    for annotations in val:
        for k,v in annotations.items():
            if k=='label':
                new_json['label']=annotations[k]
            if k=='point':
                new_json['type']=k
                new_json['coordinates']=annotations[k]
        new_annotations.append(new_json)
    with open(r'C:/Users/asad.abbas/json_folder_2/'+key.replace(".jpg","")+'.json', "w") as outfile:
        json.dump({'annotations':new_annotations},outfile, indent=4)




project.datasets.upload_annotations(dataset=dataset,
                                     local_path=r'C:/Users/asad.abbas/json_folder_2/',
                                     clean=True,
                                     export_version=dl.ExportVersion.V1
                                     )


dataset.items.upload(local_path=r'C:/Users/asad.abbas/images_folder',
                     local_annotations_path=r'C:/Users/asad.abbas/json_folder_2',
                     overwrite=True)

#Creating a filter Query
my_filter_point = dl.Filters()
my_filter_point.add_join(field='label', values='point')


pages = dataset.items.list(filters=my_filter_point)
for item in pages.all():
    print("item id")
    print(item.id)

    print('item name')
    print(item.name)

filters = dl.Filters()
filters.resource = dl.FiltersResource.ANNOTATION
filters.add(field='label', values='point')

for annotation in dataset.annotations.list(filters=filters).all():

    print("annotation label")
    print(annotation.label)
    
    print('annotation id')
    print(annotation.id)

    print('annotation coordinates')
    print(annotation.coordinates)


