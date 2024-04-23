# CustomerCareAssistant_AI-

This assistant should be capable of retrieving information about the company, its products, and services from a provided PDF document. Additionally, it should be able to create support tickets for 
queries it cannot resolve directly.


## AI model and custom assistant ##

In the custom assistant, created in Assistants (OpenAi API platform), <i>gpt-3.5-turbo</i> is set as Model.
<br>
This version of gpt is cheap (	Input- $0.50 / 1M tokens  Output-	$1.50 / 1M tokens) but sufficient to retrieve information about the company, its products, and services from a provided PDF document.<br>
In the settings of this assistant File search is obviousaly enabled and a Function is added.
This function is used to communicate with the backend in Python, adding a ticket if the user that is chatting with the assistant want to create it.
The code of this function is:
```
{
  "name": "add_ticket",
  "description": "Add ticket to ticket DB",
  "parameters": {
    "type": "object",
    "properties": {
      "nome": {
        "type": "string",
        "description": "nome of user"
      },
      "email": {
        "type": "string",
        "description": "email of user"
      },
      "testo": {
        "type": "string",
        "description": "short text"
      }
    },
    "required": [
      "nome",
      "email",
      "testo"
    ]
```

At the assistant is given some instructions to perform as well as possible and to maintain a good level of security.

## Information retrieval ##

Communication with the custom assistant is achieved by using OpenAI's API in Python.
We send 2 different API requests :
* API request for start a new thread (a run of assistant in OpenAI server)
* API request to chatting with the assistant.
 
We also set Fast API to communicate with our python code.
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

<br>
So when the local server starts at localhost:8001 we can query it with :

```
https://localhost:8001/start
```
We get thread_id as response and after set it in the next request in 'thread_id' field and 'message' with your question:
```
https://localhost:8001/chat
Body raw:
{
    "thread_id": "",
    "message": "Who are you ?"
}
```
After this request we get a response from the assistant.

## Ticket creation ##

Creating a ticket is a action that we can trigger querying to assistant senteces like:
```
Can I open ticket ?
```
```
I have a unresolved question, What can i do?
```
In this last sentence our assistant'll offer you the possibility of open a ticket.
This feauture must be implemented giving to assistant a specific instruction in Playground, OpenAI API platform.
This instruction is like:
```
When the user has some questions that you can't answer, propose him to open a ticket. If he want to open a ticket trigger add_ticket function that you memorized.
Ask him name email and the ticket content.  
```
In the ticketing.py we set context information to access of a Google Sheet stored in our Google Drive.
By using Google Cloud API we can modify this sheet adding a new line with the data in ticket request.
<br>
We have to uploaded in the project folder a json file generating by google cloud api that within it there are credentials to autenticate at Google Sheet API.<br>
This is a <a href="https://developers.google.com/sheets/api/guides/concepts?hl=it">guide</a>.









