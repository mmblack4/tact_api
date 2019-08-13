from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import generate_password_hash

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('full_name',
        help = ""
    )
    # email
    parser.add_argument('email',
        help = ""
    )
    parser.add_argument('password',
        help = ""
    )
    #linkedin link
    parser.add_argument('linkedin_link',
        help = ""
    )
    parser.add_argument('location',
        help = ""
    )
    #phone_number
    parser.add_argument('phone_number',
        type = int,
        help = ""
    )
    #github_link
    parser.add_argument('github_link',
            help = ""
    )
    #gitlab_link
    parser.add_argument('gitlab_link',
        help = ""
    )
    #bitbucket_link
    parser.add_argument('bitbucket_link',
            help = ""
    )


    def post(self, username):
        data = User.parser.parse_args()

        if UserModel.find_by_username(username):
            return {'message': "user name '{}' already exists.".format(username)}, 400
        if UserModel.find_by_email(data.email):
            return {'message': "email '{}' already used.".format(data.email)}, 400
        if UserModel.find_by_linkedin_link(data.linkedin_link):
            return {'message': "linkedin link '{}' already used.".format(data.linkedin_link)}, 400
        data.password = generate_password_hash(password, method='sha256')
        user = UserModel(username, **data)

        try:
            user.save_to_db()
        except:
            return {'message': 'An eror occured insertingthe link.'}, 500

        return user.json(), 201

    def put(self, username):
        data = User.parser.parse_args()

        user = UserModel.find_by_username(username)
        if user is not None:
            if UserModel.find_by_email(data.email):
                return {'message': "email '{}' already used.".format(data.email)}, 400
            if UserModel.find_by_linkedin_link(data.linkedin_link):
                return {'message': "linkedin link '{}' already used.".format(data.linkedin_link)}, 400
            user.full_name = data.full_name if data.full_name is not None else user.full_name
            user.email = data.email if data.email is not None else user.email
            user.password = generate_password_hash(data.password, method='sha256') if data.password is not None else user.password
            user.linkedin_link = data.linkedin_link if data.linkedin_link is not None else user.linkedin_link
            user.location = data.location if data.location is not None else user.location
            user.phone_number = data.phone_number if data.phone_number is not None else user.phone_number
            user.github_link = data.github_link if data.github_link is not None else user.github_link
            user.gitlab_link = data.gitlab_link if data.gitlab_link is not None else user.gitlab_link
            user.bitbucket_link = data.bitbucket_link if data.bitbucket_link is not None else user.bitbucket_link


            try:
                user.save_to_db()
            except:
                return {'message': 'An eror occured insertingthe link.'}, 500
        else:
            if UserModel.find_by_username(username):
                return {'message': "user name '{}' already exists.".format(username)}, 400
            if UserModel.find_by_email(data.email):
                return {'message': "email '{}' already used.".format(data.email)}, 400
            if UserModel.find_by_linkedin_link(data.linkedin_link):
                return {'message': "linkedin link '{}' already used.".format(data.linkedin_link)}, 400
            user = UserModel(username, **data)
            try:
                user.save_to_db()
            except:
                return {'message': 'An eror occured insertingthe link.'}, 500

    
        return user.json(), 201

    def delete(self, username):
        user = UserModel.find_by_username(username)
        
        if user:
            user.delete_from_db()
            return {'message': 'user delete'}

        return {'message': "user name '{}' didn't exists.".format(username)}, 400

class UserBy(Resource):

    def get(self, column, column_value):
        if column == "userid":
            user = UserModel.find_by_userid(column_value)
            if user:
                return user.json(), 201
            return {'message': "user ID '{}' didn't exists.".format(column_value)}, 400

        elif column == "username":
            user = UserModel.find_by_username(column_value)
            if user:
                return user.json(), 201
            return {'message': "user name '{}' didn't exists.".format(column_value)}, 400

        elif column == "email":
            user = UserModel.find_by_email(column_value)
            if user:
                return user.json(), 201
            return {'message': "email '{}' didn't exists.".format(column_value)}, 400

        elif column == "linked_link":
            user = UserModel.find_by_linked_link(column_value)
            if user:
                return user.json(), 201
            return {'message': "linked link '{}' didn't exists.".format(column_value)}, 400



class UserList(Resource):
    def get(self):
        return {'items': [user.json() for user in UserModel.query.all()]}
