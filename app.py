'''
Here We get app from api folder
where api folder will take care of all configuration 
like routes, database etc
Here it becomes very easy to run application
'''

from api import app

if __name__=="__main__":
    app.run(debug=True)