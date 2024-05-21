from flask import Flask, render_template
import json

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
data = [{
  "Team": "Pittsburgh Pirates",
  "Wins": "76",
  "Mascot": "Parrot"
},
 {
  "Team": "Philadelphia Phillies",
  "Wins": "75",
  "Mascot": "Philly Phanatic"
}, {
  "Team": "Chicago Cubs",
  "Wins": "40",
  "Mascot": "Bear Cub"
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "Team", # which is the field's name of data key 
    "title": "Team", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "Wins",
    "title": "Wins",
    "sortable": True,
  },
  {
    "field": "Mascot",
    "title": "Mascot",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table - With Teams')


if __name__ == '__main__':
	#print jdata
    app.run(debug=True, host="0.0.0.0", port=5000)


