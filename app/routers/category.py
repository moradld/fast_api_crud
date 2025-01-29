from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud.category import get_category, create_category
from app.schemas.category import Category, CategoryCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories/", response_model=Category)
def create_category_route(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category