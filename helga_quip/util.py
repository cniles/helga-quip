"""
Utility methods used in helga_quip.plugin
"""

import urllib

def quote_groupdict(groupdict, quotelist):
    """Quotes (url-encodes) the items in groupdict whos key is in quotelist"""
    return dict((k, urllib.quote(v)) if k in quotelist else (k, v)
                for (k, v) in groupdict.iteritems())

def quote_group(group, quotelist):
    """Quotes (url-encodes) the items in group whose index is in quotelist"""
    if group is None:
        group = []
    return [urllib.quote(v) if k in quotelist else v
            for (k, v) in zip((str(s) for s in range(len(group))), group)]

def pretty_map(inmap):
    """Returns a pretty-formatted string representing the input map"""
    return " ; ".join(["{0}: {1}".format(k, v)
                       for (k, v) in inmap.iteritems()])
