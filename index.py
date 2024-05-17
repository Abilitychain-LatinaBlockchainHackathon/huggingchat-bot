from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask import jsonify

from hugchat import hugchat
from hugchat.login import Login

EMAIL = "abilitichain@gmail.com"
PASSWD = "Abilitychain24"
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot.switch_llm(1)

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
cors = CORS(app)

@app.route('/api/chat/skills', methods=['POST'])
def create_chat():
    json = request.get_json(force=True)
    requirement_total = "Eres un psicologo donde trabajas para una academia que se dedica a mejorar las habilidades brandas, necesito responder la siguiente pregunta: " + json['message']
    query_result = chatbot.chat(str(requirement_total))
    print(query_result)
    return jsonify({'message' : str(query_result) })


if __name__ == '__main__':
    app.run(debug=True)