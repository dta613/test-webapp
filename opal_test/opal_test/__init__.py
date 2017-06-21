"""
opal_test - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'opal_test.schema'
    flow_module   = 'opal_test.flow'
    javascripts   = [
        'js/opal_test/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/opal_test/flow.js',
    ]