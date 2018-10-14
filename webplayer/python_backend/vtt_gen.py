import sys
import re
import os.path
from os import linesep
from webvtt import WebVTT, Caption
from datetime import timedelta

def open_file(file_name):
    f = open(file_name, "r")
    return f.readlines()

#def generate_srt(subs):
#    return srt.compose(subs, eol = os.linesep)

#def write_srt(srt):
#    pass

def write_vtt(vtt, output_file_name):
    with open(output_file_name, 'w+') as fd:
        vtt.write(fd)

def generate_subtitles(input_file_name, output_file_name):
    
    if not os.path.isfile(input_file_name):
        print("Invalid file name")
        return

    f_content = open_file(input_file_name)
    
    vtt = WebVTT()
   
    count = 0
    prev_start = ""
    prev_end = ""
    prev_str = ""
    for line in f_content:
        if line.startswith('Word'):
            # print(line, prev_str)
            l = line.strip() + '\n'
            m = re.search('Word: (.+?), start_time: (.+?), end_time: (.+?)\n', line)
            
            current_start = str(timedelta(seconds = float(m.group(2)), microseconds = 1))
            current_end = str(timedelta(seconds = float(m.group(3)), microseconds = 1))

            if(count < 6):
                if(count == 0):
                    prev_start = current_start
                count += 1
                prev_end = current_end
                prev_str += " " + m.group(1)

            if(count == 6): 
                #caption = Caption(
                #        str(timedelta(seconds = float(m.group(2)), microseconds = 1)),
                #        str(timedelta(seconds = float(m.group(3)), microseconds = 1)),
                #        str(m.group(1)))

                caption = Caption(
                        prev_start,
                        prev_end,
                        prev_str)
                vtt.captions.append(caption)
                count = 0
                prev_start = ""
                prev_end = ""
                prev_str = ""

    write_vtt(vtt, output_file_name)
