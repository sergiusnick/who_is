from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    text = '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width,
                        initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                        crossorigin="anonymous">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Привет, Яндекс!</h1>
                        <div class="alert alert-primary" role="alert">
                          А мы тут компонентами Bootstrap балуемся
                        </div>
                        
                        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                          <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                          </ol>
                          <div class="carousel-inner">'''
          for img in files:
            '''<div class="carousel-item active">
              <img class="d-block w-100" src="{}" alt="First slide">
            </div>'''.format(url_for('static', filename=img))

                          ''''</div>
                          <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                        
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')