from flask import jsonify, request, current_app, Response
from flask.views import MethodView
from flask_jwt_extended import jwt_required
import pafy
import requests


class Play(MethodView):
    @jwt_required
    def get(self):
        if 'id' not in request.args:
            return jsonify('must supply id')

        base_url = "https://www.youtube.com/watch?v="
        url = base_url + request.args['id']
        # video = pafy.new(url)
        # bestaudio = video.getbestaudio()
        # bestaudio.download(filepath=current_app.config['DOWNLOAD_PATH'], meta=True, quiet=True)
        url = 'https://r2---sn-gvbxgn-tt1r.googlevideo.com/videoplayback?ei=Sg_-WcSoKYXmDcGBtdAI&clen=4106131&gir=yes&keepalive=yes&mime=audio%2Fwebm&key=yt6&itag=251&pcm2cms=yes&source=youtube&lmt=1449643609609011&initcwndbps=1101250&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpcm2cms%2Cpl%2Crequiressl%2Csource%2Cexpire&ipbits=0&expire=1509843882&id=o-AILEYluhCMFI703D1LD2KEfVtdtQrBfJYKDRic6y8fE_&dur=249.841&requiressl=yes&mm=31&pl=36&mn=sn-gvbxgn-tt1r&ip=2607%3Afea8%3A9560%3A6e2%3Acc4f%3Aee7f%3Ad51d%3A38de&ms=au&mt=1509822166&mv=m&signature=AD2B4D922E4FAD209E7D312C3A80AA22CC3A65F1.BD418DEABA698DD1A2769B26381D784722E325AE&ratebypass=yes'

        def stream_url(url):
            r = requests.get(url, stream=True)
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk

        return Response(stream_url(url), mimetype='audio/webm')
