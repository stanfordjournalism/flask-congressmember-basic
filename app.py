from flask import Flask
from flask import render_template
from data_helper import get_chamber


myapp = Flask(__name__)


@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html')
    return rawhtml

###
# notice how I don't have a separate senate/ and house/ route, but
# I abstract it to a "chamber" route that spits out either Representatives or Senators
# based on the chamber argument (e.g. "senate" or "house")
###

@myapp.route("/<chamber>/")
def chamber(chamber):
    members = get_chamber(chamber)
    rawhtml = render_template('members.html', members=members, chamber=chamber)
    return rawhtml

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
