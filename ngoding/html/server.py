import tornado.websocket
import uuid
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

clients = {}
class EchoWSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket dibuka")
        self.id = uuid.uuid4()
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}

    def on_message(self, message):
        self.write_message("Kamu bilang: " + message)
        for client in clients:
            print (clients[client])
            target = clients[client]
            target['object'].write_message( str(self.id) + ": " + message)

    def on_close(self):
        print("WebSocket ditutup")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/messenger", EchoWSHandler),
    ])

    application.listen(8889)
    tornado.ioloop.IOLoop.current().start()
