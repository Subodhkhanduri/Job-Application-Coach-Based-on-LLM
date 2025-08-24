# Job-Application-Coach-Based-on-LLM

## Overview

The projects leverage IBM watsonx.ai large language models, specifically the Llama 3 series, to build AI-powered applications such as:

- Resume Polisher
- Cover Letter Generator
- Career Advisor

These applications demonstrate how to integrate IBM watsonx.ai models with Python and Gradio to create interactive AI tools.

## Environment

All development and testing were performed in IBM's **Cloud IDE Kubernetes** environment, which provides:

- Pre-configured access to IBM watsonx.ai APIs with necessary credentials.
- Python 3.11 runtime.
- Support for popular libraries including `ibm_watsonx_ai` and `gradio`..

## Getting Started

1. Clone this repository to your local machine or Cloud IDE environment.
2. Install required Python packages (if running locally):

   ```bash
   pip install ibm-watsonx-ai gradio
Run any of the provided scripts, for example:



python3.11 resumepolisher.py
Use the Gradio interface to interact with the AI-powered applications.

Project Structure
resumepolisher.py — Polishes resumes based on position and optional instructions.
cover_letter.py — Generates customized cover letters tailored to job descriptions.
career_advisor.py — Provides personalized career advice based on resume and job details.
Notes
The IBM watsonx.ai credentials and project ID are pre-configured for the Cloud IDE Kubernetes environment.
If you want to run these projects outside the Cloud IDE, you will need to set up your own IBM watsonx.ai credentials and update the code accordingly.
Resources
IBM watsonx.ai Documentation
Building Generative AI-Powered Applications with Python - Course
Feel free to contribute or raise issues to improve these AI-powered applications!
