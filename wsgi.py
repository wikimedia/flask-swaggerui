from flask import Flask, jsonify

from flask_swaggerui import render_swaggerui, build_static_blueprint

app = Flask(__name__)


@app.route('/')
def root():
    return render_swaggerui(swagger_spec_path="/spec")


@app.route('/spec')
def spec():
    return jsonify({"some swagger": "spec stuff"})


# Adds static assets for swagger-ui to path
app.register_blueprint(build_static_blueprint("swaggerui", __name__))

if __name__ == "__main__":
    app.run(port=8080, debug=True)
