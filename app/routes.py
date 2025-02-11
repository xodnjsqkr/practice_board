from flask import render_template
import pymysql
from app.config.config import Config

def init_routes(app):
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return render_template("index.html")
    
    @app.route('/check_db')
    def check_db():
        connection=None
        try:
            # 데이터베이스에 연결
            connection=pymysql.connect(
                host=app.config['DB_HOST'],
                port=app.config['DB_PORT'],
                user=app.config['DB_USER'],
                password=app.config['DB_PASSWORD'],
                db=app.config['DB_NAME'],
                cursorclass=pymysql.cursors.DictCursor 
            )
            with connection.cursor() as cursor:
                cursor.execute("select version() as version")
                version=cursor.fetchone()
                return f"Database connection is successful! MySQL version: {version['version']}", 200
        except Exception as e:
            return f"Database connection failed: {str(e)}", 500
        finally:
            if connection:
                connection.close()