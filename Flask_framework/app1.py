
from flask import Flask, jsonify, request
# working with api
# put and delete

app =Flask(__name__)

items =[
    {"id": 1, "task": "Study", "Description":"DSA"},
    {"id": 2, "task": "Playing", "Description":"Cricket"},

]



@app.route("/")
def home():
    return "Welcome to the To Do App"

# GET REQUEST
@app.route("/get")
def getitems():

    return jsonify(items)

@app.route("/get/<itemnumber>", methods =["GET"])
def getitem(itemnumber):
    item =None
    for item in items:
        if str(item["id"])==itemnumber:
            return jsonify(item)
    return jsonify({"error": "Not Found"})
    

# Post --> Creating a new item
@app.route("/items", methods =["POST"])
def create_item():
    if not request.json or not "task" in request.json:
        return jsonify({"error": "There is some error"})
    else:
        new_item ={"id": items[-1] + 1 if items else 1,
                   "task": request.json["task"],
                   "Description": request.json["Description"]}
        items.append(new_item)
        
    
if __name__=="__main__":
    app.run(debug=True)