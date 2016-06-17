from flask import render_template_string, Blueprint, send_from_directory
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(DIRECTORY, "templates/swagger-ui.html")


def render_swaggerui(swagger_spec_path, static_prefix="/swagger-ui-static",
                     **kwargs):
    with open(TEMPLATE_PATH) as f:
        template_string = f.read()
    return render_template_string(
        template_string, swagger_spec_path=swagger_spec_path,
        static_prefix=static_prefix, **kwargs)


def build_static_blueprint(*args, **kwargs):
    #kwargs['url_prefix'] = kwargs.get('url_prefix', "").rstrip("/") + \
    #                       "/swagger-ui"

    bp = Blueprint(*args, **kwargs)

    @bp.route('/swagger-ui-static/<path:fn>')
    def swaggerui_static(fn):
        return send_from_directory(os.path.join(DIRECTORY, "static"), fn)

    return bp
