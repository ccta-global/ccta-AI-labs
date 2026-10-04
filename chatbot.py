from client import client
from prompt import SYSTEM_PROMPT
#Below is for runniong locally with the model, you can uncomment it and run it in your local environment.
# messages=[
#       {
#           "role": "system",
#           "content": SYSTEM_PROMPT
#       },
#       {
#         "role": "user",
#         "content": "Hello, how are you?"
#       }
# ]
# completion = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=messages,
#     temperature=1,
#     max_completion_tokens=2048,
#     top_p=1,
#     reasoning_effort="medium",
#     stream=False,
#     stop=None
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")

# print(completion.choices[0].message.content)

# assistant_response = completion.choices[0].message.content
# messages.append({
#    "role": "assistant", 
#    "content": assistant_response
# })

# print(assistant_response)



#Continously stream the response from the model
# while True:
#    user_input = input("User: ")
#    messages.append({"role": "user", "content": user_input})
#    completion = client.chat.completions.create(
#       model="openai/gpt-oss-120b",
#       messages=messages, 
#       temperature=1, 
#       max_completion_tokens=2048, 
#       top_p=1, 
#       reasoning_effort="medium", 
#       stream=False
#   )
#    assistant_response = completion.choices[0].message.content
#    messages.append({"role": "assistant", "content": assistant_response})
#    print("Assistant: " + assistant_response)



messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def get_response(messages):

    # messages.append({
    #     "role": "user",
    #     "content": user_input
    # })

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False
    )

    assistant_response = completion.choices[0].message.content

    return assistant_response

