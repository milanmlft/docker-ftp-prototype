# docker-ftp-prototype

Python prototype for uploading a file to an SFTP server

All runs in docker compose.

```
docker compose up --exit-code-from uploader
```

- Because this is only for testing, generating static SSL certificates and committing them seems fine
- The Dockerfile builds out environment to allow `uploader/upload.py` to create a new directory in the FTP server 
  and then copy the `uploader/public.zip` to the new FTP directory. 
