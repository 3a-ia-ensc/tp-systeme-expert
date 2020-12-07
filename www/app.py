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

from src.main import initialize_akinn

app = Flask(__name__)
akinn = initialize_akinn()


@app.route('/')
def index():
    """Index endpoint
    """
    return render_template('index.html')


@app.route('/knowledge_database')
def knowledge():
    """Display the knowledge of the system
    """
    return render_template('knowledge.html',
                           nb_rules=len(akinn.rules),
                           rules=akinn.rules,
                           nb_facts=len(akinn.facts),
                           facts=akinn.facts)


@app.route('/api/forward')
def forward_checking():
    """Forward checking
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
