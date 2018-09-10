from youtube_dl import YoutubeDL
from datetime   import timedelta

class Logger(object):
  def debug(self, msg):
    pass
    
  def warning(self, msg):
    pass
  
  def error(self, msg):
    print(msg)



def hook(p):
  if p["status"] == "finished":
    print("Downloading done!")



class Ydl(object):
  
  def __init__(self, url):
    self.opts = {
      "quiet": True, 
      "logger": Logger(),
      "progress_hooks": [hook],
      "skip_download": True, 
      "outtmpl": "%(title)s-%(id)s.%(ext)s"
    }
    
    self.url = url    
    self.ydl = YoutubeDL(self.opts)
    
    with self.ydl:
      self.json = self.ydl.extract_info(url)

  
  
  # return title and duration of video json object
  def get_info(self):
    title    = self.json.get("title")
    duration = self.json.get("duration")

    # convert seconds to minutes
    duration = timedelta(seconds=duration)

    return (title, duration)


  # return available exts in video json object
  def get_video_formats(self):
    formats = {}

    for obj in self.json.get("formats"):
      formats[obj.get("format_id")] = obj.get("ext")
      
    return formats
  
  #
  def prepare(self, format, ext=0):
    if format == "video":
      self.opts["format"] = ext
      self.opts["skip_download"] = False
    
    
  # download content with defined props
  def download(self):
    
    with YoutubeDL(self.opts) as ydl:
      ydl.download([ self.url ])
    
