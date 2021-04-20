import os
from django.apps import apps

App = 'Api'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(BASE_DIR,App)

# Get All Django Models
all_models = [x.__name__ for x in apps.get_app_config(App).get_models()]
exclude_fields = ['id', 'datacriacao','dataatualizacao', 'data_criacao', 'data_atualizacao', 'date_joined'
                #   'refresh_tokens', 'user_permis', 'logentry', 'ruas', 'provincias', 'cidades', 'municipios',
                  ]


class CrudMaker():
    graphql_path = os.path.join(APP_DIR,'graphql')
    query_path = os.path.join(graphql_path,'query')
    mutation_path = os.path.join(graphql_path,'mutation')
    base_path = os.path.join(BASE_DIR,'Base')
    
    # Creating Directories : graphql, query, mutation
    if not os.path.exists(graphql_path):
        os.makedirs(os.path.join(graphql_path, 'query'))
        os.makedirs(os.path.join(graphql_path, 'mutation'))
        
        with open(os.path.join(graphql_path, f'__init__.py'), 'w') as fw: pass
        
        with open(os.path.join(base_path, f'BaseSchema.txt'), 'r') as fr:
            ### WRITING NEW QUERY FILE
            with open(os.path.join(graphql_path, 'schema.py'), 'w') as fw:
                for line in fr.readlines():
                    fw.write(line)

    ## ============================== QUERY ==============================    
    list_import = []
    list_class = ['class Query(ObjectType):\n',]

    for model in all_models:
        list_import.append(f'from .{model} import {model}Type \n')        

        list_class.append(f'\t{model.lower()} = CustomNode.Field({model}Type) \n')
        list_class.append(f'\tall_{model.lower()} = DjangoFilterConnectionField({model}Type) \n\n')
        
        # Verify if the current file already exist
        if not os.path.exists(os.path.join(query_path, f'{model}.py')):
            ### READING THE QUERY TXT
            with open(os.path.join(base_path, f'BaseQuery.txt'), 'r') as fr:
                ### WRITING NEW QUERY FILE
                with open(os.path.join(query_path, f'{model}.py'), 'w') as fw: 
                    for line in fr.readlines():
                        if line.__contains__('Base_'):
                            line = line.replace('Base_', model)
                        fw.write(line)
        
    # Writing __init__.py for queries
    with open(os.path.join(query_path, f'__init__.py'), 'w') as fw: 
        fw.write('from graphene import ObjectType \n')
        fw.write('from Core.utils import CustomNode \n')
        fw.write('from graphene_django.filter import DjangoFilterConnectionField \n')
        fw.write('\n')
        
        for line in list_import:
            fw.write(line)
        
        fw.write('\n\n')
        
        for line in list_class:
            fw.write(line)

        fw.write('\n')
        list_class.clear()
        list_import.clear()
        
    # ============================== MUTATIONS  ==============================
    list_import = []
    list_class = ['class Mutation(ObjectType):\n',]

    for model in all_models:
        list_import.append(f'from .{model} import {model}Mutation, Remove{model} \n')  

        list_class.append(f'\t{model.lower()} = {model}Mutation.Field() \n')
        list_class.append(f'\tremove_{model.lower()} = Remove{model}.Field() \n\n')
        
         # Verify if the current file already exist
        if not os.path.exists(os.path.join(mutation_path, f'{model}.py')):
            ### READING THE MUTATION TXT
            with open(os.path.join(base_path, f'BaseMutation.txt'), 'r') as fr:
                ### WRITING NEW MUTATION FILE
                with open(os.path.join(mutation_path, f'{model}.py'), 'w') as fw: 
                    for line in fr.readlines():
                        if line.__contains__('Base_'):
                            line = line.replace('Base_', model)
                        elif line.__contains__('pass_fields_'):
                            takedModel = apps.get_model(App, model)
                            # field = [field.name for field in takedModel._meta.get_fields()]
                            field = sorted([field.name for field in takedModel._meta.concrete_fields])
                            
                            # Removing exclude_fields
                            for item in exclude_fields:
                                if field.__contains__(item):
                                    field.remove(item)

                            line = line.replace('pass_fields_', f'fields = {field}')
                        fw.write(line)

    # Writing __init__.py for mutations
    with open(os.path.join(mutation_path, f'__init__.py'), 'w') as fw:
        fw.write('from graphene import ObjectType\n')
        fw.write('\n')
        
        for line in list_import:
            fw.write(line)
        
        fw.write('\n\n')
        
        for line in list_class:
            fw.write(line)

        list_class.clear()
        list_import.clear()

class CrudMaker1(object):
    def __init__(self, app_name):
        super(CrudMaker1, self).__init__()
        self.app_name = app_name
        self.create_queries()
        self.create_mutations()
    
    def create_queries(self):
        print(f'You called Create queries in {self.app_name} application')
        
        
    def create_mutations(self):
        print('You called Create mutations')
    
    