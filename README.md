# Cold Mail Generator for Job Applications

This project is a Cold Mail Generator built with Streamlit and Langchain. It helps users automatically generate personalized cold emails for job applications by extracting relevant job information from a provided URL. The generated emails include personalized links to a user's portfolio based on the required skills for the job.

## Project Overview

The Cold Mail Generator is designed to assist freshers and unemployed people in applying for jobs effectively. Users can enter a job URL, and the application will extract relevant job details such as skills required and job description, then generate a tailored cold email for them to send to employers. This email includes links to the user's portfolio that match the required skills.

## Features

- **URL Input:** Allows the user to provide a job URL to extract job details.
- **Personalization:** Users can input their name, designation, and company name for a personalized email.
- **Cold Email Generation:** Automatically generates a cold email based on the job details and user's portfolio.
- **Portfolio Integration:** Links to the user’s portfolio are added based on the skills required by the job.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cold-mail-generator.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd cold-mail-generator
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Files and Directories

- **chains.py:** Contains the Chain class used to handle the job extraction and email generation logic.
- **portfolio.py:** Contains the Portfolio class which manages portfolio links based on job skills.
- **utils.py:** Contains utility functions like `clean_text` for text processing.
- **app.py:** Main Streamlit app file where users interact with the interface.
- **requirements.txt:** Lists the required Python packages to run the project.

## How to Use

1. **Launch the Streamlit app:** Run the following command to start the Streamlit app in your browser:

   ```bash
   streamlit run app.py
   ```

2. **Enter Job URL:** Provide the URL of the job posting (e.g., from a company website).

3. **Personalize the Email:** Fill in your name, designation, and company name.

4. **Submit:** Click on the Submit button to generate a personalized cold email.

5. **View the Email:** The generated cold email, along with relevant portfolio links based on the job’s required skills, will be displayed in the Streamlit interface.

## Example Use Case

1. Enter a job URL such as `https://jobs.nike.com/job/R-43533?from=job%20search%20funnel`.
2. Enter your name, designation, and compan
