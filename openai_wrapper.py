import openai
import tiktoken
import time
import json

with open("key_openai.txt") as f:
  openai.api_key=f.read().strip()

messages=[]
functions=[]

# functions = [
# {
#     "name": "describe_opportunity",
#     "description": "Describe an opportunity",
#     "parameters": {
#       "type": "object",
#       "properties": {
#           "OpportunityName": {
#               "type": "string",
#               "description": "Name of the opportunity"
#           },
#           "BusinessFunction": {
#               "type": "string",
#               "description": "Function of the business related to the opportunity"
#           },
#           "TechnologyUsed": {
#               "type": "string",
#               "description": "Technology used in the opportunity"
#           },
#           "OpportunityDescription": {
#               "type": "string",
#               "description": "Description of the opportunity"
#           },
#           "OpportunityBenefits": {
#               "type": "array",
#               "description": "List of benefits of the opportunity",
#               "items": {
#                   "type": "string"
#               }
#           }
#       }
#     },
#     "required": ["OpportunityName", "BusinessFunction", "TechnologyUsed", "OpportunityDescription", "OpportunityBenefits"]
# }
# ]
# with open("function.json","w") as f:
#   f.write(json.dumps(functions, indent=4))

def append_message_log(role, content):
  messages.append(construct_message(role,content))

def construct_message(role,content):
  return {"role": role, "content": content}

def count_tokens(text,model):
  encoding = tiktoken.encoding_for_model(model)
  encodings=encoding.encode(text)
  return len(encodings)

def send_message(message_log,model,max_tokens=256,temperature=0.7):
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    # only send role and content
    transformed_log = [{"role": msg["role"], "content": msg["content"]} for msg in message_log]
    #print(message_log)
    try:
        response = openai.ChatCompletion.create(
            model=model,   #"gpt-4",  # The name of the OpenAI chatbot model to use
            messages=transformed_log,   # The conversation history up to this point, as a list of dictionaries
            max_tokens=max_tokens,        # The maximum number of tokens (words or subwords) in the generated response
            stop=None,              # The stopping sequence for the generated response, if any (not used here)
            temperature=temperature,        # The "creativity" of the generated response (higher temperature = more creative)
            functions=functions, # The functions
            function_call="auto"
        )

        response_message = response["choices"][0]["message"]
        if response_message.get("function_call"):
          response_message["function_call"]["name"]
          return response_message["function_call"]["arguments"]
        else :
          # If no response with text is found, return the first response's content (which may be empty)
          return response.choices[0].message.content
    except openai.error.RateLimitError as e:
        wait_duration = int(e.headers.get('Retry-After', 10))
        print(f"Rate limited. Retrying in {wait_duration} seconds. Attempt {retries + 1} of {max_retries}.")
        time.sleep(wait_duration)
        retries += 1

    raise Exception("Max retries reached. Unable to complete the API request.")