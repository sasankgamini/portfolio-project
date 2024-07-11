#!/bin/bash

#post request
echo "Testing POST endpoint below:"
curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=random&email=random@random.com&content=creating a random timeline post'

#get request
echo "Testing GET endpoint below:"
curl http://127.0.0.1:5000/api/timeline_post

