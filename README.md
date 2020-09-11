# http-api-upload

### Stack 
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
curl -X PUT -F file=@<file> http://127.0.0.1:5000/upload
```

**Response:**
```json
// If аile uploaded successfully
{"hash":"a5dc28771a0c882a7d4841a8227e069a","status":"200"}
```

```json
// If something went wrong
{'status': '400', 'error': 'Something went wrong'}
```


#### Download file:
```curl
curl -X GET http://127.0.0.1:5000/download/<hash> --output <hash>
```

**Response:**
```json
// if file nothing
{"error":"File not found","status":"404"}
```

#### Delete file:
```curl
curl -X DELETE http://192.168.1.9:5000/delete/<hash>
```

**Response:**
```json
// If file deleted
{'status': '200', 'file': hash}
```
```json
// If file nothing
{'status': '404', 'error': 'File not found'}
```