#!/usr/bin/env bash

function update
{
    echo "--------------- Starting update ---------------"
    git pull
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py collectstatic --noinput
    touch wsgi.py
    python manage.py check --deploy
    echo "--------------- Update complete ---------------"
}

# Append output of update command to the beginning of update.log flie
mv update.log update.log.bak
update | tee update.log
cat update.log.bak >> update.log
