# 🚌 Pradeep Tamilnadu Travels - AI Powered Multi-Agent Bus Ticket Booking Chatbot

https://colab.research.google.com/drive/12x7512A0Yoydvs-msGvGUQueNlpnZ7fl#scrollTo=GvctXETG9DFu

An intelligent **AI-powered Bus Ticket Booking Chatbot** developed using **Python, Gradio, Generative AI (GenAI), Multi-Agent Architecture, and an AutoGen-inspired workflow**. The chatbot enables users to book bus tickets, check bus timings, view fare details, browse available routes, contact customer support, and generate professional ticket PDFs through a conversational interface.

The project follows an **Agentic AI** approach where multiple AI agents collaborate to complete the entire booking process. Each agent is responsible for a specific task while the **Conversation Manager** coordinates the workflow from user interaction to ticket generation.

---

# 🚀 Features

- 🤖 AI-powered conversational chatbot
- 🚌 Bus ticket booking
- 🛣️ Available route information
- 🕒 Bus timings
- 💰 Fare details
- ❌ Cancellation policy
- 📞 Customer support
- 🪑 Seat selection
- 🎫 Automatic ticket generation
- 📄 PDF ticket generation
- 📥 PDF download option
- 💬 Interactive Gradio interface
- 🧠 Multi-Agent Architecture
- ⚙️ AutoGen-inspired workflow
- 🚀 Google Colab & Hugging Face compatible

---

# 🛠️ Technologies Used

- Python
- Gradio
- Generative AI (GenAI)
- Multi-Agent Architecture
- AutoGen-inspired Workflow
- Object-Oriented Programming (OOP)
- State Machine
- Session Management
- PDF Generation
- Ticket Image Generation
- GitHub
- Google Colab
- Hugging Face Spaces

---

# 🧠 System Architecture

```text
                    User
                      │
                      ▼
             Gradio Chat Interface
                      │
                      ▼
           Conversation Manager
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
 Session Manager  State Machine  Booking Flow
                      │
                      ▼
               Agent Workflow
                      │
      ┌─────────┬─────────┬─────────┐
      ▼         ▼         ▼         ▼
 Supervisor  Booking   Ticket   Support
   Agent      Agent     Agent     Agent
                      │
                      ▼
              Ticket Generator
             ├── Image Generator
             └── PDF Generator
```

---

# 🤖 Multi-Agent Architecture

Instead of handling every task inside one large program, this chatbot uses multiple specialised AI agents.

Each agent performs a dedicated responsibility and communicates with the Conversation Manager to complete the user's request.

---

# 👨‍💼 Supervisor Agent

## Responsibilities

- Receives customer requests
- Analyses user intent
- Routes tasks to the appropriate agent
- Coordinates the overall workflow
- Returns responses to the Conversation Manager

### Example

```
User

↓

Book Ticket

↓

Supervisor Agent

↓

Booking Agent
```

---

# 🚌 Booking Agent

The Booking Agent handles the complete ticket booking process.

## Responsibilities

- Starts ticket booking
- Displays available routes
- Collects passenger details
- Collects mobile number
- Collects seat number
- Sends booking information to the Ticket Agent

### Workflow

```
Book Ticket

↓

Select Route

↓

Passenger Details

↓

Seat Selection

↓

Ticket Agent
```

---

# 🎫 Ticket Agent

The Ticket Agent generates the final ticket.

## Responsibilities

- Creates ticket number
- Generates ticket information
- Generates ticket image
- Generates ticket PDF
- Returns booking confirmation

### Example Output

```
Passenger : Ramya

Route : Chennai → Madurai

Seat : C1

Ticket No : PT-DF465880

Status : Confirmed
```

---

# 📞 Support Agent

The Support Agent handles customer support queries.

## Responsibilities

- Customer support
- Contact information
- Help messages
- General assistance

Example

```
📞 +91 9876543210

📧 support@pradeeptravels.com
```

---

# 💬 Conversation Manager

