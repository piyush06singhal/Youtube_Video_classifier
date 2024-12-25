from ._anvil_designer import mainFrameTemplate
from anvil import *
import anvil.server

class mainFrame(mainFrameTemplate):
    def __init__(self, **properties):
        """Initialize the form and its components."""
        self.init_components(**properties)
        self.download_link.visible = False  # Hide the download link initially
        self.video_url_textbox.text = ""  # Clear the URL textbox initially

    def analyze_button_click(self, **event_args):
        """Triggered when the 'Analyze' button is clicked."""
        video_url = self.video_url_textbox.text.strip()  # Get the video URL and strip whitespace

        # Check if the URL is empty
        if not video_url:
            self.result_label.text = "Please enter a valid YouTube URL."
            return

        try:
            # Disable the TextBox while processing to prevent new inputs
            self.video_url_textbox.enabled = False
            self.result_label.text = "Analyzing the video, please wait..."  # Show a loading message
            self.download_link.visible = False  # Hide the download link during processing

            # Call the analyze_video function on the server
            result = anvil.server.call('analyze_video', video_url)

            if 'error' in result:
                # Show an error message if the server returns an error
                self.result_label.text = f"Error: {result['error']}"
            else:
                # Display the sentiment and genre results
                sentiment = result.get('sentiment', 'N/A')
                genre = result.get('genre', 'N/A')
                self.result_label.text = (
                    f"Overall Sentiment: {sentiment}\n"
                    f"Video Genre: {genre}"
                )

                # Provide a download link for the Excel file, if available
                if 'file' in result:
                    self.download_link.file = result['file']
                    self.download_link.text = "Download Comments Excel File"
                    self.download_link.visible = True  # Show the download link

        except anvil.server.AnvilException as e:
            # Handle known server exceptions
            self.result_label.text = f"Server error occurred: {str(e)}"
        except Exception as e:
            # Handle unexpected errors
            self.result_label.text = f"An unexpected error occurred: {str(e)}"
        finally:
            # Re-enable the TextBox after the processing is finished
            self.video_url_textbox.enabled = True
