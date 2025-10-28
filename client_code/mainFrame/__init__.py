
from ._anvil_designer import mainFrameTemplate
from anvil import *
import anvil.server

class mainFrame(mainFrameTemplate):
  def __init__(self, **properties):
    """Initialize the form and its components."""
    self.init_components(**properties)
    self.video_url_textbox.text = ""  # Clear the URL textbox initially

    # Hide download button initially (if it exists)
    if hasattr(self, 'button_download'):
      self.button_download.visible = False

  def analyze_button_click(self, **event_args):
    """Triggered when the 'Analyze' button is clicked."""
    video_url = self.video_url_textbox.text.strip()

    # Check if the URL is empty
    if not video_url:
      self.result_label.text = "Please enter a valid YouTube URL."
      return

    try:
      # Disable the TextBox while processing
      self.video_url_textbox.enabled = False

      # Show loading message
      self.result_label.text = "🔄 Analyzing the video, please wait..."

      # Hide download button if it exists
      if hasattr(self, 'button_download'):
        self.button_download.visible = False

      print("Analyzing video:", video_url)

      # Call the analyze_video function on the server
      result = anvil.server.call('analyze_video', video_url)

      if 'error' in result:
        self.result_label.text = f"❌ Error: {result['error']}"
        print(f"Error from server: {result['error']}")
      else:
        # Display results
        sentiment = result['sentiment']
        sentiment_score = result.get('sentiment_score', 'N/A')
        genre = result['genre']
        total_comments = result.get('total_comments', 0)
        spam_count = result.get('spam_count', 0)
        bot_count = result.get('bot_count', 0)
        video_title = result.get('video_title', 'Unknown')
        video_channel = result.get('video_channel', 'Unknown')
        
        # Build result text with nice formatting
        result_text = "✅ Analysis Complete!\n\n"
        result_text += f"🎥 Video: {video_title}\n"
        result_text += f"👤 Channel: {video_channel}\n\n"
        result_text += f"📊 Overall Sentiment: {sentiment}\n"
        result_text += f"📈 Sentiment Score: {sentiment_score}\n"
        result_text += f"🎭 Genre: {genre}\n\n"
        result_text += f"💬 Total Comments: {total_comments}"
        
        if spam_count > 0:
          result_text += f"\n🚫 Spam Detected: {spam_count}"
        if bot_count > 0:
          result_text += f"\n🤖 Bots Detected: {bot_count}"
        
        result_text += f"\n\n{result.get('message', 'Analysis complete.')}"
        
        self.result_label.text = result_text
        
        # ⭐ SHOW DOWNLOAD BUTTON - THIS IS THE KEY! ⭐
        if hasattr(self, 'button_download'):
          self.button_download.visible = True
          self.button_download.enabled = True
          print("Download button is now visible!")
        else:
          print("Warning: button_download not found!")
        
    except Exception as e:
      # Handle any unexpected errors
      self.result_label.text = f"❌ An unexpected error occurred: {str(e)}"
      print(f"Error: {str(e)}")
      import traceback
      traceback.print_exc()
    
    finally:
      # Re-enable the TextBox after processing
      self.video_url_textbox.enabled = True
  
  def button_download_click(self, **event_args):
    """When user clicks Download Report button"""
    video_url = self.video_url_textbox.text.strip()
    
    if not video_url:
      alert("Please enter a YouTube URL first")
      return
    
    # Show loading message
    original_text = self.result_label.text
    self.result_label.text = "📥 Generating Excel report... Please wait..."
    self.button_download.enabled = False
    
    try:
      print("Requesting Excel report from server...")
      
      # Call server to generate Excel file
      excel_file = anvil.server.call('download_report', video_url)
      
      if excel_file:
        print("Excel file received, starting download...")
        # Download the file
        anvil.media.download(excel_file)
        self.result_label.text = original_text + "\n\n✅ Report downloaded successfully!"
        print("Download complete!")
      else:
        alert("Failed to generate report. Please try again.")
        self.result_label.text = original_text + "\n\n❌ Download failed"
        print("Server returned None for excel_file")
    
    except Exception as e:
      alert(f"Error downloading report: {str(e)}")
      self.result_label.text = original_text + f"\n\n❌ Download failed: {str(e)}"
      print(f"Download error: {str(e)}")
      import traceback
      traceback.print_exc()
    
    finally:
      self.button_download.enabled = True
