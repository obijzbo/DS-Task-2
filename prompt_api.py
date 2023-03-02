from flask import Flask, request, jsonify
from gpt_prompt import get_recommended_fruits

app = Flask(__name__)

@app.route("/")
def home():
    return "API Working"

@app.route('/recommend-fruits', methods=['POST'])
def recommend_fruits():
    data = request.get_json()
    recommended_fruits = get_recommended_fruits(party_on_weekends=data['party'], flavor=data['flavors'], disliked_texture=data['texture'], price_range=data['price'])
    return jsonify({'recommended_fruits': recommended_fruits})

if __name__ == '__main__':
    app.run(debug=True)