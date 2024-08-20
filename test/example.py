"""
Simple example to show how the generation works.
Testpresentation.pdf has five slides, but one will be skipped using the tag %- after the ## markdown separator.
"""
import os
from src.create_voicover_video import parse_markdown, extract_slides_from_pdf, convert_text_to_speech, compile_video

TEST_PDF = "pdf/Test_presentation.pdf"
TEST_TXT = "text/template.md"
OUTPUT_VIDEO = "Test_presentation.mp4"


if __name__ == "__main__":
    scripts, slide_index = parse_markdown(TEST_TXT)
    audios = list()
    for i, text in enumerate(scripts):
        out = convert_text_to_speech(str(i) + '.mp3', text['text'])
        audios.append(out)

    # slides = Presentation(PPTX_PATH)
    slides = extract_slides_from_pdf(TEST_PDF, slide_index)

    final_video = compile_video(slides, audios)
    output_dir = "outputs"
    final_video.write_videofile(os.path.join(output_dir, OUTPUT_VIDEO), fps=30, codec='libx264')

