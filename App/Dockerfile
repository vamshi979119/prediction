FROM python:3.8
WORKDIR /usr/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN wget https://20tree-public.s3-eu-west-1.amazonaws.com/candidates/utils.py
RUN wget https://20tree-public.s3-eu-west-1.amazonaws.com/candidates/live_model.pickle
RUN wget -O image.tif https://20tree-public.s3-eu-west-1.amazonaws.com/candidates/cloudmask/Sentinel2L2A_sen2cor_18TUR_20180812_clouds=5.3%_area=99%.tif
RUN mkdir data
COPY . .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]