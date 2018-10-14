# - transcribe video
# - generate vtt file
# - get summary of video
# - entity analysis of text

import sys
import os.path
import argparse
import transcribe_async, vtt_gen, entity_analysis
# import textsum

original_stdout = sys.stdout

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'lecture_name', help='Name of the lecture')
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    
    args = parser.parse_args()

    transcript_filename = args.lecture_name + ".txt"
    content_filename = args.lecture_name + "_content.txt"
    subtitle_filename = args.lecture_name + ".vtt"
    summary_filename = args.lecture_name + "_summary.txt"

    # generate transcript using google api
    sys.stdout = open(transcript_filename, 'w+')
    content = transcribe_async.transcribe_gcs(args.path)
    open(content_filename, 'w+').write(content)

    # generate vtt file from transcript
    sys.stdout = original_stdout
    if not os.path.exists(transcript_filename):
        print("transcript file does not exist.\n")
        exit(-1)
    vtt_gen.generate_subtitles(transcript_filename, subtitle_filename)

    # generate summary
    # textsum.generate_summary(content_filename, summary_filename)

    # entity analysis
    entity_analysis.entities_text(content)