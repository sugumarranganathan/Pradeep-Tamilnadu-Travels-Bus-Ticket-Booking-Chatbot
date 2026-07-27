# 🚌 Pradeep Tamilnadu Travels – AI Powered Multi-Agent Bus Ticket Booking Chatbot

An intelligent **AI-powered Bus Ticket Booking Chatbot** developed using **Python, Gradio, Generative AI (GenAI), Multi-Agent Architecture, and an AutoGen-inspired Agent Workflow**.

The chatbot enables users to interact through a conversational interface to book bus tickets, check available routes, view bus timings, check fare details, view cancellation policies, and contact customer support.

The project follows an **Agentic AI** approach where multiple specialised agents collaborate to complete the booking process. A **Conversation Manager** coordinates the interaction between different agents and controls the overall booking workflow.

---

# 🚀 Features

- 🤖 AI-powered conversational chatbot
- 🚌 Bus ticket booking
- 🛣️ Available routes
- 🕒 Bus timings
- 💰 Fare details
- ❌ Cancellation policy
- 📞 Customer support
- 🪑 Seat selection
- 🎫 Booking confirmation
- 💬 Interactive Gradio interface
- 🧠 Multi-Agent Architecture
- ⚙️ AutoGen-inspired workflow
- 🚀 Google Colab compatible

---

# 🛠 Technologies Used

- Python
- Gradio
- Generative AI (GenAI)
- Multi-Agent Architecture
- AutoGen-inspired Workflow
- Object-Oriented Programming (OOP)
- State Machine
- Session Management
- GitHub
- Google Colab

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
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
Session Manager   State Machine   Booking Flow
                      │
                      ▼
              Agent Workflow
                      │
      ┌─────────┬─────────┬─────────┬─────────┐
      ▼         ▼         ▼         ▼
Supervisor  Booking   Ticket   Support
  Agent      Agent     Agent     Agent
```

---

# 🤖 Multi-Agent Architecture

The chatbot is built using multiple specialised AI agents.

Each agent has a dedicated responsibility, making the system modular, scalable, and easy to maintain.

---

# 👨‍💼 Supervisor Agent

The **Supervisor Agent** acts as the coordinator between different agents.

### Responsibilities

- Receives customer requests
- Identifies user intent
- Routes requests to the correct agent
- Coordinates the booking workflow

---

# 🚌 Booking Agent

The **Booking Agent** manages the ticket booking process.

### Responsibilities

- Starts ticket booking
- Displays available routes
- Collects passenger information
- Collects mobile number
- Collects seat information
- Passes booking data to the Conversation Manager

---

# 🎫 Ticket Agent

The **Ticket Agent** prepares booking information after confirmation.

### Responsibilities

- Generates booking details
- Creates ticket information
- Sends booking confirmation back to the Conversation Manager

---

# 📞 Support Agent

The **Support Agent** handles customer support requests.

### Responsibilities

- Customer support
- Contact details
- Help information
- User assistance

---

# 💬 Conversation Manager

The **Conversation Manager** is the core controller of the chatbot.

It manages the complete conversation and coordinates communication between all agents.

### Responsibilities

- Welcome screen
- Main menu
- Booking flow
- Session management
- Conversation state management
- Agent communication
- Booking confirmation

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

Conversation Manager

↓

Ticket Agent

↓

Booking Confirmation

↓

Gradio Chat Interface

↓

User
```

---

# ⚙️ AutoGen-inspired Workflow

The chatbot follows an AutoGen-inspired workflow where specialised agents collaborate to complete user requests.

The workflow performs the following tasks:

- Receives customer requests
- Determines the appropriate task
- Routes requests to the correct agent
- Coordinates the execution flow
- Returns responses to the Conversation Manager

This modular design makes it easy to extend the system by adding new agents such as:

- Payment Agent
- Cancellation Agent
- Notification Agent
- Analytics Agent

---

# 🧠 Generative AI (GenAI)

Generative AI enhances the chatbot by enabling natural conversational interactions.

### GenAI Features

- Natural language conversation
- Intelligent booking assistance
- Interactive customer support
- Improved user experience
- Modular AI architecture

The architecture is designed to support future integration with advanced Large Language Models (LLMs).

---

# 🔄 Booking Workflow

```text
User

↓

Welcome Screen

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

Conversation Completed
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
│   ├── database
│   ├── utils
│   └── config
│
├── ui
├── app.py
├── requirements.txt
└── README.md
```

---

# 🌟 Current Project Highlights

- ✅ AI-powered conversational chatbot
- ✅ Multi-Agent Architecture
- ✅ Agentic AI workflow
- ✅ Generative AI integration
- ✅ Conversation Manager
- ✅ State Machine
- ✅ Session Management
- ✅ Booking workflow
- ✅ Booking confirmation
- ✅ Interactive Gradio interface
- ✅ Modular project structure
- ✅ Google Colab deployment

---

# 🚀 Future Enhancements

- 📄 Ticket PDF generation
- 🖼️ Ticket image generation
- 📥 PDF download option
- 💳 Online payment integration
- ❌ Ticket cancellation
- 📜 Booking history
- 📧 Email notifications
- 📱 SMS notifications
- 🗄️ Database integration
- 🧠 RAG-based knowledge base
- 🌐 Multi-language support
- 📊 Admin dashboard
- ☁️ Cloud deployment

---

# 📌 Conclusion

**Pradeep Tamilnadu Travels – AI Powered Multi-Agent Bus Ticket Booking Chatbot** demonstrates how **Generative AI**, **Agentic AI**, and a **Multi-Agent Architecture** can work together to automate a conversational bus ticket booking system.

The **Conversation Manager** orchestrates the interaction, the **Supervisor Agent** coordinates requests, and specialised agents collaborate to complete the booking process. The modular architecture makes the application scalable, maintainable, and ready for future enhancements such as payment integration, ticket generation, database connectivity, and cloud deployment.
