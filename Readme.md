### Read Slides
This is a simple project inspired by necessity and by [Saverio Mazza](https://medium.com/@saverio3107?source=post_page-----3e6fa712e864--------------------------------)'s post on Medium [1].

### Required packages
 - gTTS
 - pdf2image
 - moviepy

Note: at the moment pptx presentations are not supported, so you can comment all the references to pypptx in the code.

### Usage
The voiceover uses the gTTS to read the text compiled on a markdown file. 

The example contained in the test folder is fairly self-explanatory. At the moment the code creates a list of texts by
parsing the given markdown file. 

Every "## " delimits a new slide. If there are slides in the pdf presentation that
should be skipped, it is possible to add the tag "%-" after the "## " to skip text generation and slide in the final video. 

[1] https://medium.com/@saverio3107/create-videos-from-slides-audio-with-python-easy-guide-3e6fa712e864