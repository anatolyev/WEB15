from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('', required=True, type=str)
parser.add_argument('', required=True, type=str)
parser.add_argument('', required=True, type=str)
