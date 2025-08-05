import google.generativeai as genai

genai.configure(api_key="AIzaSyBY1JD--25BZifA_m9vr_m1mCpEAFTPUAg")
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def spin_text(input_text):
    prompt = f"""Rewrite the following content in a more engaging, modern, and fluid storytelling style, but retain the core meaning and events.

    TEXT:
    {input_text[:4000]}
    """
    response = model.generate_content(prompt)
    return response.text

def revise_with_feedback(current_text, feedback):
    prompt = f"Revise this based on feedback: {feedback}\n\n{current_text}"
    return model.generate_content(prompt).text
