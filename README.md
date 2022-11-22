Eventex

Sistemas de Eventos

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv
3. Ative o virtualenv.
4. instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

'''
console
git clone git@github.com/andremleopoldino/eventex.git wttd
cd wttd
python -m venv .wttd
.wttd/scrips/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
'''
## Como fazer deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o Heroku.
3. Define uma SECRET_KEY segura para instãncia.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku


'''
console

heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False

#configuro o email
git push heroku main --force
'''