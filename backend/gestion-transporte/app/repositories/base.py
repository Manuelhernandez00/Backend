"""Operaciones SQLAlchemy reutilizables para los repositorios."""
from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session

ModelT = TypeVar("ModelT")

class BaseRepository(Generic[ModelT]):
    """Encapsula operaciones comunes sin alterar la lógica de los endpoints."""
    def __init__(self, model: Type[ModelT]):
        self.model = model

    def get_by_id(self, db: Session, entity_id: int):
        return db.query(self.model).filter(self.model.id == entity_id).first()

    def list(self, db: Session, *, limit: int = 100, offset: int = 0):
        return db.query(self.model).offset(offset).limit(limit).all()

    def create(self, db: Session, values: dict):
        entity = self.model(**values)
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(self, db: Session, entity, values: dict):
        for key, value in values.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        db.commit()
        db.refresh(entity)
        return entity

    def delete(self, db: Session, entity):
        """Elimina físicamente; usar solo donde la política del dominio lo permita."""
        db.delete(entity)
        db.commit()
