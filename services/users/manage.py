# services/users/manage.py


import sys

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.users.models import User
from project.api.users.models import Location
from datetime import datetime 



app = create_app()
cli = FlaskGroup(create_app=create_app)


from project.api.users.views import main
app.register_blueprint(main)






@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(username="bob", email="bobdog@gmail.com", password="supersecret"))
    db.session.add(User(username="bobdog", email="bob@goodpups.org", password="supersecret"))
    db.session.add(Location(lat="30.99999", lng="-120.93999"))
    db.session.commit()


if __name__ == "__main__":
    cli()
