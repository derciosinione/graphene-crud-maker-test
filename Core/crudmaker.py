import os
from django.apps import apps
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
App = 'Api'

class CrudMaker():
    graphql_path = os.path.join(BASE_DIR,'graphql')
    query_path = os.path.join(graphql_path,'query')
    mutation_path = os.path.join(graphql_path,'mutation')
    base_path = os.path.join(BASE_DIR,'Base')
    
    
    if not os.path.exists(graphql_path):
        os.makedirs(os.path.join('graphql','query'))
        os.makedirs(os.path.join('graphql','mutation'))
        fw = open(os.path.join(query_path, f'__init__.py'), 'w')
        fw.close()
        fw = open(os.path.join(mutation_path, f'__init__.py'), 'w')
        fw.close()
        fw = open(os.path.join(graphql_path, f'__init__.py'), 'w')
        fw.close()
        
        fr = open(os.path.join(base_path, f'BaseSchema.txt'), 'r')
        ### WRITING NEW QUERY FILE
        fw = open(os.path.join(graphql_path, 'schema.py'), 'w') 
        for line in fr.readlines():
            # if line.__contains__('Base_'):
            #     line = line.replace('Base_', model)
            fw.write(line)
        fw.close()
        fr.close()

        
    # Get All Django Models
    all_models = [x._meta.model_name for x in apps.get_app_config(App).get_models()]
    
        
    for model in all_models:
        ### READING THE QUERY TXT
        fr = open(os.path.join(base_path, f'QueryBase.txt'), 'r')
        ### WRITING NEW QUERY FILE
        fw = open(os.path.join(query_path, f'{model}.txt'), 'w') 
        # fw = open(os.path.join(query_path, f'{model}.py'), 'w') 
        for line in fr.readlines():
            if line.__contains__('Base_'):
                line = line.replace('Base_', model)
            fw.write(line)
        fw.close()
        fr.close()