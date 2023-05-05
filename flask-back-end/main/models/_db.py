from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def save(data) -> None:
    db.session.add(data)
    db.session.commit()

def delete(data) -> None:
    db.session.delete(data)
    db.session.commit()