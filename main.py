from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True



form = """
    <!DOCTYPE html>

    <html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    
    <body>
      <h1 style='text-align:center'>Web Caesar</h1>
      <form method = "post" action = "/converted">
    
      <label for = "rot">Rotate by how many spots?</label>
      <input id="rot" type="text" name="rot" value=0 />
      <textarea name="text">{0}</textarea>
      <input type="submit" value="Convert">
    </form></body>
</html>
"""

@app.route("/")
def index():
    

    blank = ''

    return form.format(blank)




@app.route("/converted", methods=['POST'])
def encrypt():
    text2 = request.form['text']
    rot2 = request.form['rot']

    #if not rot.is_integer():
    #   error message
    #

    converted_text = rotate_string(text2, rot2)





    #sentence = "Your encoded text is: " + converted_text

    return form.format(converted_text)

app.run()