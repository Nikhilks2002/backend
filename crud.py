from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_transaction(db: Session, transaction_id: str):
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_tx = models.Transaction(id=transaction.id, amount=transaction.amount, currency=transaction.currency)
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx

def mark_processed(db: Session, transaction_id: str):
    tx = get_transaction(db, transaction_id)
    if tx:
        tx.processed = True
        tx.processed_at = datetime.utcnow()
        db.commit()
        db.refresh(tx)
    return tx
