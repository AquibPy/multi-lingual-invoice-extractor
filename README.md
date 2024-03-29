# Multi-Lingual Invoice Extraction using Google Gemini Pro Vision

This FastAPI application utilizes the Google Gemini Pro Vision API to perform multi-lingual invoice extraction. Users can upload invoice images, provide prompts, and receive responses based on the content generated by the Google Generative AI model.

## Overview

The application is designed to assist users in understanding invoices in multiple languages. It leverages the capabilities of Google Gemini Pro Vision to process input images of invoices and answer questions based on the extracted information.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerization)

### Installation

1. **Clone the repository:**

    ```bash
        git clone https://github.com/AquibPy/multi-linguil-invoice-extractor.git
    ```

2. **Navigate to the project directory**


3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Create a `.env` file in the project root directory.**

2. **Add your Google API key to the `.env` file:**

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

    Replace `your_google_api_key_here` with your actual Google API key.

### Running the Application

You can run the FastAPI application using Uvicorn:

```bash
uvicorn api:app --reload
```

You can also run Streamlit app:

```bash
streamlit run main.py
```


Go to this url http://127.0.0.1:8000/docs#/
