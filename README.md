# virtuagym
cd virtuagym

chmod +x entrypoint.sh

docker-compose up -d --build

docker-compose exec web python app/manage.py createsuperuser

