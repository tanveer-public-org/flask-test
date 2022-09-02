# Python-flask

# Flask Application

## Tested by Amnic 
following are different scenarios of Flask application tested on amnic platform.

### With Secret and Config
![Screenshot](/screenshots/3.8-2.1%20secret%20config.png?raw=true)

### With Only Secret

![Screenshot](/screenshots/3.8-2.1%20secret.png?raw=true)


### With Only Config

![Screenshot](/screenshots/3.8-2.1%20config.png?raw=true)

### Without secret and config

![Screenshot](/screenshots/3.8-2.1.png?raw=true)

### Unittest and Code Coverage

![Screenshot](/screenshots/py-3.8_fl-2.1.png?raw=true)

## Docker build and run commands

```docker build -t <image_name> .```

```docker run --rm  -p 8092:5000 <image-name> ```

## Buildpack

To use buildpack and create images using different builders.

### Heroko

To create image using heroko you must have "runtime.txt" for specific runtime vesrion(python) and Procfile to provide entrypoint. in our branch we have runtime.txt and procfile, we can build the image using following command.

Build the image:
``` pack build <image_name> -B heroku/buildpacks:20 ```

Run the created image:

```docker run --rm -p 8098:5000 <image name>```

Note: use "--platform linux/amd64" only if you are on mac M1.

### Paketo

To create image using Paketo you must have Procfile for entrypoint and we have to use "--env BP_CPYTHON_VERSION=3.8.13" to provide the desired python vesrion.

Build the image:

```pack build <image_name> --env BP_CPYTHON_VERSION=3.8.13 -B paketobuildpacks/builder:base```

Run the created image:

```docker run --rm -p 8092:5000 <image name >```

### Google

To create iamge using google builder we must have Procfile present which we have and we must provide "--env  GOOGLE_RUNTIME_VERSION="3.7.1" for desired python version.

Build the image:

``` pack build <image_name> --env  GOOGLE_RUNTIME_VERSION="3.7.1"  -B gcr.io/buildpacks/builder:v1 ```

Run the image:

```docker run <image_name> -p 8092:8080 <image_name>```

Note: Google runs its server on 8080 so we have to forward the 8080 port to access the app.