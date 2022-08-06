from . import db     #import db from package

# set the location for the whoosh index

class Video(db.Model):
    __searchable__ = ['title', 'description']
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    publish_time = db.Column(db.DateTime(timezone=True))
    thumbnail_url = db.Column(db.String(100))
    video_id = db.Column(db.String(50), unique=True)

    def __init__(self, public_id, title, description, publish_time, thumbnail_url, video_id):
        self.public_id = public_id
        self.title = title
        self.description = description
        self.publish_time = publish_time
        self.thumbnail_url = thumbnail_url
        self.video_id = video_id

