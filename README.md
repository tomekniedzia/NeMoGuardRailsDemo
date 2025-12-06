# Project Setup Guide
This project uses separate virtual environments and applications:
- **Groq-based application** (`groq_app`)

Both LangChain and NeMoGuardrails rely on **Pydantic V1**, which requires Python versions **3.10–3.12**.  
This project uses **Python 3.11.9**.

### Create virtual environments
Create a virtual environment for the Groq application:  
`py -3.11 -m venv groq_env`

### Activating the environments
`groq_env\Scripts\activate`

### Installing dependencies
`cd groq_app`  
Application has its own requirements.txt.  
Install dependencies inside the activated environment  
`pip install -r requirements.txt`

### Running the applications
`python chat.py`

### Finish working
To close chat: `end`  
To close the virtual environment: `deactivate`