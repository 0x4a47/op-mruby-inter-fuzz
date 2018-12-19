# Urls

> 'fuzz' enter view
> cntrl-d b (lol)

# Web-GUI Setup

```
# need for plotting
apt-get install gnuplot

# afl mon
git clone https://github.com/reflare/afl-monitor.git

# crontab -e
*/30 * * * * (rm /var/www/html/*.png) && (/root/tools/afl-monitor/afl-monitor -h /var/www/html/ -v  /root/afl-outdirectories/)

# setup basic auth
sudo sh -c "echo -n 'afl:' >> /etc/nginx/.htpasswd"
sudo sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"

# nginx config
location / {
 try_files $uri $uri/ =404;
 auth_basic "Restricted Content";
 auth_basic_user_file /etc/nginx/.htpasswd;
}
```

# Push Notifier Setup
- Using pushover pushnotification service. [pushover](https://pushover.net)
- Using pyinotify to monitor file changes in the directory we specify. See code for details. [pyinotify](https://github.com/seb-m/pyinotify/)
- Worth noting the following links:
  - [python-pushover](https://github.com/Thibauth/python-pushover)
  - [inofitywatch](https://linux.die.net/man/1/inotifywatch)
  - [inotify-hookable](http://manpages.ubuntu.com/manpages/xenial/man1/inotify-hookable.1p.html)
