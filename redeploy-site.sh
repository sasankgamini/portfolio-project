#!/bin/bash

#going into project folder
cd /root/portfolio-project

#updating project folder to have latest changes from the main branch on GitHub.
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build