from controllers.userController import UserController, UsersController

def initialize_routes(api):
    api.add_resource(UserController, '/users')
    api.add_resource(UsersController, '/users/<id>')