from flask import Flask, redirect, request

app = Flask(__name__)

CLIENT_ID = '78j5cswwgzxzbm'
REDIRECT_URI = 'https://www.linkedin.com/developers/tools/oauth/redirect'
SCOPE = 'r_liteprofile'

@app.route('/')
def index():
    authorization_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}'
    return redirect(authorization_url)

@app.route('/linkedin/callback')
def linkedin_callback():
    code = request.args.get('code')
    # Maintenant vous avez le code d'autorisation que vous pouvez utiliser pour obtenir le jeton d'accès
    # Vous pouvez appeler la fonction get_access_token avec ce code
    # Une fois que vous avez le jeton d'accès, vous pouvez faire des requêtes à l'API LinkedIn
    return f'Code d\'autorisation: {code}'

if __name__ == '__main__':
    app.run(debug=True)
