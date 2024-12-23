import anvil.server
from anvil import *

class Form1(Form):
    def __init__(self, **properties):
        self.init_components(**properties)

    # This function will be triggered when the button is clicked
    def analyze_button_click(self, **event_args):
        video_url = self.video_url_textbox.text  # Textbox where user enters the video URL
        
        if not video_url:
            self.result_label.text = "Please enter a valid YouTube URL."
            return

        try:
            # Call the server function to analyze the video
            result = anvil.server.call('analyze_video', video_url)

            if 'error' in result:
                self.result_label.text = f"Error: {result['error']}"
            else:
                # Display the sentiment and genre results
                self.result_label.text = f"Overall Sentiment: {result['sentiment']}\nVideo Genre: {result['genre']}"

                # Create the download link for the file
                file = result['file']
                self.download_link.visible = True  # Make the download link visible
                self.download_link.file = file
        except Exception as e:
            self.result_label.text = f"An error occurred: {str(e)}"

    # Download the Excel file when the user clicks the download button
    def download_link_click(self, **event_args):
        self.download_link.download()  # This will download the Excel file to the user's machine
