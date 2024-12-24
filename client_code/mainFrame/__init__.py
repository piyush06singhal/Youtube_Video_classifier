from ._anvil_designer import mainFrameTemplate
from anvil import *
import anvil.server

class mainFrame(mainFrameTemplate):  # Ensure this matches the name of your form in the Anvil Editor
    def __init__(self, **properties):
        """Initialize the form and its components."""
        self.init_components(**properties)
        self.download_link.visible = False  # Hide the download link initially
        self.video_url_textbox.text = ""  # Initialize textbox text if required

    def analyze_button_click(self, **event_args):
        """Triggered when the 'Analyze' button is clicked."""
        video_url = self.video_url_textbox.text  # Get the video URL entered by the user

        # Check if the URL is empty
        if not video_url.strip():
            self.result_label.text = "Please enter a valid YouTube URL."
            return

        try:
            # Disable the TextBox while processing to prevent new inputs
            self.video_url_textbox.enabled = False
            self.result_label.text = "Analyzing the video, please wait..."  # Show a processing message
            self.download_link.visible = False  # Hide the download link until processing is done

            # Call the analyze_video function on the server
            result = anvil.server.call('analyze_video', video_url)

            # Check for errors in the result
            if 'error' in result:
                self.result_label.text = f"Error: {result['error']}"
            else:
                sentiment = result['sentiment']
                genre = result['genre']
                self.result_label.text = f"Overall Sentiment: {sentiment}\nVideo Genre: {genre}"

                # Provide a download link for the Excel file after processing is completed
                if 'file' in result:
                    # Use the Download component for file download
                    self.download_link.file = result['file']  # This is where we assign the file
                    self.download_link.text = "Download Comments Excel File"
                    self.download_link.visible = True  # Make the download link visible after processing

        except Exception as e:
            # Handle any unexpected errors
            self.result_label.text = f"An unexpected error occurred: {str(e)}"

        finally:
            # Re-enable the TextBox after the processing is finished
            self.video_url_textbox.enabled = True
