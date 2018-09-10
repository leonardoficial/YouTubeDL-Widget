from ydl        import Ydl
from colored    import Colored
 
 

def main(): 

  color = Colored()
  
  # STEP 1.0 - get video url from user
  color.print_value("- Please, enter URL -")
  url = input()
  
  # STEP 1.1 - create video json object
  ydl = Ydl(url)

  # STEP 2.0 - return information about video in json object
  title, duration = ydl.get_info()
  color.print_pair("title", title)
  color.print_pair("duration", duration)
  
  # STEP 3.0 - asks user what is the desired format, checks if input is valid and prepare
  # content to get downloaded
  while True:
    format = color.list("\n- choose a format", ("video", "audio", "thumbnail", "json"))
    
    if format == "video":
      # list the availables exts for the desired format and asks user to choose one
      exts = ydl.get_video_formats()
      chosen_format = color.list_options(exts)
      color.print_pair("chosen format", chosen_format)
    
      ydl.prepare(format, chosen_format)
      ydl.download()  
      break
    
    elif format == "audio" or format == "thumbnail":
      ydl.prepare(format)
      ydl.download()  
      break
    
    elif format == "json":
      break
        
    elif format == "exit":
      print("\Exiting")
      break
  
    else:
      print("\nWrong format!")


if __name__ == "__main__": 
  main()


