from apps import db, ma

class Home(db.Model):
    __tablename__ = 'users'  # set table

    id = db.Column(db.Integer, primary_key=True)
	
    def __init__(self, aData):
        self.name = aData['name']


class HomeSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name'
        )