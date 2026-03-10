from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableLambda
from utils.pdf_text_extraction import read_pdf
from prompts.agent1_prompt import agent1_pompt
from prompts.agent2_prompt import agent2_prompt
from utils.txt_reader import read_txt
import json


################        Inputs         ##################################

resume_path = r"data\resume_1.pdf"
job_description_file = r"data\job_description.txt"

#########################################################################
llm = ChatOllama(
    model = "llama3.1",
    temperature=0,
    format="json"
)

pdf_reading = RunnableLambda(read_pdf)

prompt_1 = ChatPromptTemplate.from_template(agent1_pompt)

resume_agent = pdf_reading | prompt_1 | llm | JsonOutputParser()

result = resume_agent.invoke({"pdf_path": resume_path})

candidate_name=result["name"]

#Review profile summary
with open('profile_summary.json', "w", encoding='utf-8') as f:
    json.dump(result,f,indent=4)

job_description = read_txt(file_path=job_description_file)

prompt_2 = ChatPromptTemplate.from_template(agent2_prompt)

evaluater_agent = prompt_2 | llm | JsonOutputParser()

evaluated_result = evaluater_agent.invoke({"job_description":job_description,"resume_data":result})

evaludation_filename = candidate_name + "evaludation_report.json"

with open(evaludation_filename, "w", encoding='utf-8') as f:
    json.dump(evaluated_result,f,indent=4)

