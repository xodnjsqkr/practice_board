from flask import render_template
from app.db.connection import get_db_connection

def init_routes(app):
    @app.route('/')
    def index():
        return render_template("index.html")
    
    @app.route('/user/<username>')
    def user(username):
        return render_template('user_info.html', username=username)
    
    @app.route('/check_db')
    def check_db():
        connection=None
        try:
            connection=get_db_connection()
            cursor=connection.cursor()
            sql="select version() as version"
            cursor.execute(sql)
            result=cursor.fetchone()
            return f"Database connection is successful! MySQL version: {result['version']}", 200
        except Exception as e:
            return f"Database connection failed: {str(e)}", 500
        finally:
            if connection:
                connection.close()