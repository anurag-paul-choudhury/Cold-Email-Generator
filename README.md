# Cold Email Generator

An AI-powered tool for service-based outreach using Groq, LangChain, and Streamlit.  
Users provide a company careers page URL, and the tool extracts job listings to generate personalized cold emails.  
Emails are enriched with relevant portfolio links retrieved from a vector database, tailored to each job description.

---

## Example Scenario

- A company needs a software engineer and is spending time and resources in the hiring process.  
- Your tool can generate a professional cold email for outreach to that company, including portfolio links or relevant information.

![alt text](image.png)

## Features

- Automatically extract job listings from a company’s careers page
- Generate highly personalized cold emails tailored to specific job descriptions
- Enrich emails with relevant portfolio links or project samples from a vector database
- Streamlit-based interactive UI for quick testing and iteration
- Secure handling of API keys through `.env` files
- Easy integration into business development workflows


## Installation

1. **Clone the repository**

```bash
git clone https://github.com/anurag-paul-choudhury/Cold-Email-Generator.git
cd Cold-Email-Generator

2. Create a virtual environment (recommended)

python -m venv venv

3. Activate the environment

- Windows:

    venv\Scripts\activate


- macOS/Linux:

    source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Setup API Key

Copy the template .env.example to .env:

cp .env.example .env


Open .env and add your Groq API key:

GROQ_API_KEY=your_api_key_here


Note: Do not commit your .env file to GitHub. Use .env.example as a template.

6. Run the Streamlit app
streamlit run email_generator.ipynb


Open the URL displayed in your terminal (usually http://localhost:8501)

Enter prompts and generate cold emails instantly


## Author

Anurag Paul Choudhury  
[GitHub](https://github.com/anurag-paul-choudhury)

