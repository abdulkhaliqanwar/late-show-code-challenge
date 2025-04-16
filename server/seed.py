
from app import app
from models import db, Episode, Guest

with app.app_context():
    db.drop_all()
    db.create_all()

    e1 = Episode(date="1/11/99", number=1)
    e2 = Episode(date="1/12/99", number=2)

    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    g3 = Guest(name="Tracey Ullman", occupation="television actress")

    db.session.add_all([e1, e2, g1, g2, g3])
    db.session.commit()
