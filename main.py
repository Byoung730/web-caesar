from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
    <!DOCTYPE html>

    <html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    
    <body>
      <h1 style='text-align:center'>Web Caesar</h1>
      <form action="/converted", method=['GET']>
      <label for = "rot">Rotate by how many spots?</label>
      <input id="rot" type="text" name="rot" />
      <textarea id="text1" placeholder="Enter text here"></textarea>
      <input type="submit" value="Convert">
    </form></body>
</html>
"""


@app.route("/")
def index():
    return form


converted_form = """
  <!DOCTYPE html>

    <html>
    <head>
        <h1>Converted Text</h1>
    </head>
    <body>
        <---something--->
    </body>
    </html>
"""

@app.route("/converted", methods=['GET'])
def encrypt():
    text1 = request.form['form']
    rotation = 'rot'
    text_to_convert1 = 'text1'

    converted_text = rotate_string(text1, rot)
    print (converted_text)

    return converted_form

app.run()