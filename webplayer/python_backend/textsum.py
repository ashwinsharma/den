import argparse
from pytldr.summarize.lsa import LsaOzsoy, LsaSteinberger
from pytldr.summarize.relevance import RelevanceSummarizer
from pytldr.summarize.textrank import TextRankSummarizer

def TextRank(txt, l):    
    textrank = TextRankSummarizer()
    return textrank.summarize(txt, length=l)
def Relevance(txt, l):
    relevance = RelevanceSummarizer()
    return relevance.summarize(txt, length=l)
def Lsa(txt, l):
    lsa_o = LsaOzsoy()
    return lsa_o.summarize(txt, length=l)

def generate_summary(transcript_filename, summary_filename, lenth = 10, sumamrizer="TextRankSummarizer"):   
    txt = ""
    summary = ""

    if transcript_filename:
        f = open(transcript_filename,'r')
        txt = f.read()
    else:
        print("Transcript file path not specified. Please try again")
        exit(0)
    
    
    if summarizer == "TextRankSummarizer":    
        summary = TextRank(txt, length)
    elif summarizer == "RelevanceSummarizer":
        summary = Relevance(txt, length)
    elif summarizer == "LSA":
        summary = Lsa(txt, length)


    f = open(summary_filename,'w+')
    for sentence in summary:
        f.write(sentence)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--transcript", help="Enter the full path of the generated transcript file",required=True)
    parser.add_argument("-len","--length_of_summary", help="Enter the desired length of the summary")
    parser.add_argument("-s","--summarizer", help="Enter the full path of the generated transcript file")

    length = 0
    txt = ""
    summarizer = ""
    summary = ""
    filename = ""


    args = parser.parse_args()
    print (args.length_of_summary)
    print (args.summarizer)
    print (args.transcript)
    if args.transcript:
        f = open(args.transcript,'r')
        txt = f.read()
        filename = args.transcript.split(".")[0]
    else:
        print("Transcript file path not specified. Please try again")
        exit(0)
    if args.length_of_summary:
        length = int(args.length_of_summary)
    else:
        length = 10
    if args.summarizer:
        summarizer = args.summarizer
    else:
        summarizer = "TextRankSummarizer"

    if summarizer == "TextRankSummarizer":    
        summary = TextRank(txt, length)
    elif summarizer == "RelevanceSummarizer":
        summary = Relevance(txt, length)
    elif summarizer == "LSA":
        summary = Lsa(txt, length)


    f = open(filename+".txt",'w')
    for sentence in summary:
        f.write(sentence)

    