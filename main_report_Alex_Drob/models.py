from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('monaco_racing_report.db')


class RacingReport(Model):
    place = CharField()
    abbr = CharField()
    name = CharField()
    car = CharField()
    time = CharField()

    class Meta:
        database = db
