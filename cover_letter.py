from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
import gradio as gr

# Model and project settings
model_id = "meta-llama/llama-3-2-11b-vision-instruct"
credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
)
params = TextChatParameters(
    temperature=0.7,
    max_tokens=512
)
project_id = "skills-network"

# Initialize the model
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

def generate_cover_letter(company_name, position_name, job_description, resume_content):
    """
    Generates a customized cover letter using the IBM watsonx.ai model.
    """
    prompt = (
        f"Write a professional and persuasive cover letter for the position '{position_name}' "
        f"at '{company_name}'. Use the following job description to tailor the letter:\n{job_description}\n\n"
        f"Incorporate relevant skills and experiences from this resume:\n{resume_content}\n\n"
        "The cover letter should be clear, concise, and highlight why the candidate is a great fit."
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]

    response = model.chat(messages=messages)
    cover_letter = response['choices'][0]['message']['content']
    return cover_letter

# Gradio interface setup
iface = gr.Interface(
    fn=generate_cover_letter,
    inputs=[
        gr.Textbox(label="Company Name", placeholder="Enter the company name"),
        gr.Textbox(label="Position Name", placeholder="Enter the job position"),
        gr.Textbox(label="Job Description", lines=6, placeholder="Paste the job description here"),
        gr.Textbox(label="Resume Content", lines=10, placeholder="Paste your resume content here")
    ],
    outputs=gr.Textbox(label="Generated Cover Letter"),
    title="Cover Letter Generator with IBM watsonx.ai",
    description="Generate a tailored cover letter based on job description and your resume."
)

if __name__ == "__main__":
    iface.launch()