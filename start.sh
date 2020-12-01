export NEWS_API_KEY='5810c4b503854ab0bb9be6639d73a30a'
export SECRET_KEY='2324'

python3.6 manage.py server

heroku config:set NEWS_API_KEY=5810c4b503854ab0bb9be6639d73a30a
heroku config:set SECRET_KEY=2324