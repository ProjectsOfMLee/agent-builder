import requests
from requests.auth import HTTPBasicAuth
import os

# Replace these with your actual Confluence credentials and URL
CONFLUENCE_URL = 'https://your-confluence-instance.atlassian.net/wiki/rest/api'
USERNAME = 'your-email@example.com'
API_TOKEN = 'your-api-token'

SPACE_KEY = 'CaaS'
SPACE_TITLE = 'CaaS Environment'

def get_page_id(space_key, title):
  url = f"{CONFLUENCE_URL}/content"
  params = {
    'spaceKey': space_key,
    'title': title,
    'expand': 'body.storage'
  }
  response = requests.get(url, params=params, auth=HTTPBasicAuth(USERNAME, API_TOKEN))
  response.raise_for_status()
  results = response.json().get('results', [])
  if not results:
    raise Exception(f"Page with title '{title}' not found in space '{space_key}'")
  return results[0]['id']

def get_page_content(page_id):
  url = f"{CONFLUENCE_URL}/content/{page_id}?expand=body.storage"
  response = requests.get(url, auth=HTTPBasicAuth(USERNAME, API_TOKEN))
  response.raise_for_status()
  return response.json()

def save_page_content_to_file(page_content, file_path):
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(page_content['body']['storage']['value'])

def download_page_and_children(page_id, parent_dir):
  page_content = get_page_content(page_id)
  page_title = page_content['title']
  page_dir = os.path.join(parent_dir, page_title)
  os.makedirs(page_dir, exist_ok=True)
  save_page_content_to_file(page_content, os.path.join(page_dir, 'content.html'))

  # Get children pages
  url = f"{CONFLUENCE_URL}/content/{page_id}/child/page"
  response = requests.get(url, auth=HTTPBasicAuth(USERNAME, API_TOKEN))
  response.raise_for_status()
  children = response.json().get('results', [])
  
  for child in children:
    download_page_and_children(child['id'], page_dir)

def main():
  try:
    url = f"{CONFLUENCE_URL}/content"
    params = {
      'spaceKey': SPACE_KEY,
      'type': 'page',
      'expand': 'body.storage'
    }
    response = requests.get(url, params=params, auth=HTTPBasicAuth(USERNAME, API_TOKEN))
    response.raise_for_status()
    pages = response.json().get('results', [])
    
    for page in pages:
      page_id = page['id']
      download_page_and_children(page_id, '/path/to/save/directory')
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()