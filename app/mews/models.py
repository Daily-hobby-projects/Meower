from . import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Mew(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(),nullable=True)
    content=db.Column(db.Text(),nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class MewSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Mew
        sqla_session=db.session

    id=fields.Integer()
    name=fields.String()
    content=fields.String()
        