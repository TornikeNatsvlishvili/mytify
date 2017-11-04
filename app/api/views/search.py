from app.extensions import mongo

from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
import pafy


class Search(MethodView):
    @jwt_required
    def get(self):
        results = []
        if 'qs' in request.args:
            term = request.args['qs']
            wdata = pafy.call_gdata('search', generate_search_qs(term))
            for item in wdata['items']:

                song = {
                    'title': item['snippet']['title'],
                    'video_id': get_track_id_from_json(item)
                }
                results.append(song)

        return jsonify({'results': results}), 200


config = {
    'order': 'relevance',  # options: relevance date views rating title
    'api_key': "AIzaSyCIM4EzNqi1in22f4Z3Ru3iYvLaY8tc3bo",
    'search_music': True
}


def generate_search_qs(term, match='term', videoDuration='any', after=None, category=None, is_live=False):
    """ Return query string. """

    aliases = dict(views='viewCount')
    qs = {
        'q': term,
        'maxResults': 50,
        'safeSearch': "none",
        'order': config['order'],
        'part': 'id,snippet',
        'type': 'video',
        'videoDuration': videoDuration,
        'key': config['api_key']
    }

    if after:
        after = after.lower()
        qs['publishedAfter'] = '%sZ' % (datetime.utcnow() - timedelta(days=DAYS[after])).isoformat() \
            if after in DAYS.keys() else '%s%s' % (after, 'T00:00:00Z' * (len(after) == 10))

    if match == 'related':
        qs['relatedToVideoId'] = term
        del qs['q']

    if config['search_music']:
        qs['videoCategoryId'] = 10

    if category:
        qs['videoCategoryId'] = category

    if is_live:
        qs['eventType'] = "live"

    return qs


def get_track_id_from_json(item):
    """ Try to extract video Id from various response types """
    fields = ['contentDetails/videoId',
              'snippet/resourceId/videoId',
              'id/videoId',
              'id']
    for field in fields:
        node = item
        for p in field.split('/'):
            if node and isinstance(node, dict):
                node = node.get(p)
        if node:
            return node
    return ''
