from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

# Initialize the LLM
# Make sure Ollama is running with the llama3 model
llm = ChatOllama(model="llama3", format="json")

# Define the structured output we want
parser = JsonOutputParser()

# Create a prompt template that instructs the model
prompt = PromptTemplate(
    template="""You are an expert civic issue analyst.
    Analyze the following report from a citizen and extract key information.
    The priority must be one of: 'Low', 'Medium', 'High'.
    A 'High' priority indicates a direct and immediate threat to public safety (e.g., power lines down, major traffic failure).
    A 'Medium' priority is a significant but not life-threatening issue (e.g., large pothole on a major road).
    A 'Low' priority is a minor issue (e.g., graffiti).

    Report: "{report_text}"

    {format_instructions}
    """,
    input_variables=["report_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Create the processing chain by piping the components together
# This is the modern way to use LangChain (LCEL)
chain = prompt | llm | parser

def analyze_report(text: str) -> dict:
    """Analyzes a raw text report and returns a structured dictionary."""
    try:
        result = chain.invoke({"report_text": text})
        return result
    except Exception as e:
        print(f"Error analyzing report: {e}")
        return None