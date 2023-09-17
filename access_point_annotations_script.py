import dtlpy as dl
dl.login()

#Accessing the project and dataset
project = dl.projects.get(project_id='ee06dd20-8c7e-4933-a67b-02b4de998a74')
dataset = project.datasets.get(dataset_name='new_dataset')

#Acessing the images that have point annotation as per the JSON file
item_1 = dataset.items.get(item_id='6506cc2a3d477e676885cc42')
item_2= dataset.items.get(item_id='6506cc2b37f286c0a97dab28')

builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Point(x=173.6123972734067, y= 201.27956683881678, label='point'))
builder.add(annotation_definition=dl.Point(x=174.66143334966824, y=116.00264757387058, label='point'))
item_1.annotations.upload(builder)

builder = item_2.annotations.builder()
builder.add(annotation_definition=dl.Point(x= 173.6123972734067, y=201.27956683881678, label='point'))
builder.add(annotation_definition=dl.Point(x= 123.74583031836863, y=162.94832356737442, label='point'))
item_2.annotations.upload(builder)

#Creating a filter Query
my_filter_top = dl.Filters()
my_filter_top.add_join(field='label', values='point')


pages = dataset.items.list(filters=my_filter_top)
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
