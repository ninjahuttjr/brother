import openai
import os
import json
from utils import get_current_datetime, browse_web, search_gif
from dotenv import load_dotenv
from function_descriptions import get_current_datetime_func, browse_web_func, search_gif_func

load_dotenv()  # take environment variables from .env.

openai.api_key = os.environ.get("OPENAI_API_KEY")

def send_message(message_log):
    print("Preparing to send message.")

    print("Sending message to OpenAI API.")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=message_log,
        max_tokens=375,
        stop=None,
        temperature=0.9,
        functions=[get_current_datetime_func, browse_web_func, search_gif_func]
    )

    print("Received response from OpenAI API.")
    for choice in response.choices:
        if "text" in choice:
            return choice.text
        
        elif choice["finish_reason"] == "function_call":
            if choice['message']['function_call']['name'] == "get_current_datetime":
                datetime_str = get_current_datetime()
                message_log.append({"role": "assistant", "content": datetime_str})
                message_log.append({"role": "user", "content": "What can you tell me about this date and time?"})
                datetime_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=message_log,
                    max_tokens=375,
                    stop=None,
                    temperature=0.9
                )
                return datetime_response.choices[0].message['content']
            
            elif choice['message']['function_call']['name'] == "browse_web":
                arguments = json.loads(choice['message']['function_call']['arguments'])
                url = arguments['url']
                webpage_content = browse_web(url)
                print("Adding webpage content to message log.")
                message_log.append({"role": "assistant", "content": webpage_content})
                print("Asking GPT-4 to do something with the content.")
                message_log.append({"role": "user", "content": "Respond to the user's request, which may include asking questions or requesting specific actions (such as translation, rewriting, etc.), based on the provided content. ONLY if the user does not make a specific request for you, perform the following tasks: 1. Display the title in the user's language; 2. Summarize the article content into a brief and easily understandable paragraph; 3. DEPENDING on the content, present three thought-provoking questions or insights with appropriate subheadings. For articles, follow this approach; for code, formulas, or content not suited for questioning, this step may be skipped."})
                summary_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=message_log,
                    max_tokens=375,
                    stop=None,
                    temperature=0.9
                )
                print("Received summary from GPT-4.")
                return summary_response.choices[0].message['content']
            
            elif choice['message']['function_call']['name'] == "search_gif":
                search_term = json.loads(choice['message']['function_call']['arguments'])['search_term']
                gif_url = search_gif(search_term)
                return gif_url
    print("Sending message content.")
    return response.choices[0].message.content
