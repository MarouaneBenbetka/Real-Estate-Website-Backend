import os

from api import app
import jwt

token = jwt.encode({"userId": "b55faeb4-a3fe-11ed-a61a-fc084ad74753"}, os.getenv("TOKEN_SECRET"))
print(token)
print(jwt.decode(jwt.encode({"userId": "b55faeb4-a3fe-11ed-a61a-fc084ad74753"}, os.getenv("TOKEN_SECRET")),os.getenv("TOKEN_SECRET"),algorithms='HS256'))
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")



