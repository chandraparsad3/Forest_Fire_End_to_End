
# FWI Prediction Flask App

## Project Overview

This Flask application predicts the Fire Weather Index (FWI) based on various environmental factors like temperature, relative humidity (RH), wind speed (Ws), and more. The app leverages a pre-trained Ridge Regression model and a StandardScaler for accurate predictions.

## Features

- **Web Interface:** User-friendly HTML form to input environmental data.
- **FWI Prediction:** The app predicts the FWI based on the provided data.
- **Model Integration:** Utilizes a pre-trained Ridge Regression model for prediction.
- **Data Scaling:** Features are scaled using a pre-fitted StandardScaler to ensure consistency.

## Project Structure

```
├── app.py               # Main Flask application file
├── models/
│   ├── ridge.pkl        # Trained Ridge Regression model
│   ├── scaler.pkl       # Pre-fitted StandardScaler
├── templates/
│   ├── index.html       # HTML form for user input
│   ├── home.html        # HTML page to display prediction result
├── README.md            # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- `scikit-learn`

### Installing Dependencies

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository and navigate to the project directory.
2. Start the Flask application with:

   ```bash
   python app.py
   ```

3. To access your Flask application, open a new tab and paste the URL:

   ```
   https://{your_url}.pwskills.app:5000/
   ```

## Application Workflow

1. **Home Page (`/`):** Displays a simple "Hello, World!" message.
2. **Input Form (`/`):** Collects environmental data inputs such as Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, and Region.
3. **Prediction (`/predictdata`):** After form submission:
   - The app retrieves the input values.
   - Scales the data using the StandardScaler.
   - Predicts the FWI using the Ridge Regression model.
   - Displays the prediction result.

### Future Enhancements

- Implement input validation.
- Enhance UI/UX design.
- Include visualizations of prediction data.
- Add exception handling for improved robustness.

