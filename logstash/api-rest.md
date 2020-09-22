## muda o log level para erros do filtro dissect

```
curl -XPUT 'localhost:9600/_node/logging?pretty' -H 'Content-Type: application/json' -d' 
    {
        "logger.org.logstash.dissect.Dissector" : "ERROR"
    }'
```