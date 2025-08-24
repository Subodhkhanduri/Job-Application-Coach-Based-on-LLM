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
    max_tokens=1024
)
project_id = "skills-network"

# Initialize the model
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

def generate_career_advice(position_applied, job_description, resume_content):
    """
    Generates personalized career advice for a job applicant.
    """
    prompt = (
        f"You are assisting a user who is using cloud-ide-kubernetes tools to complete the "
        f"'Building Generative AI-Powered Applications with Python' course.\n\n"
        f"Provide tailored career advice for someone applying for the position '{position_applied}'.\n"
        f"Here is the job description:\n{job_description}\n\n"
        f"Here is the candidate's resume content:\n{resume_content}\n\n"
        f"Offer practical tips and suggestions to improve their chances of success."
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
    advice = response['choices'][0]['message']['content']
    return advice

# Gradio interface setup
iface = gr.Interface(
    fn=generate_career_advice,
    inputs=[
        gr.Textbox(label="Position Applied For", placeholder="Enter the job position"),
        gr.Textbox(label="Job Description", lines=8, placeholder="Paste the job description here"),
        gr.Textbox(label="Resume Content", lines=12, placeholder="Paste your resume content here")
    ],
    outputs=gr.Textbox(label="Career Advice"),
    title="Career Advisor with IBM watsonx.ai",
    description="Get personalized career advice based on your job application and resume."
)

if __name__ == "__main__":
    iface.launch()