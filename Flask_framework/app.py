from flask import Flask, render_template, request, redirect, url_for

# Will createn instance of flask class which is WSGI App
# Giving __name__ as entry point of flask app
app =Flask(__name__)
# Jinja 2 template engine 
'''
1. {{}}
2. {%..%} cond
3. {#..#} For comments

'''


# route for root utl
@app.route("/")
def welcome():
    return "Faiq Imran DS csnc audhadb"

@app.route("/index")
def ind():
    # This will redirect to index.html placed within template folder
    return render_template("index.html")



@app.route("/form", methods =["GET", "POST"])
def forms():
    if request.method=="GET":
        return render_template("form_.html")
    else:
        name =request.form["name"]
        age =request.form["age"]
        return f'Name:{name}\n Age: {age} '

    
    

# Variabe rule by default type is str use <int: age> to change type
@app.route("/showname/<name>")
def showname(name):
    return name



# {{}}
@app.route("/result/<int:score>")
def result(score):
    res =""
    if score>=50:
        res ="PASS"
    else:
        res ="Fail"


    # Sending Data to html page
    return render_template("results.html", results =res)


# using dict {{% %}}
@app.route("/result1/<int:score>")
def result1(score):
    res =""
    if score>=50:
        res ="PASS"
    else:
        res ="Fail"

    dict ={"score": score, "result": res}

    # Sending Data to html page
    return render_template("results1.html", results =dict)


# using if cond {{% %}}
@app.route("/result2/<int:score>")
def result2(score):


    # Sending Data to html page
    return render_template("result2.html", results =score)

# building dynamic url
@app.route("/subjects", methods =["GET", "POST"])
def subject():
    if request.method=="GET":
        return render_template("subjects.html")
    else:
        eng =int(request.form["english"])
        urdu =int(request.form["urdu"])
        math =int(request.form["math"])
        tot =(eng+math+urdu)/3
        return redirect(url_for("result1",score =tot))

if __name__=="__main__":
    # debug=True restart the server if you will make change
    app.run(debug =True)