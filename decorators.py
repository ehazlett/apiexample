#!/usr/bin/env python
from functools import wraps
from flask import request, Response, json

def throttle(rds=None, limit=50):
    def inner_throttle(f):
        def decorated(*args, **kwargs):
            if int(rds.get('visitors:{0}'.format(str(request.remote_addr)))) > limit:
                data = {
                    'status': 'fail',
                    'response': 'Over limit ; try again later',
                }
                return Response(json.dumps(data, indent=2), 403)
            return f(*args, **kwargs)
        return wraps(f)(decorated)
    return inner_throttle

