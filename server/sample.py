import falcon

class QuoteResource:
    def on_get(self, req, resp):
        quote = {
            'author': 'Grace Hopper',
            'quote': {
                "I've"
            },
        }

        resp.media = quote

app = falcon.App()
app.add_route('/quote', QuoteResource())
