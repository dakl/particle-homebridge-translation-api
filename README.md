# Development

## Run locally

~~~bash
python run.py
~~~

# Deplotyment

## Build & push

~~~bash
docker build -t dakl/particle-homebridge-translation-api .
docker push dakl/particle-homebridge-translation-api
~~~

## Run Container

~~~bash
docker run \
-e RELAY_HUB_DEVICE_ID=(echo $RELAY_HUB_DEVICE_ID) \
-e LEGO_HOUSE_DEVICE_ID=(echo $LEGO_HOUSE_DEVICE_ID) \
-e PARTICLE_ACCESS_TOKEN=(echo $PARTICLE_ACCESS_TOKEN) \
-p 8000:8000 \
dakl/particle-homebridge-translation-api
~~~