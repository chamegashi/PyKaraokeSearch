from PyKaraokeSearch.joysound.JoySoundSearchQueryField import Match
from flask import Flask, jsonify, request

from PyKaraokeSearch import search_joysound, JoySoundSearchQuery, make_joysound_responce
from PyKaraokeSearch import JoySoundSearchQueryField as QF
from PyKaraokeSearch import search_clubdam, ClubDamSearchQuery, make_clubDam_responce

from GetKeyRange import keySearch

app = Flask(__name__)

@app.route('/api/search', methods=['GET'])
def search_keyword():
	if request.method == 'GET':
		keyword = request.args.get('keyword')

		if not keyword:
			return jsonify({"status": "error", "message": "なんか文字入れて"})


		joyResult = search_joysound(JoySoundSearchQuery(
			filters=[
				QF.Filter(
					kind='compound',
					word=word,
					match="partial",
				)
				for word in keyword.split(" ")
			]
		))
		joyResponce = make_joysound_responce(joyResult)

		damResult = search_clubdam(ClubDamSearchQuery(keyword=keyword))
		damResponce = make_clubDam_responce(damResult)

		return jsonify({"damResponce" : damResponce, "joyResponce": joyResponce, "status": "ok"})
	else:
		return jsonify({"status": "error", "message": "POST やん..."})

@app.route('/api/getKey', methods={'GET'})
def get_key():
	if request.method == 'GET':
		keywords = request.args.get('keywords')
		if not keywords:
			return jsonify({"status": "error", "message": "なんか文字入れて"})
		
		res = keySearch.searchKey(keywords)

		return jsonify({"data" : res, "status": "ok"})
	else:
		return jsonify({"status": "error", "message": "POST やん..."})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
	app.run(debug=True)

