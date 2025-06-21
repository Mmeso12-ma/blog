# A simple blogging website

### How to set up (using your terminal)
1. ``git clone https://github.com/Mmeso12-ma/blog.git``
2. ``cd blog``
3. ``python -m venv .venv``
4. On Linux or macOS run: ``source .venv/bin/activate``. On windows, run: ``.venv\Scripts\activate``
5. ``pip install -r requirements.txt``
6. To run the backend: ``uvicorn main:app --reload``. To run the frontend: ``streamlit run client.py``.<br>  
**[Important]** To run both at the same time (necessary for full functionality):  
* On Linux or macOS, run: ``uvicorn main:app --reload & streamlit run client.py``\
* On Windows, run with powershell: ``Start-Process powershell -ArgumentList "uvicorn main:app --reload"``, then: 
``Start-Process powershell -ArgumentList "streamlit run client.py"``