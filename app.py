from flask import Flask, request, jsonify
from schemas import ParamsListSchema
from marshmallow import ValidationError

from utils import build_query

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        params = ParamsListSchema().load(request.json)
    except ValidationError as ex:
        return ex.messages, '400'

    result = None

    for query in params["queries"]:
        result = build_query(cmd=query["cmd"], param=query["value"], data=result)

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(port=14000)
