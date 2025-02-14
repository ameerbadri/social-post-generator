Social Post Generator

Welcome to the Social Post Generator! This application leverages the Writer Framework to generate engaging social media posts, relevant hashtags, and creative images based on a user-defined topic.

Features
	•	Generate Social Media Posts: Create five engaging posts about a specified topic, complete with emojis.
	•	Generate Hashtags: Produce around five relevant hashtags for the given topic.
	•	Generate Images: Create a creative image related to the topic using OpenAI’s image generation capabilities.

Prerequisites

Before running the application, ensure you have the following:
	•	Python 3.9.2 or higher: The application is built using Python and requires version 3.9.2 or above.
	•	Writer Framework: An open-source Python framework for building feature-rich apps.
	•	API Keys: You need API keys for both Writer and OpenAI services.

Installation
	1.	Set Up a Virtual Environment (Optional but recommended):
	•	Create a virtual environment:

python3 -m venv venv


	•	Activate the virtual environment:
	•	On Windows:

venv\Scripts\activate


	•	On macOS and Linux:

source venv/bin/activate


	2.	Install the Writer Framework:
	•	Use pip to install the Writer Framework:

pip install writer


	3.	Set Up Environment Variables:
	•	Create a .env file in the root directory of your project.
	•	Add your API keys to the .env file in the following format:

WRITER_API_KEY=your_writer_api_key
OPENAI_API_KEY=your_openai_api_key

Replace your_writer_api_key and your_openai_api_key with your actual API keys.

Usage
	1.	Create a New Application:
	•	Use the Writer Framework to create a new application named social-post-generator:

writer create social-post-generator


	2.	Navigate to the Application Directory:
	•	Change to the application’s directory:

cd social-post-generator


	3.	Add the Provided Code:
	•	Replace the contents of the main.py file in your application directory with the provided code.
	4.	Start the Visual Editor:
	•	Launch the Writer Framework’s visual editor:

writer edit social-post-generator


	•	This command opens the visual editor in your default web browser, allowing you to design and customize your application’s user interface.

	5.	Run the Application Locally:
	•	After setting up the UI and ensuring everything is in place, run the application:

writer run social-post-generator


	•	By default, the application will be accessible at http://localhost:3005.

Deployment

To deploy your application to the Writer Cloud:
	1.	Deploy to Writer Cloud:
	•	Use the deploy command:

writer deploy social-post-generator


	•	You will be prompted to enter your Writer API key during this process.

For more detailed deployment options, including using Docker, refer to the Writer Framework Deployment Documentation.

Additional Resources
	•	Writer Framework Documentation: https://dev.writer.com/framework/introduction
	•	Writer API Documentation: https://dev.writer.com/api-guides/introduction
	•	OpenAI API Documentation: https://platform.openai.com/docs/introduction

For further assistance, consider exploring the Writer Framework Tutorials Repository for sample applications and tutorials.

Note: Ensure that your API keys are kept secure and not exposed in public repositories or shared environments.