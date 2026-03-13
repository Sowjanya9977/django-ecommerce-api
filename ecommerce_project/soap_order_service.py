from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class OrderService(ServiceBase):

    orders = []

    @rpc(Integer, Integer, Integer, _returns=Unicode)
    def create_order(ctx, user_id, product_id, quantity):
        order = {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity
        }
        OrderService.orders.append(order)
        return "Order created successfully"

    @rpc(_returns=Unicode)
    def get_orders(ctx):
        return str(OrderService.orders)


application = Application(
    [OrderService],
    tns='ecommerce.soap.orders',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

if __name__ == "__main__":
    server = make_server('127.0.0.1', 9000, wsgi_application)
    print("SOAP server running at http://127.0.0.1:9000")
    server.serve_forever()