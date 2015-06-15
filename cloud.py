# coding: utf-8

from leancloud import Engine

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return u'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'
