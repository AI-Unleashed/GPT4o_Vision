# GPT4o_Vision

Starter code to use new GPT4o vision API to do extract text from an image. Has a file to generate from an internet accessible URL (InvoiceExtract.py) and from a local copy of an image(InvoiceExtract_LocalFile.py).
Step 1: Make sure you have the OpenAI API key environment variable(OPENAI_API_KEY) setup in your environment

- Steps for mac: https://www.patreon.com/posts/setting-up-your-90435028
- Steps for windows: https://www.patreon.com/posts/securely-setting-90627687

Step 2: Install the prerequisite libraries (Just OpenAI for this starter code)

- pip install -r requirements.txt

Step 3: Run it!

- python InvoiceExtract.py
- Should generate a JSON file!
