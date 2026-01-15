import google.generativeai as genai
from google.api_core import exceptions
from tenacity import retry, stop_after_attempt, wait_fixed

class SummarizerService:
    def __init__(self, api_key):
        """
        Initialize the Google Gemini client.
        """
        if not api_key:
            raise ValueError("API Key is missing.")
        
       
        genai.configure(api_key=api_key)
    def _get_system_instruction(self, style):
        """
        Returns the specific instruction based on style.
        """
        instructions = {
            "Brief": "Summarize the following text in 1-2 concise sentences.",
            "Detailed": "Provide a comprehensive summary of the text, covering all main arguments, supporting details, and the conclusion.",
            "Bullet Points": "Summarize the key takeaways of the text using a structured bulleted list."
        }
        return instructions.get(style, instructions["Brief"])

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def summarize(self, text, style="Brief"):
        """
        Sends text to Google Gemini for summarization.
        """
        if not text or len(text.strip()) == 0:
            return "Error: Input text cannot be empty."

        instruction = self._get_system_instruction(style)
        
      
        full_prompt = f"{instruction}\n\n---\n\nText to summarize:\n{text}"

        try:
            
            response = self.model.generate_content(full_prompt)
            
            
            return response.text

        except exceptions.InvalidArgument as e:
            raise Exception(f"Invalid API Key or Argument: {str(e)}")
        except exceptions.ResourceExhausted as e:
            raise Exception(f"Quota exceeded (Rate Limit): {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")