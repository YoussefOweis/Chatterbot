# Employee Integration Chatbot

A Python-based employee integration chatbot designed to help new employees get information about their workplace, onboarding process, and useful learning resources.

The chatbot uses **Flask** for the web application and **ChatterBot** for natural-language conversation.

## Features

- Employee onboarding assistance
- Answers common questions about:
  - Working hours
  - First day at work
  - Workplace and parking
  - Dress code
  - Employee ID cards
  - Lunch and breaks
  - Salary and expenses
  - Benefits and holidays
  - Sick leave
  - Remote work
  - Internet and intranet
  - Email and social media
  - Training and career development
  - Projects and technologies
- Provides technical learning resources
- Simple web-based chat interface
- Uses ChatterBot's `BestMatch` logic adapter
- Custom training data for employee integration
- REST-like endpoint for sending messages

## Technologies

- Python
- Flask
- ChatterBot
- HTML
- CSS
- JavaScript
- jQuery

## Project Structure

```text
Chatterbot/
│
├── Rapport PFE - OWEIS YOUSSEF.pdf
│
└── chatterbot/
    ├── index.py
    ├── math.py
    ├── units.py
    │
    ├── templates/
    │   └── index.html
    │
    └── json_sandbox/
        ├── LICENSE
        ├── ambignq.zip
        ├── answer.json
        ├── dev.json
        ├── newfile.txt
        └── question.json
```

## How It Works

The application is built around a Flask web server and a ChatterBot instance.

### Flask Application

The Flask application provides the web interface and API endpoint.

```python
app = Flask(__name__)
```

The homepage is served through:

```text
/
```

The chatbot communication endpoint is:

```text
/get
```

### ChatterBot

The chatbot uses ChatterBot's `BestMatch` logic adapter to find the most appropriate response from its training data.

```python
bot = ChatBot(
    "chatbot",
    response_selection_method=get_random_response,
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry i dont have an answer",
            "maximum_similarity_threshold": 0.8
        }
    ]
)
```

### Training Data

The chatbot is trained using `ListTrainer`.

```python
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train2)
```

The training data contains employee-related questions and answers as well as technical learning resources.

The chatbot can provide resources for technologies such as:

- Python
- .NET
- Angular
- ASP.NET Core
- React
- React Native
- Vue.js
- HTML/CSS/JavaScript
- Android/Kotlin
- Git
- PHP
- Spring
- jQuery
- Go

## Web Interface

The frontend is implemented in:

```text
chatterbot/templates/index.html
```

It provides a simple chat interface where users can enter messages and receive responses from the chatbot.

jQuery is used to communicate with the Flask backend through AJAX.

The frontend sends the user's message to:

```text
/get?userMessage=...
```

The Flask application processes the message and returns the chatbot's response.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YoussefOweis/Chatterbot.git
```

Navigate to the project:

```bash
cd Chatterbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

Install the required Python packages:

```bash
pip install flask chatterbot
```

Depending on the ChatterBot version and Python version being used, additional compatibility dependencies may be required.

## Running the Application

Navigate to the chatbot directory:

```bash
cd chatterbot
```

Run the Flask application:

```bash
python index.py
```

Open your browser and access:

```text
http://127.0.0.1:5000/
```

## Example Questions

You can ask questions such as:

```text
What time should I arrive?
```

```text
What should I wear on my first day?
```

```text
Where can I park?
```

```text
How do I get my employee ID?
```

```text
What happens on my first day?
```

```text
How can I learn Python?
```

```text
Where can I learn React?
```

```text
How can I learn Git?
```

## Learning Resources

The chatbot can provide links to online learning resources based on the technology requested by the employee.

Examples include resources for:

- Python
- JavaScript
- HTML/CSS
- React
- Angular
- Vue.js
- .NET
- ASP.NET Core
- PHP
- Spring
- Git
- Android/Kotlin
- Go

## API Endpoint

The chatbot exposes a simple endpoint for sending messages.

### Request

```http
GET /get?userMessage=Hello
```

### Response

The endpoint returns the chatbot's response as plain text.

Example:

```text
Hello! How can I help you?
```

## Project Documentation

The repository also contains the project's PFE report:

```text
Rapport PFE - OWEIS YOUSSEF.pdf
```

The report provides additional information about the project's objectives, implementation, and development process.

## Possible Improvements

Future versions of the project could include:

- Database-based conversation storage
- Authentication for employees
- Administrator dashboard
- Better natural-language understanding
- Context-aware conversations
- Conversation history
- Employee-specific information
- Integration with company databases
- Improved frontend interface
- More structured learning resources
- Production deployment
- Automated testing
- REST API documentation

## Author

**Youssef Oweis**

Web Developer / Python Developer

GitHub:  
https://github.com/YoussefOweis

## License

This project is intended primarily as an educational and portfolio project.
