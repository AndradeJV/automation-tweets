import json
from Twitter.Classes.Login import Login


def login_usuario_twitter():
    with open("pessoal.json") as f_login:
        data_login = json.load(f_login)

    with open("tweets.json") as r_tweets:
        data_tweets = json.load(r_tweets)
    
    Login.abrir_twitter()
    Login.click_logar()
    Login.inserir_usuario(data_login.get('login'))
    Login.inserir_senha(data_login.get('senha'))
    Login.realizar_tweet(data_tweets.get('tweetTres'))
    Login.logoff()


login_usuario_twitter()