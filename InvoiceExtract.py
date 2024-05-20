from openai import OpenAI
import json
import os
from urllib.parse import urlparse

client = OpenAI()

def load_json_schema(schema_file: str) -> dict:
    with open(schema_file, 'r') as file:
        return json.load(file)

image_url = 'https://www.invoicesimple.com/wp-content/uploads/2018/06/Sample-Invoice-printable.png'


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
filename_without_extension = os.path.splitext(os.path.basename(urlparse(image_url).path))[0]
json_filename = f"{filename_without_extension}.json"

with open(json_filename, 'w') as file:
    json.dump(json_data, file, indent=4)

print(f"JSON data saved to {json_filename}")