from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def process_form():
    print(request.form)
    return render_template("show_form.html", name=request.form["name"], loc=request.form["location_select"], lang=request.form["lang_select"], comments=request.form["comments"])
    
if __name__ == "__main__":
    app.run(debug=True)
