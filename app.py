from src import create_app
from apscheduler.schedulers.background import BackgroundScheduler
import googleapiclient.discovery
import os
import uuid
import datetime

app = create_app()
sched = BackgroundScheduler()
from src.database import db
from src.models import Video
from src.config import ACCESS_KEY


def fetch_data_from_api(): 
    print('Fetching Data')
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ACCESS_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        q='Cricket',
        part='snippet',
        type='video',
        maxResults=10,
        publishedAfter="2020-01-01T00:00:00Z",
        order='date',
    )

    response = request.execute()

    with app.app_context():
        Video.query.delete()
        for video in response['items']:
            video_entry = Video(
                public_id = str(uuid.uuid4()),
                title = video['snippet']['title'],
                description = video['snippet']['description'],
                publish_time = datetime.datetime.strptime(video['snippet']['publishTime'], "%Y-%m-%dT%H:%M:%SZ"),
                thumbnail_url = video['snippet']['thumbnails']['default']['url'],
                video_id = video['id']['videoId']
            )
            db.session.add(video_entry)
        db.session.commit()
    print("Data Saved Succesfully")


if __name__ == '__main__':
    sched.add_job(fetch_data_from_api, 'interval', seconds=10)
    sched.start()
    app.run(debug=True) 
    
