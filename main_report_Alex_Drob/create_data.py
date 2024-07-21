from main_report_Alex_Drob.models import RacingReport, db
from main_report_Alex_Drob.main import build_report
from pathlib import Path

db.connect()
db.create_tables([RacingReport])


def files():
    data_folder = Path("../data")
    return [data_folder / "abbreviations.txt", data_folder / "end.log", data_folder / "start.log"]


report_info = build_report(paths=files())
for racer in report_info:
    RacingReport.create(place=racer['place'], abbr=racer['abbr'], name=racer['name'], car=racer['car'],
                        time=str(racer['time']))

db.close()
