# http-api-upload
 
Upload file:
curl -X PUT -F file=@hyde-2.1.0.zip http://127.0.0.1:5000/upload

Download file:
curl -X GET http://127.0.0.1:5000/download/a5dc28771a0c882a7d4841a8227e069a --output a5dc28771a0c882a7d4841a8227e069a