# pdf2code128
Extract and decode code128 data from pdf files.

## Build docker image
```bash
$ docker build -t pdf2code128 .
```

## Run web service locally via docker
```bash
$ docker run -p 8080:8080 -e SECRET_TOKEN=API_TOKEN_HERE pdf2code128
```

Then you send pdf files to `localhost:8080/`

## Send pdf to service via cURL
```bash
$ curl -F 'data=@/path/to/pdf' -H 'Authorization: Bearer API_TOKEN_HERE' https://pdf2code128.herokuapp.com/decode
```

## Decode pdf locally via cli and docker
```bash
$ docker run -v /path/to/data:/data pdf2code128 ./decode_code128_from_pdf.py /data/file.pdf
```

