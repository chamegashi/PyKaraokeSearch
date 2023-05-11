from PyKaraokeSearch.joysound.JoySoundSearchQueryField import Match
from flask import Flask, jsonify, request

from PyKaraokeSearch import search_joysound, JoySoundSearchQuery, make_joysound_responce
from PyKaraokeSearch import JoySoundSearchQueryField as QF
from PyKaraokeSearch import search_clubdam, ClubDamSearchQuery, make_clubDam_responce

from GetKaraokeDBData import getMusic, registMusic, getShareMusic, registShareMusic, updateIsAvailable, deleteShareMusic, updateShareMusic
from GetKeyRange import keySearch

app = Flask(__name__)


@app.route('/api/search', methods=['GET'])
def search_keyword():
    if request.method == 'POST':
        return jsonify({"status": "error", "message": "POST やん..."})

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

    return jsonify({"damResponce": damResponce, "joyResponce": joyResponce, "status": "ok"})


@app.route('/api/music/get', methods=['GET'])
def get_music():
    if request.method != 'GET':
        return jsonify({"status": "error", "message": "GET じゃないやん..."})

    result = getMusic()
    return jsonify({"result": result,  "status": "ok"})


@app.route('/api/music/regist', methods=['POST'])
def regist_music():
    if request.method != 'POST':
        return jsonify({"status": "error", "message": "POST じゃないやん..."})

    data = {
        "music_name": request.form.get(),
        "music_name_hira": request.form.get(),
        "artist": request.form.get(),
        "key": request.form.get(),
        "max_key": request.form.get(),
        "max_score": request.form.get(),
        "user_id": request.form.get(),
    }

    result = registMusic()
    return jsonify({"result": result,  "status": "ok"})


@app.route('/api/getKey', methods={'GET'})
def get_key():
    if request.method == 'GET':
        keywords = request.args.get('keywords')
        if not keywords:
            return jsonify({"status": "error", "message": "なんか文字入れて"})

        res = keySearch.searchKey(keywords)

        return jsonify({"data": res, "status": "ok"})
    else:
        return jsonify({"status": "error", "message": "POST やん..."})


# share music 用 api

@app.route('/api/share_music/get', methods=['GET'])
def get_share_music():
    if request.method != 'GET':
        return jsonify({"status": "error", "message": "GET じゃないやん..."})

    result = getShareMusic()
    return jsonify({"result": result,  "status": "ok"})


@app.route('/api/share_music/regist', methods=['POST'])
def regist_share_music():
    if request.method != 'POST':
        return jsonify({"status": "error", "message": "POST じゃないやん..."})

    data = {
        "title": request.form.get('title'),
        "hiragana": request.form.get('hiragana'),
        "artist": request.form.get('artist'),
        "max_key": request.form.get('max_key'),
        "is_available_msy": request.form.get('is_available_msy'),
        "is_available_gil": request.form.get('is_available_gil'),
        "is_available_fulu": request.form.get('is_available_fulu'),
    }

    result = registShareMusic(data)
    return jsonify({"result": result,  "status": "ok"})


@app.route('/api/share_music/update', methods=['POST'])
def update_share_music():
    if request.method != 'POST':
        return jsonify({"status": "error", "message": "POST じゃないやん..."})

    data = {
        "id": request.form.get('id'),
        "title": request.form.get('title'),
        "hiragana": request.form.get('hiragana'),
        "artist": request.form.get('artist'),
        "max_key": request.form.get('max_key'),
        "is_available_msy": request.form.get('is_available_msy'),
        "is_available_gil": request.form.get('is_available_gil'),
        "is_available_fulu": request.form.get('is_available_fulu'),
    }

    result = updateShareMusic(data)
    return jsonify({"result": result,  "status": "ok"})


@app.route('/api/share_music/update_is_avialable', methods=['POST'])
def update_is_avialable():
    if request.method != 'POST':
        return jsonify({"status": "error", "message": "POST じゃないやん..."})

    data = {
        "id": request.form.get('id'),
        "is_available_msy": request.form.get('is_available_msy'),
        "is_available_gil": request.form.get('is_available_gil'),
        "is_available_fulu": request.form.get('is_available_fulu'),
    }

    result = updateIsAvailable(data)
    return jsonify(result)


@app.route('/api/share_music/delete', methods=['POST'])
def delete_share_music():
    if request.method != 'POST':
        return jsonify({"status": "error", "message": "POST じゃないやん..."})

    result = deleteShareMusic(request.form.get('id'))
    return jsonify(result)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
