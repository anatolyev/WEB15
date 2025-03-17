from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('title', required=True, type=str)
parser.add_argument('content', required=True, type=str)
parser.add_argument('is_private', required=True, type=str)
parser.add_argument('user_id', required=True, type=str)
# parser.add_argument('', required=True, type=str)
