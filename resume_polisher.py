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

def polish_resume(position_name, resume_content, polish_prompt=""):
    """
    Polishes a resume for a specific position with optional additional instructions.
    """
    if polish_prompt:
        prompt = (
            f"Please polish the following resume for the position '{position_name}' "
            f"with these additional instructions: {polish_prompt}\n\nResume:\n{resume_content}"
        )
    else:
        prompt = (
            f"Please polish the following resume for the position '{position_name}'.\n\n"
            f"Resume:\n{resume_content}"
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

    # Generate polished resume using the model
    response = model.chat(messages=messages)
    polished_resume = response['choices'][0]['message']['content']
    return polished_resume

# Create Gradio interface
iface = gr.Interface(
    fn=polish_resume,
    inputs=[
        gr.Textbox(label="Position Name", placeholder="Enter the job position"),
        gr.Textbox(label="Resume Content", lines=10, placeholder="Paste your resume here"),
        gr.Textbox(label="Additional Instructions (Optional)", lines=3, placeholder="E.g., focus on leadership skills")
    ],
    outputs=gr.Textbox(label="Polished Resume"),
    title="Resume Polisher with IBM watsonx.ai",
    description="Enter a position and your resume, optionally add instructions, and get a polished resume."
)

if __name__ == "__main__":
    iface.launch()