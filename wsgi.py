import os
import connexion
from openapi_server import encoder


_here = os.path.dirname(os.path.abspath(__file__))
_spec_dir = os.path.join(_here, 'openapi_server', 'openapi')

app = connexion.App(__name__, specification_dir=_spec_dir)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Swagger Petstore - OpenAPI 3.0'},
            pythonic_params=True)

application = app

if __name__ == '__main__':
    application.run(port=8080)
