# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/example', methods=['GET'])
def get_exa():
    response = Controller.get_example()
    return jsonify(data=response)

@api.route('/exampleadd', methods=['POST','GET'])
def post_exa():
    response = Controller.post_exmple()
    return jsonify(data=response)

@api.route('/exampleput/<int:exa_id>', methods=['PUT','GET'])
def put_exa(exa_id):    
    response = Controller.put_exmple(exa_id)
    return jsonify(data=response)

@api.route('/exampledel/<int:exa_id>', methods=['DELETE','GET'])
def delete_exa(exa_id):
    response = Controller.delete_exmple(exa_id)
    return jsonify(data=response)


