# -*- coding: UTF-8 -*- 
import sys,os
from lxml import etree
import collections
import itertools

###############################
##
## Script to convert tab file to CAT format for evaluation.
## Usage: python3 convert2CAT-system-class-reimers.py [system-out] [outdir]
##
#################################


def create_folder(filepath):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)


def split_list(event_dict, index_dict):

    event_span_sentence = {}

    for filename_sentence, events in event_dict.items():
        if filename_sentence in index_dict:
            span = [events[i:j] for i, j in zip([0] + index_dict[filename_sentence], index_dict[filename_sentence] + [None])]
            event_span_sentence[filename_sentence] = span

    return event_span_sentence


def conver2cat(file_dict, event_spans, outdir):


    root_cat = etree.Element("Document")

    """
    fill the xml document
    """

    #outdir

    for token_id, values in file_dict.items():

        path_fileId, sentenceId, token_string = values

        child1 = etree.SubElement(root_cat, "token")
        root_cat.set('doc_name', path_fileId.split("/")[-1].split(".col.txt.out")[0])
#        token_number =  child1.set('number', str(token_id))
#        token_sentence = child1.set('sentence', str(sentenceId))
#        token_id = child1.set('t_id', str(token_id))
#        child1.text = token_string
        child1.set('number', str(token_id))
        child1.set('sentence', str(sentenceId))
        child1.set('t_id', str(token_id))
        child1.text = token_string


    child2 = etree.SubElement(root_cat, "Markables")
    child3 = etree.SubElement(root_cat, "Relations")

    counter_event = 0

    for k, v in event_spans.items():
        for aevent in v:
            if len(aevent) > 0:
                counter_event += 1
                event_tag = etree.SubElement(child2, "EVENT")
                event_tag.set('m_id', str(counter_event))
                event_tag.set('class', aevent[0].split("-")[1])
                for elem in aevent:
                    token = elem.split("\t")[0]
                    anchor_event = etree.SubElement(event_tag, "token_anchor")
                    anchor_event.set('t_id', token)


    filename_out = root_cat.attrib.get('doc_name', 'null')
    if filename_out.endswith(".txt.out"):
        filename_out = root_cat.attrib.get('doc_name', 'null').split(".txt.out")[0]
        outfile = outdir + filename_out

        with open(outfile + ".xml", 'wb') as output:
            output.write(etree.tostring(root_cat, pretty_print=True))

    else:
        outfile = outdir + filename_out
        with open(outfile + ".xml.xml", 'wb') as output:
            output.write(etree.tostring(root_cat, pretty_print=True))


def read_data(filename, out):

    counter_sentence = -1
    counter_token = 0
    file_tokens = {}
    event_dict = collections.defaultdict(list)

    with open(filename) as inputf:

        grps = itertools.groupby(inputf, key=lambda line: bool(line.strip()))
        for k, v in grps:
            if k:
                counter_sentence += 1
                sentence_token = list(v) # (inputf, counter_sentence, list(v),)
#                print(sentence)
                for i in range(0, len(sentence_token)):
                    counter_token += 1
                    val_token = sentence_token[i]
                    val_token_stripped = val_token.strip()
                    val_token_splitted = val_token_stripped.split("\t")

                    values = (filename, counter_sentence, val_token_splitted[0])
                    file_tokens[counter_token] = values
#
#                    if val_token_splitted[1].endswith("-EVENT"):
                    if (val_token_splitted[1].startswith("B") or val_token_splitted[1].startswith("I")):
                        entry_event_dict = str(counter_token) + "\t" + val_token_splitted[1]
                        event_dict[filename + "\t" + str(counter_sentence)].append(entry_event_dict)


    """
    check for multi-tokens events in the same sentence : based on proximity
    """

    index_split_sentence = collections.defaultdict(list)

    for key, values in event_dict.items():
        for i in values:
            if i.split("\t")[-1].startswith("B-"):
                index_split_sentence[key].append(values.index(i))


    event_splits_sentence = split_list(event_dict,index_split_sentence)

    #outdir = out + filename.split("/")[-3] + '-' + filename.split("/")[-2] + '-CAT4eval/'
    outdir = out + filename.split("/")[-2] + '-CAT4eval/'

    create_folder(outdir)

    conver2cat(file_tokens, event_splits_sentence, outdir)



def data2convert(inputdir, out):
    for f in os.listdir(inputdir):
        if f.endswith(".out"):
            read_data(inputdir + f, out)




def main(argv = None):
    if argv is None:
        argv = sys.argv

        if len(argv) < 3:
            print('Usage: python3 convert2CAT-system-class-reimers.py [col_dir_data] [outdir]')
        else:
            data2convert(argv[1], argv[2])


if __name__ == '__main__':
    main()

