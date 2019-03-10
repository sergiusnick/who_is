from flask import Flask, url_for, send_from_directory
import os

app = Flask(__name__)

directory = os.getcwd()
countDIR = str(len(os.listdir(directory + '/static')) - 1)
files = os.listdir(
    directory + '/static/' + str(len(os.listdir(directory + '/static')) - 1))


@app.route('/')
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
                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>            
                    <link rel="stylesheet" href="static/carousel.css">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                      <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                      </ol>
                      <div class="carousel-inner">'''
    text += '''<div class="carousel-item active">
                <img class="d-block" src="static/1/dimas.jpg" class="img-fluid" alt="Блин блинский">
            </div>'''

    for img in files:
        text += '''<div class="carousel-item">
                    <img class="d-block" src="{}" class="img-fluid" alt="Блин блинский">
                </div>
                        '''.format(url_for('static', filename=countDIR + '/' + img))
        print(countDIR + '/' + img)
                        # '''<div class="carousel-item active">
                        #   <img class="d-block w-100" src="static/1/dima_2.jpg" alt="First slide">
                        # </div>'''

    text += '''</div>
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

    return text


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')



    # for img in files:
    #     text += '''<div class="carousel-item">
    #                         <img class="d-block w-100" src="{}" alt="Блин блинский">
    #                     </div>
    #                     '''.format(
    #         url_for('static', filename=countDIR + '/' + img))
    #     print(countDIR + '/' + img)
