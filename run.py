from PyKaraokeSearch.joysound.JoySoundSearchQueryField import Match
from flask import Flask, jsonify, request

from PyKaraokeSearch import search_joysound, JoySoundSearchQuery, make_joysound_responce
from PyKaraokeSearch import JoySoundSearchQueryField as QF
from PyKaraokeSearch import search_clubdam, ClubDamSearchQuery



app = Flask(__name__)

@app.route('/api/search', methods=['GET'])
def search_keyword():
	if request.method == 'GET':
		keyword = request.args.get('keyword')

		print(keyword)

		if not keyword:
			return jsonify({"status": "error", "message": "なんか文字入れて"})


		joyResult = search_joysound(JoySoundSearchQuery(
			filters=[
				QF.Filter(
					kind='compound',
					word=keyword,
					match="partial",
				)
			]
		))
		joyResponce = make_joysound_responce(joyResult)

		damResult = search_clubdam(ClubDamSearchQuery(keyword=keyword))

		return jsonify({"joyResult": joyResponce, "status": "ok"})
		# return jsonify({"damResult" : damResult, "joyResult": joyResult, "status": "ok"})
	else:
		return jsonify({"status": "error", "message": "POST やん..."})


if __name__ == "__main__":
	app.run(debug=True)

