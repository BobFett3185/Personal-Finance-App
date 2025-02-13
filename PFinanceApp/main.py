# install flask, flask login, sql alchemy - done 
#import the create app function from Pfinanceweb

# main.py is just for running the app, code for app is on init.py and you just import it in main.py

# double {{ }} in an html file allows you to write python code in the html file though jinja (templating lang)

# HTTP requests: get request is retrieving info or showing webpage, post request is for updating something

from PFW import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


