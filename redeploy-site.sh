#!/bin/bash

tmux kill-server
cd /root/portfolio-project
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s portfolio_app
tmux send-keys -t portfolio_app 'cd /root/portfolio-project' C-m
tmux send-keys -t portfolio_app 'source python3-virtualenv/bin/activate' C-m
tmux send-keys -t portfolio_app 'flask run --host=0.0.0.0 --port=80' C-m