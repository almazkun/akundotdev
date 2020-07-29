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
docker-compose -f docker-compose.yml down -v


docker-compose -f docker-compose.yml up -d --build


docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput


docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

```
<VirtualHost *:80>
    ServerAdmin me@akun.dev
    DocumentRoot /var/www/html/akun.dev/
    ServerName akun.dev

    <Directory /var/www/html/akun.dev/akundotdev_conf>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    WSGIScriptAlias / /var/www/html/akun.dev/akundotdev_conf/wsgi.py
    
    ErrorLog /var/log/httpd/akun.dev.com-error_log
    CustomLog /var/log/httpd/akun.dev.com-access_log common
</VirtualHost>

```

/etc/httpd/conf.d/akun.dev.conf

PATH=$PATH:~/opt/bin
killall gunicorn

sudo rm -rf staticfiles
sudo mkdir staticfiles
sudo chmod 777 staticfiles
python36 manage.py collectstatic
sudo chmod 755 staticfiles

```bash
gunicorn -b 127.0.0.1:8000 -w 3 akundotdev_conf.wsgi --daemon
```

```bash
git clone https://github.com/almazkun/akundotdev.git
```
```bash
sudo yum install -y mod24_ssl
sudo ./certbot-auto --debug -v --server https://acme-v02.api.letsencrypt.org/directory certonly -d akun.dev
```
IT Consulting · Web Development · Custom Software Development · Application Development
Web Development · Business Analytics · Database Development · Custom Software Development · Information Management · User Experience Design (UED)
Web Development · Custom Software Development · Application Development