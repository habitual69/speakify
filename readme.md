# Speakify

Speakify is a web application that uses Edge TTS to convert text to speech using a variety of voices.

# Demo Site
[Speakify](https://speakify.vpms.xyz).

## Installation

To run the Speakify app locally, you'll need to have Python 3.9 and pip installed on your machine. Clone the project repository, navigate to the project folder, and install the required Python packages by running:

```
pip install -r requirements.txt
```

## Usage

To start the Speakify app, run:

```
python3 main.py
```

This will start the app server and automatically reload the server whenever changes are made to the Python code.

You can access the app by visiting `http://localhost:8000` in your web browser.

## Docker

Alternatively, you can run the Speakify app using Docker. To build a Docker image, navigate to the project folder and run:

```
docker build -t speakify .
```

Once the image has been built, you can start a container from it with:

```
docker run -p 8000:8000 speakify
```

This will start a new container and map port 8000 in the container to port 8000 on your local machine. You can access the app by visiting `http://localhost:8000` in your web browser.

## Contributing

If you'd like to contribute to Speakify, please fork the repository, make your changes, and submit a pull request. We welcome contributions of all kinds, including bug fixes, feature additions, documentation improvements, and more.

## Credits

Speakify was created by [habitual69]. The app uses Edge TTS for text-to-speech conversion.

## License

Speakify is licensed under the [MIT License](https://github.com/your-username/speakify/blob/main/LICENSE).