from flask import render_template_string, Blueprint
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(DIRECTORY, "templates/swagger-ui.html")


def render_swaggerui(swagger_spec_path, **kwargs):
    with open(TEMPLATE_PATH) as f:
        template_string = f.read()
    return render_template_string(
        template_string, swagger_spec_path=swagger_spec_path, **kwargs)


def build_static_blueprint(*args, **kwargs):
    kwargs['url_prefix'] = kwargs.get('url_prefix', "").rstrip("/") + \
                           "/swagger-ui"

    if 'static_folder' not in kwargs:
        kwargs['static_folder'] = os.path.join(DIRECTORY, "static/")

    return Blueprint(*args, **kwargs)
