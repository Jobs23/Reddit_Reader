from flask import Flask 
import json, requests, time, unidecode

app = Flask(__name__)

def get_headlines():
	user_pass_dict = {'user':'your_username','passwd':'your_password','api_type':'json'}
	sess = requests.Session()
	sess.headers.update({'User-Agent':'Trying some stuff out'})
	sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
	time.sleep(1)
	url = 'https://www.reddit.com/r/news/.json?limit=15'
	html = sess.get(url)
	data = json.loads(html.content.decode('utf-8'))
	li = [each for each in data['data']['children']] #[u'modhash', u'whitelist_status', u'children', u'after', u'before'] 
	titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
	titles = '\n\n'.join([i for i in titles])
	return titles

titles = get_headlines()
print titles


if __name__ == '__main__':
	app.run(debug=True)
