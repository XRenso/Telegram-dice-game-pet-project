FROM python:3.11.8
ENV TOKEN="Your TOKEN"
WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "run.py"]