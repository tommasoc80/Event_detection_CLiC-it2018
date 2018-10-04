import sys, os, os.path
from lxml import etree
from collections import Counter


"""
compare system output for event detection and classification against the gold
TRUE POSITIVES events - check the POS per event tag (uses manually annotated POS labels from the Gold data)
"""

def get_xml_event(inputf):

    """
    :param inputf: input CAT XML file - gold
    :return: dict of event tokens and class; event token tuple is key, event class label is value
    """

    docf = etree.parse(inputf, etree.XMLParser(remove_blank_text=True))
    root_doc = docf.getroot()
    root_doc.getchildren()


    event_dict = {}

    doc_name = root_doc.get('doc_name', 'null')

    for elem in root_doc.findall('Markables/EVENT'):
        event_id = elem.get('m_id', 'null')
        event_class = elem.get('class', 'null')
        event_pos = elem.get('pos', 'null')
        token_id = [tokens.get('t_id', 'null') for tokens in elem.findall('token_anchor')]
        event_dict[event_id] = tuple(token_id) + (event_pos,)

    event_dict_final = {}

    for k, v in event_dict.items():
        class_event = v[-1]
        event_dict_final[v[0:-1]] = class_event

    return event_dict_final



def get_data (gold_data, sys1_data):

    """
    :param gold_data: xml CAT file - GOLD
    :param sys1_data: xml CAT file - system out
    """

    event_list_gold = []

    """
    GOLD data
    """

    gold_dict = get_xml_event(gold_data)

    """
    system
    """
    system_dict = get_xml_event(sys1_data)

    true_positive_stats = []
    for k, v in system_dict.items():
        if k in gold_dict:
            true_positive_stats.append(gold_dict[k])


    return true_positive_stats


def read_folder(gold_dir, sys1dir,):

    full_stats_true_pos = []

    for f in os.listdir(gold_dir):
        sys1in = sys1dir + f

        if f.endswith(".xml"):
            true_positive_data = get_data(gold_dir + f, sys1in)
            full_stats_true_pos.extend(true_positive_data)
        else:
            print("Error - missing data: " + f)


    print(Counter(full_stats_true_pos))

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) < 3:
        print('Usage: python2 true_pos_stats_POS.py gold sys1')
    else:
        read_folder(argv[1], argv[2])

if __name__ == '__main__':
    main()

























