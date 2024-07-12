#!/bin/bash

#going into project folder
cd /root/portfolio-project

#updating project folder to have latest changes from the main branch on GitHub.
git fetch && git reset origin/main --hard

#entering python virtual environment and installing required dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

#restarting the myportfolio systemd service, so that the changes above get applied
systemctl daemon-reload
systemctl restart myportfolio