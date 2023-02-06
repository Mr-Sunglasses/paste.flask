from pastebin import db

class PasteBook(db.Model):

    __tablename__ = 'pastebooks'

    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Text)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"{self.id} and {self.data}"

