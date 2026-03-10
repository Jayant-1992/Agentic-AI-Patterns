####################################################################################
This example demonstrates prompt chaining agent design pattern using Langchain.
There are two LLM calls:
  1. Create JSON schema of extracted test information from candidate's resume
  2. Evaluate candidate based on job description

Resume and job description are kept in the data folder
** Example is built using locally hosted Ollama 3.1 model.
####################################################################################

######## PROMPT CHAINING AGENT DESIGN PATTERN ########

Prompt Chaining is an agentic AI design pattern where a complex task is broken into multiple smaller LLM tasks, and the output of one prompt becomes the input to the next prompt. Each prompt acts like a specialized agent responsible for a specific step in the workflow.

This pattern improves accuracy, modularity, and maintainability compared to using a single large prompt to solve the entire problem.



######## WHY PROMPT CHAINING? ########

Large tasks such as resume evaluation, document analysis, or knowledge extraction involve multiple reasoning steps. If we attempt to solve everything with one prompt, the LLM may:

hallucinate information

produce inconsistent outputs

become harder to debug

Prompt chaining solves this by dividing the workflow into focused stages, where each stage performs a well-defined task.



######## HOW IT WORKS ########

In prompt chaining, the pipeline typically follows this structure:

Input Data
   │
   ▼
Agent 1 (Information Extraction)
   │
   ▼
Structured Data
   │
   ▼
Agent 2 (Analysis / Evaluation)
   │
   ▼
Final Result


######## ADVANTAGES OF PROMPT CHAINING ########

> Prompt chaining provides several benefits:

> Improved Accuracy

> Breaking tasks into smaller steps allows each agent to focus on a single responsibility, improving output quality.

> Better Debugging

> Intermediate outputs (such as extracted resume JSON) can be inspected and validated before further processing.

> Modular Architecture

> Each agent can be independently improved or replaced without affecting the entire system.

> Reduced Prompt Complexity

> Smaller prompts are easier for the model to follow compared to a single large prompt.


######## WHEN TO USE PROMPT CHAINING ########

> Prompt chaining is useful when:

> tasks involve multiple reasoning steps

> intermediate structured data is required

> workflows need to be modular and extensible

######## COMMON APPLICATIONS INCLUDE ########

> resume screening systems

> document analysis pipelines

> knowledge extraction systems

> multi-step AI assistants
