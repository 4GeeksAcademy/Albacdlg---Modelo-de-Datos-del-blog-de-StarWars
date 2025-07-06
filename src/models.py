from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
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
    favorites: Mapped[list["Favorite"]] = relationship(
        'Favorite', back_populates='user')

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
    favorites: Mapped[list["Favorite"]] = relationship(
        'Favorite', back_populates='planet')

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
    favorites: Mapped[list["Favorite"]] = relationship(
        'Favorite', back_populates='character')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height
        }


class Favorite(db.Model):
    __tablename__ = 'favorite'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planet_id: Mapped[int] = mapped_column(
        ForeignKey('planet.id'), nullable=True)
    character_id: Mapped[int] = mapped_column(
        ForeignKey('character.id'), nullable=True)

    # Relaciones
    user: Mapped["User"] = relationship('User', back_populates='favorites')
    planet: Mapped["Planet"] = relationship(
        'Planet', back_populates='favorites')
    character: Mapped["Character"] = relationship(
        'Character', back_populates='favorites')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }
