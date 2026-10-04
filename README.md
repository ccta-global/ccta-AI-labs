# Groq Chatbot - Python Backend

This README explains the **Python code used to build the chatbot** with the Groq API.

> **Scope:** This document covers only the Python/chatbot part of the project.  
> The Flask web interface, HTML, CSS, and JavaScript are intentionally not covered.

---

## 1. Project Overview

This project is a simple Python chatbot powered by the **Groq API** and the model:

```text
openai/gpt-oss-120b
```

The Python code is responsible for:

1. Creating a connection to Groq.
2. Defining the system prompt.
3. Maintaining the conversation messages.
4. Sending messages to the Groq model.
5. Receiving the model's response.
6. Returning the assistant response to the application.

The basic flow is:

```text
User Input
    ↓
messages list
    ↓
get_response()
    ↓
Groq API
    ↓
GPT-OSS-120B
    ↓
Assistant Response
```

---

# 2. Project Structure

The Python part of the project contains these files:

```text
Groq chatbot/
│
├── client.py
├── prompt.py
├── chatbot.py
└── README.md
```

Each file has a separate responsibility.

| File | Purpose |
|---|---|
| `client.py` | Creates the Groq API client |
| `prompt.py` | Contains the chatbot's system prompt |
| `chatbot.py` | Contains the chatbot logic and calls the model |
| `README.md` | Documentation |

---

# 3. Installation

Make sure you have Python installed.

A virtual environment is recommended.

For example:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the Groq Python package:

```powershell
python -m pip install groq
```

If you are using `uv`, you can also install the package with:

```powershell
uv pip install groq
```

---

# 4. Groq API Key

The chatbot needs a Groq API key to communicate with the Groq API.

A common approach is to store the key in an environment variable instead of writing it directly in the Python source code.

For PowerShell:

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

Do **not** upload your API key to GitHub.

Never write a real API key in:

```text
client.py
README.md
GitHub
```

---

# 5. client.py

The purpose of `client.py` is to create the Groq client.

Example:

```python
from groq import Groq

client = Groq()
```

The `Groq()` client reads the API key from the environment.

The rest of the application can then import this client:

```python
from client import client
```

This keeps the API connection setup separate from the chatbot logic.

---

# 6. prompt.py

The system prompt defines how the AI should behave.

Example:

```python
SYSTEM_PROMPT = "You are a helpful assistant."
```

The system prompt is different from a normal user message.

For example:

```text
System:
You are a helpful assistant.

User:
What is Python?
```

The system message gives instructions to the model, while the user message contains the actual question.

---

# 7. Understanding Messages

The Groq chat API uses a list of message objects.

A message has two important fields:

```python
{
    "role": "user",
    "content": "Hello"
}
```

### Role

The `role` tells the model who sent the message.

Common roles are:

```text
system
user
assistant
```

### Content

`content` contains the actual text.

For example:

```python
{
    "role": "user",
    "content": "What is Python?"
}
```

---

# 8. Conversation History

A chatbot needs to remember previous messages.

This is done by sending the conversation history to the model.

Example:

```python
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I help you?"
    },
    {
        "role": "user",
        "content": "What is Python?"
    }
]
```

The model can use the previous messages as context when generating the next response.

This is why a chatbot can have a conversation instead of treating every question as completely independent.

---

# 9. chatbot.py

The main chatbot logic is placed in `chatbot.py`.

A simplified version is:

```python
from client import client

def get_response(messages):
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
```

Let's understand this step by step.

---

# 10. Importing the Client

```python
from client import client
```

This imports the Groq client created in `client.py`.

Instead of creating the client again, `chatbot.py` reuses it.

---

# 11. get_response()

The function:

```python
def get_response(messages):
```

takes the conversation history as input.

For example:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What is Python?"
    }
]
```

The function sends these messages to the model.

---

# 12. Calling the Groq API

The most important part is:

```python
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=False
)
```

This sends a request to the Groq API.

---

# 13. Model

```python
model="openai/gpt-oss-120b"
```

This tells Groq which model should generate the answer.

The model receives the messages and generates an assistant response.

---

# 14. messages

```python
messages=messages
```

This sends the conversation history to the model.

For example:

```python
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What is Python?"
    }
]
```

The model uses this information as context.

---

# 15. Temperature

```python
temperature=1
```

Temperature controls how predictable or varied the model's responses can be.

Generally:

```text
Lower temperature
        ↓
More predictable / consistent responses

Higher temperature
        ↓
More varied / creative responses
```

For example:

```text
temperature=0.2
```

can produce more consistent answers.

While:

```text
temperature=1
```

allows more variation.

---

# 16. max_completion_tokens

```python
max_completion_tokens=2048
```

This controls the maximum number of tokens the model can generate in the completion.

It does not mean that every response will contain 2048 tokens.

It is a limit.

For example:

```text
Short question
    ↓
Short answer

Complex question
    ↓
Longer answer
```

The model can generate fewer tokens than the maximum.

---

# 17. top_p

```python
top_p=1
```

`top_p` controls the set of possible tokens considered by the model using nucleus sampling.

A simple way to understand it:

```text
top_p = 1
    ↓
Consider the full probability distribution

smaller top_p
    ↓
Consider a smaller high-probability set
```

For basic chatbot development, it is usually better to change either `temperature` or `top_p` rather than changing both aggressively at the same time.

---

# 18. reasoning_effort

```python
reasoning_effort="medium"
```

This controls the requested level of reasoning effort supported by the model/API configuration.

Conceptually:

```text
Lower reasoning effort
        ↓
Faster / less reasoning

Higher reasoning effort
        ↓
More reasoning for complex tasks
```

The appropriate setting depends on the model and task.

---

# 19. stream=False

```python
stream=False
```

This tells the API to return the completion as one response instead of sending it incrementally.

With:

```python
stream=False
```

we can access the final response like this:

```python
completion.choices[0].message.content
```

With:

```python
stream=True
```

the API returns an iterable stream of chunks, so the response must be collected by iterating through those chunks.

For the current simple chatbot implementation, `stream=False` keeps the code easier to understand.

---

# 20. Getting the Assistant Response

After the API returns the completion:

```python
assistant_response = completion.choices[0].message.content
```

This extracts the generated text.

The structure can be thought of as:

```text
completion
    ↓
choices
    ↓
first choice [0]
    ↓
message
    ↓
content
    ↓
actual assistant text
```

For example:

```text
completion
    └── choices
          └── [0]
               └── message
                    └── content
                         └── "Python is a programming language..."
```

---

# 21. Returning the Response

Finally:

```python
return assistant_response
```

returns the generated text to the code that called `get_response()`.

For example:

```python
response = get_response(messages)

print(response)
```

The output could be:

```text
Python is a high-level programming language...
```

---

# 22. Complete chatbot.py

A clean version of the current Python chatbot logic is:

```python
from client import client


def get_response(messages):
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
```

---

# 23. Complete Basic Example

You can also test the chatbot without a web interface.

Example:

```python
from client import client
from prompt import SYSTEM_PROMPT


messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": "Hello, how are you?"
    }
]


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

print(assistant_response)
```

This is the basic idea behind the chatbot.

---

# 24. How a Conversation Works

Suppose the user sends:

```text
Hello
```

The application creates:

```python
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hello"
    }
]
```

The model might respond:

```text
Hello! How can I help you?
```

The response can then be added to the history:

```python
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I help you?"
    }
]
```

If the user then asks:

```text
What can you do?
```

the new message is added:

```python
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I help you?"
    },
    {
        "role": "user",
        "content": "What can you do?"
    }
]
```

The complete history is sent to the model.

This is what gives the chatbot conversational context.

---

# 25. Streaming vs Non-Streaming

There are two common ways to receive a response.

## Non-streaming

```python
stream=False
```

The application waits for the response and then receives it.

Conceptually:

```text
Request
   ↓
Wait
   ↓
Complete response
```

This is easier to understand and is currently used in this project.

## Streaming

```python
stream=True
```

The model response arrives in pieces called chunks.

Conceptually:

```text
Request
   ↓
Chunk 1
   ↓
Chunk 2
   ↓
Chunk 3
   ↓
Chunk 4
   ↓
Complete response
```

With streaming, you normally process the chunks:

```python
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    stream=True
)

for chunk in completion:
    content = chunk.choices[0].delta.content

    if content:
        print(content, end="")
```

Streaming is useful for a UI where you want the answer to appear progressively.

---

# 26. Important Difference: Message vs Messages

This is an important concept when building the chatbot.

### One message

```python
{
    "role": "user",
    "content": "Hello"
}
```

### Multiple messages

```python
[
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hello"
    }
]
```

The API's `messages` parameter expects a list of message objects.

Each individual message's `content` should normally be the actual content, such as a string.

Do not accidentally do this:

```python
{
    "role": "user",
    "content": messages
}
```

when `messages` is already a list.

That would put the entire conversation list inside the `content` field and can cause an API validation error.

---

# 27. Common Errors

## Error: `messages.2.content must be a string`

This usually means a list or another incorrect data type was placed inside a message's `content`.

Incorrect:

```python
{
    "role": "user",
    "content": messages
}
```

Correct:

```python
{
    "role": "user",
    "content": "Hello"
}
```

---

## Error: `'tuple' object has no attribute 'choices'`

This means the object stored in `completion` is a tuple instead of the expected completion response object.

If this occurs, inspect the code that creates or wraps the Groq client/request.

For example:

```python
print(type(completion))
print(completion)
```

Also check `client.py` for accidental tuple creation or a wrapper that returns multiple values.

---

## Error: API key error

Check that the API key is available as an environment variable:

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

Then restart the terminal/application if necessary.

---

# 28. Security

Never commit your API key to Git.

Do not put this in source code:

```python
client = Groq(api_key="gsk_...")
```

Prefer an environment variable.

If using a `.env` file, add it to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

---

# 29. Key Concepts Learned

By building this chatbot, you are learning several important concepts:

### API

An API allows your Python program to communicate with an external service.

```text
Python
   ↓
Groq API
   ↓
AI Model
   ↓
Response
```

### Client

The client manages communication with the API.

```python
client = Groq()
```

### Messages

Messages represent the conversation.

```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]
```

### Model

The model generates the response.

```python
model="openai/gpt-oss-120b"
```

### Parameters

Parameters control model generation:

```python
temperature=1
top_p=1
max_completion_tokens=2048
reasoning_effort="medium"
```

### Streaming

Streaming allows the response to arrive incrementally.

```python
stream=True
```

---

# 30. Overall Architecture

The Python chatbot can be understood as four layers:

```text
┌─────────────────────────────┐
│          User Input         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Conversation          │
│         messages            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        chatbot.py            │
│        get_response()        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│          Groq API            │
│     GPT-OSS-120B Model       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Assistant Response       │
└─────────────────────────────┘
```

---

# 31. Next Improvements

Once the basic chatbot is working, possible improvements include:

1. Add streaming responses.
2. Add better conversation memory.
3. Add token/context-window management.
4. Add error handling for API failures.
5. Add configurable model parameters.
6. Add environment-variable configuration.
7. Add logging.
8. Add conversation reset functionality.
9. Add system-prompt configuration.
10. Add tests for the chatbot functions.

---

## Summary

The core chatbot is built around three main ideas:

```text
client.py
    ↓
Connect to Groq

prompt.py
    ↓
Define AI behavior

chatbot.py
    ↓
Send messages to the model
and return the response
```

The most important function is:

```python
def get_response(messages):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False
    )

    return completion.choices[0].message.content
```

This is the core Python logic that turns a list of conversation messages into an AI-generated response.
