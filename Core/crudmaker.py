import os
from django.apps import apps
    
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
App = 'Api'

class CrudMaker():
    destin = os.path.join(BASE_DIR,'graphql')
    if not os.path.exists(destin):
        os.mkdir('graphql')

    all_models = [x._meta.model_name for x in apps.get_app_config(App).get_models()]
    
    for model in all_models:
        ### READING THE QUERY TXT
        fr = open(os.path.join(destin,f'QueryBase.txt'), 'r')
        ### WRITING NEW QUERY FILE
        fw = open(os.path.join(destin,f'{model}.py'), 'w') 
        for line in fr.readlines():
            if line.__contains__('Base_'):
                line = line.replace('Base_', model)
            fw.write(line)
        fw.close()
        fr.close()