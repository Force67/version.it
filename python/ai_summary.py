import requests
import json
from logging import getLogger

log = getLogger(__name__)

class AISummary:
  """
    Class to generate a summary of Git diffs using OpenAI's ChatGPT Turbo.
    """

  def __init__(self, api_key):
    self.api_key = api_key

  def summarize_text(self, user_prompt, **kwargs):
    """
        Uses OpenAI's API to generate based on info about the repo.
    """
    system_prompt = "You are a helpful assistant. Please be aware of the following variables that give you context about a git repo in the key:value format:\n"
    for key, value in kwargs.items():
      if isinstance(value, dict):
          system_prompt += f"{key}: {value}\n"
      elif isinstance(value, list) or isinstance(value, tuple):
          system_prompt += f"{key}: {', '.join(str(v) for v in value)}\n"
      else:
          system_prompt += f"{key}: {value}\n"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{
            "role": "system",
            "content": system_prompt
        }, {
            "role": "user",
            "content": user_prompt
        }],
        "temperature": 0.3,
        "max_tokens": 150
    }
    try:
      response = requests.post(
          "https://api.openai.com/v1/chat/completions",
          headers=headers,
          timeout=50,
          json=data)
      response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
      log.error("HTTP Error: %s", errh)
      return None
    except requests.exceptions.ConnectionError as errc:
      log.error("Error Connecting: %s", errc)
      return None
    except requests.exceptions.Timeout as errt:
      log.error("Timeout Error: %s", errt)
      return None
    except requests.exceptions.RequestException as err:
      log.error("Something went wrong: %s", err)
      return None

    try:
      response_json = response.json()
      return response_json["choices"][0]["message"]["content"].strip()
    except json.decoder.JSONDecodeError as err:
      log.error("Error decoding JSON: %s", err)
      return None
