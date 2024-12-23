import anvil.server

class Form1(Form1Template):  # Automatically generated class from the Form1 template
    def __init__(self, **properties):
        self.init_components(**properties)

    def fetch_comments_button_click(self, **event_args):
        video_url = self.video_url_textbox.text  # Get the URL from the TextBox
        if video_url:
            try:
                # Call the server function to analyze the overall sentiment
                overall_sentiment = anvil.server.call('get_overall_sentiment', video_url)

                # Display the result in the Label
                self.result_label.text = f"Overall Sentiment: {overall_sentiment}"
            except Exception as e:
                self.result_label.text = f"Error: {str(e)}"
        else:
            self.result_label.text = "Please enter a valid YouTube URL."
