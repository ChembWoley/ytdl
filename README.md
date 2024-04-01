# ytdl
ytdl is a CLI application built with Python made to make downloading YouTube videos simple and easy.

## Installation
### Without source code
To install ytdl without the source code, download the latest release of ytdl from the Releases page in this repo.
Then, add the executable to your system's PATH variable.
And now, you can use ytdl from every directory in your system!

### Using source code
To make a new build of ytdl using the source code, first install Python, run
`
pip install -r requirements.txt
`
in the main folder, then run
`
pyinstaller ytdl.py --onefile
`.

The new executable will be built in `dist/ytdl`'.

## Usage
To use ytdl, use the following command:
`
ytdl <youtube-video-id>
`
You can also specify the output path, but that is completely optional.


(contact me @ mcardente.contato@gmail.com)
