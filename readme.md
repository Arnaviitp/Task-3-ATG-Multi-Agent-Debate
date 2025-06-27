
# 🧠 Multi-Agent Debate DAG using LangGraph

This project simulates a structured 8-round debate between two AI personas (Scientist and Philosopher) on a user-defined topic. It uses the [LangGraph](https://github.com/langchain-ai/langgraph) framework to manage state, memory, debate logic, and final judgment via a DAG architecture.

---

## 🚀 How to Run

### ✅ 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/multi-agent-debate-dag.git
cd multi-agent-debate-dag
```

### ✅ 2. Install Dependencies

Ensure you have Python 3.10+ and install dependencies:

```bash
pip install -r requirements.txt
```

If you’re on Windows, make sure [Graphviz](https://graphviz.org/download/) is installed and added to PATH (needed for DAG generation).

### ✅ 3. Run the Debate CLI

```bash
python cli_main.py
```

The system will ask for a debate topic and simulate a full 8-round debate, logging all actions.

---

## 🧱 Node and DAG Structure

The LangGraph DAG consists of the following nodes:

### 1. **UserInputNode**
- Accepts the debate topic from the user.
- Initializes state: topic, round counter, memory, and turn control.

### 2. **AgentA (Scientist)**
- Makes arguments on even turns.
- Draws from a list of scientific/regulatory perspectives.

### 3. **AgentB (Philosopher)**
- Makes arguments on odd turns.
- Draws from a philosophical/freedom-focused perspective.

### 4. **MemoryNode**
- Stores each agent's arguments in a structured format.
- Ensures no repeated arguments and updates memory state after every round.

### 5. **JudgeNode**
- Summarizes the entire debate.
- Declares a winner based on argument quality, diversity, and logical strength.
- Provides a justification for the verdict.

---

## 🔁 DAG Workflow Diagram

A visual DAG is included:  
📄 `debate_dag.png`

To regenerate it:

```bash
python generate_dag.py
```

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `cli_main.py` | Main CLI interface for running the debate |
| `debate_graph.py` | Core LangGraph logic and state control |
| `nodes/` | Modular node implementations (agents, memory, judge, input) |
| `generate_dag.py` | Code to visualize the DAG |
| `debate_log.txt` | Auto-generated log of all state transitions |
| `debate_dag.png` | DAG diagram image |
| `requirements.txt` | Required Python dependencies |
| `README.md` | This file! |

---

## 📓 Output Example

```
Enter topic for debate: Should AI be regulated like medicine?

[Round 1] Scientist: AI must be regulated due to high-risk applications.
[Round 2] Philosopher: Regulation could stifle philosophical progress and autonomy.
...
[Judge] Winner: Scientist
[Judge] Reason: Presented more grounded, risk-based arguments aligned with public safety principles.
```
## 👨‍💻 Author

**Arnav Anand**  
Machine Learning Intern – ATG
