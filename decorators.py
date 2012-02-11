#!/usr/bin/env python
from functools import wraps
from flask import request, Response

def throttle(rds=None, limit=50):
    def inner_throttle(f):
        def decorated(*args, **kwargs):
            if int(rds.get('visitors:{0}'.format(str(request.remote_addr)))) > limit:
                return Response('Over limit ; chill out', 420)
            return f(*args, **kwargs)
        return wraps(f)(decorated)
    return inner_throttle

