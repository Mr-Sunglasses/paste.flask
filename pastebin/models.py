from pastebin import db

class Bin(db.Model):

    __tablename__ = "pastebinpys"

    id: int = db.Column(db.Integer, primary_key = True )
    content: str = db.Column(db.Text)

    def __init__(self, content) -> None:
        self.content = content
    
    def __repr__(self) -> str:
        return f"{self.content}"