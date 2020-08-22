from app import app

@app.route('/')
def home():
   return "hello from Tarik to the world!"
