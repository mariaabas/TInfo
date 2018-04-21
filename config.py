# Set this to False if going to production
DEBUG = True

# Set this to random value when going to production
SECRET_KEY = 'development'

# App credentials lazy load configuration
# Read: https://flask-oauthlib.readthedocs.io/en/latest/client.html#lazy-configuration
# Get them: https://raco.fib.upc.edu/api/v2/o/
RACO = {
    'consumer_key': '301b1425-d6a9-4a18-80e8-64f3157947c4',
    'consumer_secret': '71c7d4e3-8aa1-4da0-bb78-ec95b003610c'
}
