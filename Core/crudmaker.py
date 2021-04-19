import os
from django.apps import apps
    
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
App = 'Api'

class CrudMaker():
    if not os.path.exists(os.path.join(BASE_DIR,'graphql')):
        os.mkdir('graphql')

    models2 = [x._meta.model_name for x in apps.get_app_config(App).get_models()]
    
    
    
    print('**********')
    print(models2)
    print(os.path.join(BASE_DIR,'graphql'))
    print('**********')
