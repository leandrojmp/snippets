## instalação e configuração do memcached

### install
 
`yum install memcached`
 
### config
 
`/etc/sysconfig/memcached`
 
 ```
PORT="11211"
USER="memcached"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS="-l IP -U 0"
 ```
 
### service
 
`/usr/lib/systemd/system/memcached.service`

 ```
[Unit]
Description=Memcached
Before=httpd.service
After=network.target
 
[Service]
Type=simple
EnvironmentFile=-/etc/sysconfig/memcached
ExecStart=/usr/bin/memcached -u $USER -p $PORT -m $CACHESIZE -c $MAXCONN $OPTIONS
 
[Install]
WantedBy=multi-user.target
```