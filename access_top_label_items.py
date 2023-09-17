import dtlpy as dl
dl.login()

#Accessing the project and dataset
project = dl.projects.get(project_id='ee06dd20-8c7e-4933-a67b-02b4de998a74')
dataset = project.datasets.get(dataset_name='new_dataset')
dataset.add_label(label_name='top')

#Acessing the images that have label top as per the Json file
item_1 = dataset.items.get(item_id='6506cc2a3d477e676885cc42')

builder = item_1.annotations.builder()

builder.add(annotation_definition=dl.Classification(label='top'))
item_1.annotations.upload(builder)

item_2 = dataset.items.get(item_id='6506cc2b37f286c0a97dab28')

builder = item_1.annotations.builder()

builder.add(annotation_definition=dl.Classification(label='top'))
item_2.annotations.upload(builder)

#Creating a filter Query
my_filter_top = dl.Filters()
my_filter_top.add_join(field='label', values='top')


pages = dataset.items.list(filters=my_filter_top)
for item in pages.all():
    print("item id")
    print(item.id)

    print('item name')
    print(item.name)