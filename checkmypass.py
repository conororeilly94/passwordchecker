import requests
import hashlib

def request_api_data(query_char): # Give hash version of password
	url = 'https://api.pwnedpasswords.com/range/' + query_char #Only gives part of hash function password
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
	return res

def pwned_api_check(password):
	# Check password if it exits in API response
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	return sha1password 

pwned_api_check('123')