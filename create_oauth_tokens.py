import json
import webbrowser
import http.server
import requests

from oauth2client.client import OAuth2WebServerFlow

CLIENT_ID = None
CLIENT_SECRET = None


class OAuth2Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        code = self.path.split('/?code=')[1]

        response = requests.post('https://www.googleapis.com/oauth2/v4/token', data={
            'code': code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': 'http://localhost:8915',
            'grant_type': 'authorization_code',
        })

        tokens = json.loads(response.text)

        with open('./client_secrets.example.json', 'r') as client_secrets_file:
            content = json.load(client_secrets_file)

        with open('./client_secrets.json', 'w') as client_secrets_file:
            content['web']['client_id'] = CLIENT_ID
            content['web']['client_secret'] = CLIENT_SECRET

            json.dump(content, client_secrets_file, indent=4, separators=(',', ': '))

        with open('./youtube.py-oauth2.example.json', 'r') as oauth2_file:
            content = json.load(oauth2_file)

        with open('./youtube.py-oauth2.json', 'w') as oauth2_file:
            content['refresh_token'] = tokens['refresh_token']
            content['client_id'] = CLIENT_ID
            content['client_secret'] = CLIENT_SECRET
            content['access_token'] = tokens['access_token']
            content['token_response']['access_token'] = tokens['access_token']

            json.dump(content, oauth2_file, indent=4, separators=(',', ': '))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(str.encode('Success!'))


def main():
    global CLIENT_ID, CLIENT_SECRET

    CLIENT_ID = input('Enter your client_id: ')
    CLIENT_SECRET = input('Enter your client_secret: ')

    flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               scope='https://www.googleapis.com/auth/youtube.upload',
                               redirect_uri='http://localhost:8915')

    webbrowser.open(flow.step1_get_authorize_url())

    server = http.server.HTTPServer(('localhost', 8915), OAuth2Handler)
    server.handle_request()

if __name__ == '__main__':
    main()
