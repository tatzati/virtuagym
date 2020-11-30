# virtuagym
cd virtuagym

chmod +x entrypoint.sh

docker-compose up -d --build

docker-compose exec web python app/manage.py createsuperuser
email: admin@admin.com & password: 12345678

