from ydl        import Ydl
from colored    import Colored

"""
# return title and duration of video json object
def return_info(json):
  title    = json.get("title")
  duration = json.get("duration")

  color.print_pair("title", title)

  # convert seconds to minutes
  min = timedelta(seconds=json.get("duration"))
  color.print_pair("duration", min)


# 
def get_formats(json):
  formats = {}

  for obj in json.get("formats"):
    formats[obj.get("ext")] = obj.get("format_id")
    
  return formats
"""





def main(): 

  color = Colored()
  
  # STEP 1.0 - get video url from user
  color.print_value("- Please, enter URL -")
  url = input()
  
  # STEP 1.1 - get video json object
  ydl = Ydl(url)

  # STEP 2.0 - return information about video
  title, duration = ydl.get_info()
  color.print_pair("title", title)
  color.print_pair("duration", duration)
  
  # STEP 3.0 - asks user what is the desired format
  format = color.list("\n- choose a format", ("video", "song", "thumbnail", "json"))
  
  if format == "video":
    # list the availables exts for the desired format and asks one
    exts = ydl.get_video_formats()
    chosen_format = color.list_options(exts)
    color.print_pair("chosen format", chosen_format)
    
    ydl.prepare("video", chosen_format)
    ydl.download()
  


if __name__ == "__main__": 
  main()


