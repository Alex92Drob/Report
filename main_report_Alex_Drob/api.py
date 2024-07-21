from flask import request, jsonify, Response, abort
from flask_restful import Resource
from flasgger.utils import swag_from
import dicttoxml
from main_report_Alex_Drob.models import RacingReport


class ReportData(Resource):
    @swag_from('swagger/report_data.yml')
    def get(self):
        format_request = request.args.get('format', 'json')
        table = []
        for racer in RacingReport:
            racer_info = {
                'place': racer.place,
                'abbr': racer.abbr,
                'name': racer.name,
                'car': racer.car,
                'time': racer.time
            }
            table.append(racer_info)

        if format_request == 'xml':
            xml_data = dicttoxml.dicttoxml(table, attr_type=False, custom_root='racers')
            return Response(xml_data, mimetype='application/xml')

        return jsonify(table)


class ReportDrivers(Resource):
    @swag_from('swagger/report_drivers.yml')
    def get(self):
        driver_id = request.args.get('driver_id')
        format_request = request.args.get('format', 'json')
        table = []
        if driver_id:
            if driver_id not in [racer.abbr for racer in RacingReport]:
                abort(404, 'Driver not found')
            else:
                for racer in RacingReport:
                    if racer.abbr == driver_id:
                        racer_info = {
                            'place': racer.place,
                            'abbr': racer.abbr,
                            'name': racer.name,
                            'car': racer.car,
                            'time': racer.time
                        }
                        table.append(racer_info)
                if format_request == 'xml':
                    xml_data = dicttoxml.dicttoxml(table, attr_type=False, custom_root='racers')
                    return Response(xml_data, mimetype='application/xml')

                return jsonify(table)

        for racer in RacingReport:
            racer_info = {
                'abbr': racer.abbr,
                'name': racer.name
            }
            table.append(racer_info)

        if format_request == 'xml':
            xml_data = dicttoxml.dicttoxml(table, attr_type=False, custom_root='racers')
            return Response(xml_data, mimetype='application/xml')

        return jsonify(table)
