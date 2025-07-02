from flask import request, jsonify, Blueprint
from openai import OpenAI
import requests
from ..config.settings import Config as settings

client = OpenAI(
  api_key=settings.API_KEY,
)
travel_bp = Blueprint('travel', __name__)

@travel_bp.route('/travel', methods=['POST'])
def travel():
  try:
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "user", "content": f"Plan a trip from {start} to {end}."}
      ]
    )
    return jsonify({
      "from": start,
      "to": end,
      "trip_plan": response.choices[0].message.content
    }), 200
  
  except requests.exceptions.RequestException as e:
    return jsonify({"error": "Failed to connect to OpenAI API"}), 500
  except Exception as e:
    return jsonify({"error": "Invalid JSON format"}), 400