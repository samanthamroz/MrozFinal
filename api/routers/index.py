from api.routers import orders, order_details, menu_items, customers, payments, promo_codes, reviews, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(menu_items.router)
    app.include_router(customers.router)
    app.include_router(payments.router)
    app.include_router(promo_codes.router)
    app.include_router(reviews.router)
    app.include_router(resources.router)