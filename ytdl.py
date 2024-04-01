from pytube import YouTube
from sys import argv
from re import match
from keyboard import read_key
from pytube.cli import on_progress

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

def complete(strm, path):
    print(f"| Video downloaded sucessfully at path {path}!")

def progress(strm, dtchnk, bytslft):
    print("\033[A| ", end="")
    on_progress(strm, dtchnk, bytslft)
    print("")

print(f"‿  {link("https://github.com/ChembWoley/ytdl", "ytdl v1.0.0")}")

if len(argv) < 2:
    print("| usage: ytdl <yt-video-id> optional: <path>")
else:
    if not match(r"[0-9A-z]{11}", argv[1]):
        print("| ID provided is not valid.")
    else:
        askInput = True
        vid = YouTube(f'https://youtube.com/watch?v={argv[1]}',
                      on_complete_callback=complete,
                      on_progress_callback=progress)

        vid.check_availability()

        print(f"| Do you mean {vid.author}'s \"{vid.title}\"? (Y/N)\n| ", end="")
        
        while askInput:
            yn = read_key()
            if yn.lower() == "y" or yn.lower() == "n": askInput = False

        if yn.lower() == "n":
            print("Operation cancelled.")
        else:
            path = argv[2] if len(argv) > 2 else None
            print("Downloading...")
            print("| ")
            vid.streams.get_highest_resolution().download(path)

print("⁀")
