from openai import OpenAI
import base64
import json
import os
from urllib.parse import urlparse

client = OpenAI()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def load_json_schema(schema_file: str) -> dict:
    with open(schema_file, 'r') as file:
        return json.load(file)


mode = 'URL'  # different logic for URL or LocalFile
#https://images.ehive.com/accounts/5831/objects/images/gb3v5i_93nt_l.jpg
image_url = 'https://www.invoicesimple.com/wp-content/uploads/2018/06/Sample-Invoice-printable.png'
local_path = ''
invoice_schema = load_json_schema('invoice_schema.json')
response = client.chat.completions.create(
    model='gpt-4o',
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "provide JSON file that represents this document. Use this JSON Schema: " +
                    json.dumps(invoice_schema)},
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            ],
        }
    ],
    max_tokens=500,
)

# Extract JSON data from the response and remove Markdown formatting
# json_string = response.choices[0].message.content
# json_string = json_string.replace("```json\n", "").replace("\n```", "")

# Parse the string into a JSON object
# json_data = json.loads(json_string)

json_data = json.loads(response.choices[0].message.content)

# Determine the filename based on File_Mode
if mode == "URL":
    filename_without_extension = os.path.splitext(
        os.path.basename(urlparse(image_url).path))[0]
else:  # Local file mode
    filename_without_extension = os.path.splitext(
        os.path.basename(local_path))[0]

# Add .json extension to the filename
json_filename = f"{filename_without_extension}.json"

# Save the JSON data to a file with proper formatting
with open(json_filename, 'w') as file:
    json.dump(json_data, file, indent=4)

print(f"JSON data saved to {json_filename}")

# print(response.choices[0].message.content)

# print(response.choices[0])
# https://cdn.create.microsoft.com/catalog-assets/en-us/ddd47a54-4900-42d5-91b4-cf48da993f99/thumbnails/600/sales-invoice-modern-simple-1-1-bd227c3e7767.webp
# https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/02/19/ML-1955-2.jpg
# f"data:image/jpeg;base64,{base64_image}"
