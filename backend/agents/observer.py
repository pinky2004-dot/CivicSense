from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

# Initialize the LLM
llm = ChatOllama(model="llama3", format="json")

# Define a Pydantic model for the expected output
class IssueAnalysis(BaseModel):
    issue_type: str = Field(description="A short category for the issue, e.g., 'Power Outage', 'Pothole'.")
    summary: str = Field(description="A concise, one-sentence summary of the report.")
    priority: str = Field(description="The assessed priority: 'Low', 'Medium', or 'High'.")

# Pass the Pydantic model to the parser to enforce the structure
parser = JsonOutputParser(pydantic_object=IssueAnalysis)

# Create a more specific prompt template
prompt = PromptTemplate(
    template="""You are an expert civic issue analyst. Your task is to analyze a report and respond ONLY with a valid JSON object.
    
    The JSON object must have these exact keys: "issue_type", "summary", and "priority".
    
    - "issue_type": A short category for the issue (e.g., 'Power Outage', 'Pothole', 'Flooding').
    - "summary": A concise, one-sentence summary of the report.
    - "priority": Must be one of 'Low', 'Medium', or 'High'. A 'High' priority indicates a direct and immediate threat to public safety.

    Analyze the following report:
    Report: "{report_text}"

    {format_instructions}
    """,
    input_variables=["report_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# The chain
chain = prompt | llm | parser

def analyze_report(text: str) -> dict:
    """Analyzes a raw text report and returns a structured dictionary."""
    try:
        # The .dict() method is needed if I use a Pydantic parser
        result = chain.invoke({"report_text": text})
        return result
    except Exception as e:
        print(f"Error analyzing report: {e}")
        return None