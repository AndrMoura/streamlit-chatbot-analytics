# Streamlit Chatbot Application

This repository contains a Streamlit-based chatbot application that leverages the Ollama with the Langchain library and integrates [PostHog-LLM](https://github.com/postlang/posthog-llm) for analytics and monitoring. 

![My Animation](img/Animation.gif)

# Features
     
*  AI Chatbot: Uses Ollama with Langchain.
*  Integration with PostHog-LLM: Enables detailed monitoring of chatbot interactions.
*  Simple UI: Built with Streamlit for an easy-to-navigate user interface.

# Installation

## Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/AndrMoura/streamlit-chatbot-analytics.git
cd streamlit-chatbot-analytics
```

## Create a Virtual Environment

Create a new virtual environment using `venv`:

```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:

```bash
venv\Scripts\activate
```

For macOS and Linux:

```bash
source venv/bin/activate
```

## Install Dependencies

Install the necessary Python packages in requirements.txt:

```bash
pip install -r requirements.txt
```

# Install PostHog-LLM

Run the following command to install PostHog-LLM for monitoring:
```bash
sudo  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/postlang/posthog-llm/HEAD/bin/deploy-hobby)"
```

After a few minutes your PostHog-LLM instance will be available at https://localhost. Create your account and project grab your API key and export the following environment variables:

```bash
export POSTHOG_HOST='http://localhost'
export POSTHOG_API_KEY='UNDER_SETTINGS_PAGE'
```

# Install Ollama and download Llama3 model
Go to Ollama [website](https://ollama.com) and install for your OS. After installation, download the Llama3 8b model:

```bash
ollama run llama3
```

# Running the ChatBot Application
Run the application using Streamlit:

```bash
streamlit run streamlit/app.py
```

# Usage
After starting the application, navigate to the provided local URL (http://localhost:8501) in your web browser to interact with the chatbot.

Check the PostHog-LLM instance in the activity page to monitor the chatbot interactions.