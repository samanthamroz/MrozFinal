from api.models import orders, order_details, recipes, reviews, menu_items, resources, payments, customers, promo_codes

from api.dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promo_codes.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)