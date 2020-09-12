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

{"hash":"<hash>"}

// HTTP Response: 200
```

```json
// If something went wrong

{"error": "Something went wrong"}

// HTTP Response: 404
```


#### Download file:
```curl
curl -X GET http://<IP or domain>/download/<hash> --output <hash>
```

*Response:*
```json
// if file not found

{"error":"File not found"}

// HTTP Response: 404
```

#### Delete file:
```curl
curl -X DELETE http://<IP or domain>/delete/<hash>
```

*Response:*
```json
// If file deleted

{"file": "<hash>"}

// HTTP Response: 200
```
```json
// If file not found

{"error": "File not found"}

// HTTP Response: 404
```