The Conversation Manager is the central controller of the chatbot.

It manages the entire conversation from the welcome screen until ticket generation.

## Responsibilities

- Welcome screen
- Main menu
- Booking flow
- Session management
- State management
- Agent communication
- Ticket generation

The Conversation Manager decides which agent should perform the next task based on the current conversation state.

---

# 🔄 Agent Communication Flow

```text
User

↓

Gradio Chat Interface

↓

Conversation Manager

↓

Supervisor Agent

↓

Booking Agent

↓

Booking Flow

↓

Ticket Agent

↓

Ticket Service

↓

Image Generator

↓

PDF Generator

↓

Conversation Manager

↓

Gradio Interface

↓

User receives Ticket PDF
```

---

# ⚙️ AutoGen-inspired Workflow

This project follows an AutoGen-inspired workflow where multiple specialised agents collaborate to complete a task.

The workflow is responsible for:

- Analysing user requests
- Routing requests to the correct agent
- Managing the execution flow
- Returning responses to the Conversation Manager

This modular architecture makes it easy to extend the project by adding new agents such as:

- Payment Agent
- Cancellation Agent
- Notification Agent
- Analytics Agent

---

# 🧠 Generative AI (GenAI)

Generative AI is integrated into the chatbot architecture to provide intelligent conversational interactions.

## GenAI Features

- Natural language interaction
- Intelligent conversation flow
- User-friendly booking assistance
- Improved customer experience
- Scalable AI architecture

The chatbot is designed so that advanced Large Language Models (LLMs) can be integrated in future versions without changing the overall architecture.

---

# 🔄 Complete Booking Workflow

```text
User

↓

Welcome

↓

Main Menu

↓

Book Ticket

↓

Select Route

↓

Passenger Name

↓

Age

↓

Gender

↓

Mobile Number

↓

Seat Selection

↓

Booking Confirmation

↓

Ticket Generation

↓

Ticket Image

↓

Ticket PDF

↓

Download PDF

↓

Booking Completed
```

---

# 📁 Project Structure

```text
Pradeep-Tamilnadu-Travels-Bus-Ticket-Booking-Chatbot

│

├── backend
│   ├── agents
│   │   ├── supervisor_agent.py
│   │   ├── booking_agent.py
│   │   ├── ticket_agent.py
│   │   └── support_agent.py
│   │
│   ├── autogen
│   │   ├── workflow.py
│   │   └── team.py
│   │
│   ├── conversation
│   │   ├── conversation_manager.py
│   │   ├── booking_flow.py
│   │   ├── session_manager.py
│   │   ├── state_machine.py
│   │   └── menu.py
│   │
│   ├── services
│   ├── ticket
│   ├── database
│   ├── utils
│   └── config
│
├── ui
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🌟 Project Highlights

- ✅ AI Powered Chatbot
- ✅ Multi-Agent Architecture
- ✅ Agentic AI Workflow
- ✅ Generative AI Integration
- ✅ Conversation Manager
- ✅ State Machine
- ✅ Session Management
- ✅ AutoGen-inspired Workflow
- ✅ Ticket Generation
- ✅ Ticket Image Generation
- ✅ Ticket PDF Generation
- ✅ PDF Download
- ✅ Interactive Gradio UI
- ✅ Google Colab Deployment
- ✅ Hugging Face Compatible
- ✅ Modular & Scalable Design



# 📌 Conclusion

**Pradeep Tamilnadu Travels – AI Powered Multi-Agent Bus Ticket Booking Chatbot** demonstrates how **Generative AI**, **Agentic AI**, and a **Multi-Agent Architecture** can work together to automate the complete bus ticket booking process. The **Conversation Manager** orchestrates the conversation, the **Supervisor Agent** routes requests, specialised agents perform booking, ticket generation, and customer support, and the system produces downloadable PDF tickets through an interactive Gradio interface.

The modular architecture makes the application scalable, maintainable, and ready for future enhancements such as payment integration, RAG, database connectivity, and cloud deployment.
