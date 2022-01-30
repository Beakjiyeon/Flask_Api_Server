from main import app, Config

if __name__ == '__main__':
    app.run(host=Config.RUN_HOST, port=Config.RUN_PORT)
    


