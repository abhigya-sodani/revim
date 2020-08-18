from flask import Flask
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
# I # Engine, a webserver process such as Gunicorn will serve the app. Thispp
# c # can be configured by adding an `entrypoint` to app.yaml.
app app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'
