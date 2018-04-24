from flask import Flask
from flask import render_template
from data_helper import get_senate, get_house



myapp = Flask(__name__)


@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html')
    return rawhtml

@myapp.route("/<chamber>/")
def members(chamber):
    if chamber == 'senate':
        members = get_senate()
    elif chamber == 'house':
        members = get_house()
    else:
        abort(404)

    rawhtml = render_template('members.html', members=members, chamber=chamber)
    return rawhtml

if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
