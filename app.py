from flask import Flask
import flask
import os
import platform

framework_version= flask.__version__
runtime_version = platform.python_version()
app = Flask(__name__)

config_key = "TEST_INT_VALUE"
secret_key = "SAMPLE_SECRET"
secret_key2 = "SAMPLE_SECRET2"

if secret_key in os.environ:
    secrets = os.environ['SAMPLE_SECRET']
else:
    secrets= "No secrets from Secret manager were found"

if secret_key2 in os.environ:
    secrets2 = os.environ['SAMPLE_SECRET2']
else:
    secrets2= "No secret from parameter store were found"
    
    
if config_key in os.environ:
    configs = os.environ['TEST_INT_VALUE']
else:
    configs= "No configs were found"


@app.route("/")
def hello():
    return """Hello From AMNIC !!<br/>
              python_version : {0}<br/>  
              flask_version :{1}<br/>
              secrets : {2}<br/>
              secrets : {3}<br/>
              configs : {4}<br/>
                """.format(runtime_version,framework_version,secrets,secrets2,configs)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
