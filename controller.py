import web
from models import RegisterModel, LoginModel, Posts

# To properly run the sessions
web.config.debug = False

urls = (
    '/', 'home',
    '/register', 'register',
    '/postregistration', 'PostRegistration',
    '/login', 'LogIn',
    '/logout', 'LogOut',
    '/checklogin', 'CheckLogin',
    '/postactivity', 'postactivity',
    '/settings', 'settings',
    '/updateform', 'updateform'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("views/templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})

# Classes/Routes
class home:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Home(posts)
    '''   
        data = type('obj', (object,), {"username": "Navya", "password": "putti"})

        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
    '''



class register:
    def GET(self):
        return render.Register()


class LogIn:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
            return isCorrect

        return "error"


class postactivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['name']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"


class settings:
    def GET(self):
        return render.Settings()
    '''    
        data = type('obj', (object,), {"username": "Navya", "password": "putti"})

        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect
    '''


class updateform:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]
        
        settings_model = LoginModel.LoginModel()
        if settings_model.update_info(data):
            return "success"
        else:
            return "Fatal error"


class LogOut:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"


if __name__ == "__main__":
    app.run()
