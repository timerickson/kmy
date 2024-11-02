def pairs_dict_from_xml(pair_nodes):
    if pair_nodes is None:
        return {}
    result = {}
    for pair_node in pair_nodes:
        result[pair_node.attrib["key"]] = pair_node.attrib["value"]
    return result
