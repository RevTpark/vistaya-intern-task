from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SlotData(db.Model):
    __tablename__ = "slots"
    slot_time = db.Column(db.Integer, nullable=False, primary_key=True)
    slot_one = db.Column(db.String, nullable=True)
    slot_two = db.Column(db.String, nullable=True)

