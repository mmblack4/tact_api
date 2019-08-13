from db import db



class UserModel(db.Model):

    __tablename__ = 'user'

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique=True)
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255),nullable=False)
    linkedin_link = db.Column(db.String(255),unique=True)
    location = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    github_link = db.Column(db.String(255))
    gitlab_link = db.Column(db.String(255))
    bitbucket_link = db.Column(db.String(255))


    def __init__(self, username, password ,full_name=None, email=None, location=None, linkedin_link=None, phone_number=None, github_link=None, gitlab_link=None, bitbucket_link=None):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.password = password
        self.linkedin_link = linkedin_link
        self.location = location
        self.phone_number = phone_number
        self.github_link = github_link
        self.gitlab_link = gitlab_link
        self.bitbucket_link = bitbucket_link
    
    def json(self):
        return {'username': self.username,
                'full name': self.full_name,
                'email': self.email,
                'password': self.password,
                'linkedin link': self.linkedin_link,
                'location': self.location,
                'phone number': self.phone_number,
                'github link': self.github_link,
                'gitlab link': self.gitlab_link,
                'bitbacket link': self.bitbucket_link
    }

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(userid=userid).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_linkedin_link(cls, linkedin_link):
        return cls.query.filter_by(linkedin_link=linkedin_link).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
