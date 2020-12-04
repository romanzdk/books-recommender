FROM python

COPY . /recommender/
EXPOSE 5000
RUN pip install -r /recommender/requirements.txt
WORKDIR /recommender/
CMD [ "python", "app.py"]