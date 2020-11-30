# Virtuagym

## How to Install

### 1. cd into project files
```bash
cd virtuagym
```

### 2.Adjust permissions
```bash
sudo chmod +x entrypoint.sh
```

### 3. Get the docker image up and running
```bash
docker-compose up -d --build
```

### 4. Create new superuser
```bash
docker-compose exec web python app/manage.py createsuperuser
```
Please use email: _admin@admin.com_ password: _12345678_ when prompted.

Now the application is running just navigate to localhost or localhost/admin and use 
email:admin@admin.com password: 12345678 
to login as admin.


### API Documentation
Api documentation is found on the root url.

