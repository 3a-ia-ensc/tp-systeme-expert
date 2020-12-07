# -*- coding: utf-8 -*-

""" app.py
Create a web app
"""
from json import dumps

from flask import Flask, request, jsonify, render_template, Response

__author__ = "Simon Audrix and Gabriel Nativel-Fontaine"
__credits__ = ["Simon Audrix", "Gabriel Nativel-Fontaine"]
__copyright__ = "Copyright 2020}, TP représentation des connaissances"
__license__ = "WTFPL"
__version__ = "1.0.0"
__email__ = "gnativ910e@ensc.fr"
__status__ = "Development"


app = Flask(__name__)


@app.route('/')
def get_docs():
    """Index endpoint
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)