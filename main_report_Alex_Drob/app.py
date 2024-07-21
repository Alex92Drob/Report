from flasgger import Swagger
from flask import Flask, render_template, request, abort, redirect
from flask_restful import Api
from main_report_Alex_Drob.api import ReportData, ReportDrivers
from main_report_Alex_Drob.models import RacingReport

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


@app.route("/")
def index():
    return redirect("/report")


@app.route('/report')
def homepage():
    order = request.args.get('order', 'asc')
    if order == 'desc':
        return render_template('homepage.html', report=RacingReport.select().order_by(-RacingReport.id))
    return render_template('homepage.html', report=RacingReport)


@app.route('/report/drivers')
def drivers():
    driver_id = request.args.get('driver_id')
    if driver_id:
        if driver_id not in [racer.abbr for racer in RacingReport]:
            abort(404, 'Driver not found')
        else:
            for racer in RacingReport:
                if racer.abbr == driver_id:
                    return render_template('driver_info.html', racer=racer)

    return render_template('drivers.html', report=RacingReport, request=request)


api.add_resource(ReportData, '/api/v1/report/')
api.add_resource(ReportDrivers, '/api/v1/drivers/')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='localhost')
