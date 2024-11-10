from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

engine = create_engine("sqlite:///./product.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)

Base.metadata.create_all(engine)


class Function:
    def add_product(self, product_id, name, price, description, category):
        session = SessionLocal()

        try:
            new_product = Product(product_id=product_id, name=name, price=price, description=description, category=category)
            session.add(new_product)
            session.commit()

        except Exception as e:
            session.rollback()
            print(f'error adding new product: {e}')

        finally:
            session.close()

    def remove_product(self, product_id):
        session = SessionLocal()

        try:
            product_to_remove = session.query(Product).filter_by(product_id=product_id).first()
            session.delete(product_to_remove)
            session.commit()

        except Exception as e:
            session.rollback()
            print(f'error removing a product: {e}')

        finally:
            session.close()

    def get_product(self, product_id):
        session = SessionLocal()

        try:
            product_to_get = session.query(Product).filter_by(product_id=product_id).first()
            if product_to_get:
                return product_to_get
            else:
                return None

        except Exception as e:
            session.rollback()
            print(f'error getting a product: {e}')

        finally:
            session.close()