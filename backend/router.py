from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (create_product,
                  get_products,
                  get_product,
                  delete_product,
                  update_product
                  )

router = APIRouter()

@router.post("/products/", response_model= ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.get("/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_products_route(product_id:int , db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail= "Você esta procurando um produto que não existe")
    return db_product



@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    
    if product_db is None:

        raise HTTPException(status_code=404, detail= "Você esta tentando deletar um produto que não existe")
    return product_db
    

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    
    if product_db is None:

        raise HTTPException(status_code=404, detail= "Você esta tentando atualizar um produto que não existe")
    return product_db

    
