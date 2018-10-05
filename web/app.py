from flask import Flask, render_template
from dbworker import IUBArchive

app = Flask(__name__, static_folder='static')
app.jinja_env.autoescape = False


@app.route('/')
def index():
    ## print generated query
    # import logging
    # logger = logging.getLogger('peewee')
    # logger.setLevel(logging.DEBUG)
    # logger.addHandler(logging.StreamHandler())

    filter =(IUBArchive.main_cpv_code == '80420000-4') | \
            (IUBArchive.main_cpv_code == '80513000-3') | \
            (IUBArchive.main_cpv_code.startswith('72')) | \
            (IUBArchive.main_cpv_code.startswith('302')) | \
            (IUBArchive.main_cpv_code.startswith('48')) | \
            (IUBArchive.main_cpv_code.startswith('503')) | \
            (IUBArchive.main_cpv_code.startswith('516')) | \
            (IUBArchive.main_cpv_code.startswith('642')) | \
            (IUBArchive.main_cpv_code.startswith('793')) | \
            (IUBArchive.main_cpv_code.startswith('80533'))

    data = IUBArchive.select().where(filter).order_by(IUBArchive.created_date.desc()) #.limit(100)
    return render_template('layout.html', andis="cirulis", data=data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
