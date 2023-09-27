import dtlpy as dl
dl.login()

#Accessing the project and dataset
project = dl.projects.get(project_id='ee06dd20-8c7e-4933-a67b-02b4de998a74')
dataset = project.datasets.get(dataset_name='new_dataset')


dataset.items.upload(local_path=r'C:/Users/asad.abbas/images_folder',
                     local_annotations_path=r'C:/Users/asad.abbas/json_folder_1')

#Creating a filter Query
my_filter_top = dl.Filters()
my_filter_top.add_join(field='label', values='top')


pages = dataset.items.list(filters=my_filter_top)
for item in pages.all():

    print('item name')
    print(item.name)

    print("item id")
    print(item.id)

