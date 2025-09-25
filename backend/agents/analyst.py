from typing import List, Dict, Any
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

# --- AI Setup for the Analyst ---
llm = ChatOllama(model="llama3", format="json")

class Insight(BaseModel):
    title: str = Field(description="A short, descriptive title for the insight cluster.")
    summary: str = Field(description="A one-sentence summary explaining the pattern or trend found.")
    priority: str = Field(description="The assessed priority of this insight: 'Low', 'Medium', or 'High'.")

class AnalysisResult(BaseModel):
    insights: List[Insight] = Field(description="A list of insights found from the provided issues.")

parser = JsonOutputParser(pydantic_object=AnalysisResult)

prompt = PromptTemplate(
    template="""You are an expert civic analyst. Your job is to find patterns and create insights from a list of active issues.
    
    Analyze the following list of issue summaries. Group them into meaningful clusters based on their content.
    Only create an insight if a cluster contains 2 or more related issues. If no patterns are found, return an empty list of insights.

    Respond ONLY with a valid JSON object matching the format instructions.

    List of active issues:
    {issue_list}

    {format_instructions}
    """,
    input_variables=["issue_list"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

def find_insights(active_issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Analyzes a list of active issues to find patterns and generate insights using an LLM."""
    
    # need at least 2 issues to find a pattern
    if len(active_issues) < 2:
        return []

    # Format the list of issues for the prompt
    issue_summaries = [f"- {issue.get('summary', 'No summary')}" for issue in active_issues]
    issue_list_str = "\n".join(issue_summaries)

    print(f"Analyst is reviewing {len(active_issues)} issues to find insights...")

    try:
        response = chain.invoke({"issue_list": issue_list_str})
        # The response will be a dictionary like {'insights': [...]}
        return response.get('insights', [])
    except Exception as e:
        print(f"Analyst LLM call failed: {e}")
        return []