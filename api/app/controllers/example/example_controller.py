# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################
from flask_restful import reqparse,abort
from flask import request
from app.exception import InternalServerError
from app.models import ExampleModel
from app import db
from app.models import BaseModel

task_post_args = reqparse.RequestParser()
task_post_args.add_argument('name', type=str, help='name requerido', required=True)
task_post_args.add_argument('identification', type=str, help='identificacion requerido', required=True)
task_post_args.add_argument('description', type=str, help='descripcion requerido', required=True)
task_post_args.add_argument('status', type=int, help='status requerido', required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument('name', type=str)
task_put_args.add_argument('identification', type=str)
task_put_args.add_argument('description', type=str)
task_put_args.add_argument('status', type=int)


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_example():
        sql = ExampleModel.query.all()
        example = {}

        for data in sql:
            example[data.id] = {"nombre":data.name, "identificacion":data.identification,
                                "descripcion":data.description, "status":data.status}
        
        return example
    
    @staticmethod
    def post_exmple():
        args = task_post_args.parse_args()
       
        v = ExampleModel(name=args['name'], identification=args['identification'],description=args['description'],status=args['status'])
        BaseModel.save(v)
        dat = ExampleModel.export_data(v)

        return dat
    
    @staticmethod
    def put_exmple(exa_id):
        args = task_put_args.parse_args()
        sql = ExampleModel.query.filter_by(id=exa_id).first()
        
        if not sql:
            abort('error id no existe')
        
        if args['name']:
            sql.name =args['name']        
        if args['identification']:
            sql.identification =args['identification']
        if args['description']:
            sql.description =args['description']
        if args['status']:
            sql.status =args['status']        
        
        BaseModel.update(sql)        
        dat = ExampleModel.export_data(sql)
        return dat

    @staticmethod
    def delete_exmple(exa_id):
        sql = ExampleModel.query.filter_by(id=exa_id).first()

        if not sql:
            abort('error id no existe')
            
        BaseModel.delete(sql)        
        
        return "Elemento Eliminado",204

    

