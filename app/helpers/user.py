from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from app.database import get_db, SessionLocal
from app.models import User


def get_user(id: int, db: Session = SessionLocal()):
    user = db.query(User).filter(User.id == id).first()
    return user


def get_users(db: Session = SessionLocal()):
    users = db.query(User).all()
    return users


def add_user(name, email, password, db: Session = SessionLocal()):
    user = User(name=name, email=email, password=password)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(id: int, updated: dict, db: Session = SessionLocal()):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(
            f"No user with this Id", status_code=status.HTTP_404_NOT_FOUND
        )
    user_query.update(updated)
    db.commit()
    return user_query.first()


def delete_user(id: int, db: Session = SessionLocal()):
    user_query = db.query(User).filter(User.id == id)
    user = user_query.first()
    if not user:
        raise HTTPException(
            f"No user with this Id", status_code=status.HTTP_404_NOT_FOUND
        )
    user_query.delete()
    db.commit()
    return True
