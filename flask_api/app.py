from flask import Flask, jsonify, request
import spacy
from benepar.spacy_plugin import BeneparComponent
nlp = spacy.load("en_core_web_lg")
nlp.add_pipe(BeneparComponent("benepar_en2"))
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/spacy_doc",methods=["POST"])
def users_api():
    text = request.form["text"]
    output = nlp(text).to_bytes()
    return output