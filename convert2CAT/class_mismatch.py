import sys, os, os.path
from lxml import etree
from collections import Counter


"""
compare system output for event classification against the gold
check class mismatch on TRUE POSITIVES between Gold and sys output
"""


def get_xml_event (inputf):

    """
    :param inputf: input CAT XML file
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
        token_id = [tokens.get('t_id', 'null') for tokens in elem.findall('token_anchor')]
        event_dict[event_id] = tuple(token_id) + (event_class,)

    event_dict_final = {}

    for k, v in event_dict.items():
        class_event = v[-1]
        event_dict_final[v[0:-1]] = class_event

    return event_dict_final



def get_data (gold_data, sys1_data):

    """
    :param gold_data: xml CAT file - GOLD
    :param sys1_data: xml CAT file - system
    :return:
    """

    gold_event = get_xml_event(gold_data)

    """
    sys1
    """
    system_class_mistmatch = []

    system_event = get_xml_event(sys1_data)
    for tokens_, class_event in gold_event.items():
        if tokens_ in system_event:
            if class_event != system_event[tokens_]:
                system_class_mistmatch.append((class_event, system_event[tokens_],))

    return system_class_mistmatch


def read_folder(gold_dir, sys1dir):

    system_mistmatch = []

    for f in os.listdir(gold_dir):
        sys1in = sys1dir + f

        if f.endswith(".xml"):
            system_class = get_data(gold_dir + f, sys1in)
            system_mistmatch.extend(system_class)


    print("Wrong class: " + str(len(system_mistmatch)))

    wrong_class = []
    gold_system = []

    for elem in system_mistmatch:
        gold, system_wrong = elem
        wrong_class.append(system_wrong)
        gold_system.append(gold)


    print("Distribution of wrong classes")
    print(Counter(wrong_class))
#    print(Counter(gold_system))



def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) < 3:
        print('Usage: python3 class_mistmacth.py gold sys1')
    else:
        read_folder(argv[1], argv[2])

if __name__ == '__main__':
    main()





















