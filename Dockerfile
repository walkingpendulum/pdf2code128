FROM python:3.8
RUN apt-get update && apt-get install -y python-zbar=0.22-1 poppler-utils=0.71.0-5

RUN mkdir -p /opt/pdf2code128
WORKDIR /opt/pdf2code128

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD decode_code128_from_pdf.py decode_code128_from_pdf.py
ADD app.py app.py

CMD python3 /opt/pdf2code128/app.py
