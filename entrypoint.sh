#!/bin/sh
set -e
service ssh start
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)
exec gunicorn -w 4 -b 0.0.0.0:8000 app:app