from flask import Blueprint, make_response, request
from .models import Video


views = Blueprint('views', __name__)

@views.route('/', methods =['GET'])
def home():
    return make_response({'data': "Server up and running"}, 200)

@views.route('/videos')
@views.route('/videos/page/<int:page>', methods =['GET'])
def get_all_videos(page=1):
    video_list = Video.query.order_by(
        Video.publish_time.desc()
    ).paginate(page, per_page=5)
    if video_list:
        videos_data = []
        for video in video_list.items:
            videos_data.append({
                "title" : video.title,
                "description" : video.description,
                "publish_time" : video.publish_time,
                "thumbnail_url" : video.thumbnail_url,
                "video_id" : video.video_id,
            })
        return make_response({'videos': videos_data}, 200)
    else:
        return make_response({"error":"No data available"}, 403)


@views.route('/videos/search', methods =['GET'])
def search():
    args = request.args
    data = args.get('data')

    if not data:
        return make_response({"error":"No parameters passed"})

    video_list = Video.query.msearch(data,fields=['title','description']).all()

    if video_list:
        videos_data = []
        for video in video_list:
            videos_data.append({
                "title" : video.title,
                "description" : video.description,
                "publish_time" : video.publish_time,
                "thumbnail_url" : video.thumbnail_url,
                "video_id" : video.video_id,
            })
        return make_response({'videos': videos_data}, 200)
    else:
        return make_response({"error":"No data available"}, 403)