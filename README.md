# http-api-upload

### Stack

**venv**

`pip3 install flask gunicorn`

**Gunicorn**

Start daemon:  `gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon`

**Flask**

Modules in Flask:
- hashlib
- os
- werkzeug

**Hash**

Hashing method is MD5

****

### Request and response
#### Upload file:
```curl
curl -X PUT -F file=@<file> http://<IP or domain>/upload
```

*Response:*
```json
// If file uploaded successfully
{"hash":"<hash>","status":"200"}
```

```json
// If something went wrong
{"status": "400", "error": "Something went wrong"}
```


#### Download file:
```curl
curl -X GET http://<IP or domain>/download/<hash> --output <hash>
```

*Response:*
```json
// if file nothing
{"error":"File not found","status":"404"}
```

#### Delete file:
```curl
curl -X DELETE http://<IP or domain>/delete/<hash>
```

*Response:*
```json
// If file deleted
{"status": "200", "file": "<hash>"}
```
```json
// If file nothing
{"status": "404", "error": "File not found"}
```