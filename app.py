from ice_breaker import ice_break
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_url = ice_break(name=name)
    return jsonify(
        {
            "summry": person_info.summary,
            "interest": person_info.topic_of_interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breakers,
            "picture_url": profile_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
