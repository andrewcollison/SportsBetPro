# python version 3.8.0

# Import required packages
import requests
import json

def main():
	# should not actually be run from here. import to different script
	print('loaded pull_data')

class GetData():
	"""docstring for getData"""
	def __init__(self):
		# nothing to init
		print('GetData class init')
		
	def get_active_sports(self):
		print('Starting Sports Request')

		# https://api.the-odds-api.com/v3/sports/?apiKey=4e28f0f30c120627544a89a7a51977a5
		resp = requests.get('https://api.the-odds-api.com/v3/sports',
			headers={'Content-Type':'application/json'},
			params={'api_key': '4e28f0f30c120627544a89a7a51977a5'} )
		#print(resp.json())

		#dump response json to file
		with open('json_dumps\sports.json', 'w') as f:
			json.dump(resp.json(), f)

		print('Finish Sports Request')
		

	def get_sport_odds(self, request_params):
		print('Starting Odds Request')

		resp = requests.get(request_params.request_url,
			headers = {'Content-Type':'application/json'},
			params = request_params.params )
		#print(resp.json())

		#dump response json to file
		with open('json_dumps\odds.json', 'w') as f:
			json.dump(resp.json(), f)

		print('Finish Odds Request')
		return resp.json()

class SportOddsRequestParams():
	"""class for data structures for request parameters"""
	def __init__(self, sport='not set', region='au', market='h2h'):
		#setup structure
		self.params = {}
		self.params['api_key'] = '4e28f0f30c120627544a89a7a51977a5'
		self.params['region'] = region
		self.params['sport'] = sport
		self.params['mkt'] = market #default to h2h

		self.request_url = 'https://api.the-odds-api.com/v3/odds'

	def updateParams(self, sport, region='au', market='h2h'):
		self.params['sport'] = sport
		self.params['sport'] = region
		self.params['sport'] = market





if __name__== '__main__':
	main()
