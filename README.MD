# Software Engineer, Portfolio

Portfolio of [Almaz Kunpeissov, Software Engineer](https://akun.dev). Python, Django.



## Useful links
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html
* https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/
* https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
* https://django-lessons.com/lesson/lesson-22-django-deploy-production-step-by-step-from-zero-to-hero-part-5-gunicorn

* https://github.com/dmitrym0/simple-lets-encrypt-docker-compose-sample/blob/master/docker-compose.yml


## Docker commands
```bash
docker-compose -f docker-compose.prod.yml down -v


docker-compose -f docker-compose.prod.yml up -d --build


docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput


docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```


