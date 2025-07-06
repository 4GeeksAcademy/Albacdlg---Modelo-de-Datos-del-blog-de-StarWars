from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    susbscription_date: Mapped[datetime] = mapped_column(
        default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_nem": self.last_name,
            "susbscription_date": self.susbscription_date.isoformat()
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    __tablename__ = 'planet'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(100))
    population: Mapped[str] = mapped_column(Integer)
    terrain: Mapped[str] = mapped_column(String(100))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain
        }


class Character(db.Model):
    __tablename__ = 'character'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    birth_year: Mapped[str] = mapped_column(String(20))
    gender: Mapped[str] = mapped_column(String(20))
    height: Mapped[int] = mapped_column(Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height
        }
