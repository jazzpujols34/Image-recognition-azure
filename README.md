# Image Recognition with Azure Custom Vision

This web application uses Azure Custom Vision to recognize and classify images. Users can upload an image, and the application will display the predicted class along with the confidence level. The application also allows users to provide feedback on the predictions and view the prediction history.

## Features

- Image classification using Azure Custom Vision
- Feedback submission for predictions
- Prediction history
- Image tagging

## Installation and Setup

1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Activate the virtual environment using `env\Scripts\activate` (Windows) or `source env/bin/activate` (Linux/Mac).
4. Run the application using `python app.py`.

## Project Structure

- `app.py`: The main application file containing the Flask routes and the logic for image recognition and classification using Azure Custom Vision.
- `static`: Contains static files such as uploaded images.
- `templates`: Contains the HTML templates for the different pages in the application.
- `.gitignore.txt`: Specifies files and directories to be ignored by Git.
- `Procfile`: Configuration file for deployment on a platform like Heroku.
- `requirements.txt`: Lists the required Python packages for the project.
- `startup.txt`: Instructions for starting the application.
- `web.config`: Configuration file for deployment on a platform like Azure Web Apps.

## Usage

1. Run the application locally using `python app.py`.
2. Open your browser and go to `http://localhost:5000`.
3. Upload an image, and the application will display the predicted class along with the confidence level.
4. You can provide feedback on the predictions and view the prediction history.

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).
