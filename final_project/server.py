import os
import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    txt_tran=translator.english_to_french(textToTranslate)
    return "Translated text to English=",txt_tran

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translator.french_to_english(textToTranslate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
    
    
