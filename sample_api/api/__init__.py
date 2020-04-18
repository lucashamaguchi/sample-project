from flask_restplus import Api, reqparse
from werkzeug.exceptions import HTTPException
import json
import datetime

api = Api(version='0.0.1', default='hello_world', title='Sample API', description='API to help people')


parser_auth = reqparse.RequestParser()
parser_auth.add_argument('Authorization', location='headers', required=True)


@api.errorhandler
def default_error_handler(e):
    if isinstance(e, HTTPException):
        print(e.get_response())
        response = {'message': e.description}
        status_code = e.code
    else:
        response = {'message': 'Unhandled Exception'}
        status_code = 500

    return response, status_code


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    data_s = json.dumps(data, cls=DateTimeEncoder)
    data_d = json.loads(data_s)
    resp = Api().make_response(data_d, code, fallback_mediatype='application/json')
    resp.headers.extend(headers or {})
    return resp
