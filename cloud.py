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


@engine.define
def editobj(**params):
    from leancloud import Object
    TestObject = Object.extend('TestObject')
    from leancloud import Query
    query = Query(TestObject)
    testObject = query.get('557fd90ee4b0d02dc2e3e342')
    testObject.set('foo', 'edit')
    testObject.save()

