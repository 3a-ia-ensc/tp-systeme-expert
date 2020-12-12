# -*- coding: utf-8 -*-

""" app.py
Create a web app
"""
from json import dumps

from flask import Flask, request, render_template

__author__ = "Simon Audrix and Gabriel Nativel-Fontaine"
__credits__ = ["Simon Audrix", "Gabriel Nativel-Fontaine"]
__copyright__ = "Copyright 2020}, TP représentation des connaissances"
__license__ = "WTFPL"
__version__ = "1.0.0"
__email__ = "gnativ910e@ensc.fr"
__status__ = "Development"

from src.main import initialize_akinn, Fact


app = Flask(__name__,
            template_folder="www/templates",
            static_folder="www/static")
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


@app.route('/api/forward', methods=['POST'])
def forward_checking():
    """Forward checking
    """
    print(request.form.get('reconstruction'))
    facts = [
        Fact(request.form.get('input')),
        Fact(request.form.get('action')),
        Fact(request.form.get('label')),
        Fact(request.form.get('reconstruction'))
    ]
    neural_net_expertise, biblio = akinn.ForwardChaining(facts)

    result = []
    for nn in neural_net_expertise:
        result.append(nn.to_json())

    bibliography = []
    for bb in biblio:
        bibliography.append(bb.to_json())

    to_send = dumps({'result': result, 'bibliography': bibliography})

    response = app.response_class(response=to_send,
                                  status=200,
                                  mimetype='application/json')

    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    app.run(debug=True)
