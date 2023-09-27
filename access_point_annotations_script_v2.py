import dtlpy as dl
dl.login()

#Accessing the project and dataset
project = dl.projects.get(project_id='ee06dd20-8c7e-4933-a67b-02b4de998a74')
dataset = project.datasets.get(dataset_name='new_dataset')


# Local path to the corresponding annotations - make sure the file names fit
local_annotations_path = r'C:/home/project/annotations_folder'

dataset.items.upload(local_path=r'C:/Users/asad.abbas/images_folder',
                     local_annotations_path=r'C:/Users/asad.abbas/json_folder_1')

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

