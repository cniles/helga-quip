""" Helga entry point for plugin """
import re, requests
from helga import log
from helga.db import db
from helga.plugins import command, match, random_ack

from helga_quip.util import quote_groupdict, quote_group

_help_text = 'Match quips and other witticisms. Usage:\
!quip add/remove <quip_kind> <quip_regex>\
Example:\
1. !quip add "thats what she said" "(it|that|this) (sounds|is|was) really hard"\
2. !quip add "your mom {0}" "(looks|is) really (leet|fat|awesome)"'

logger = log.getLogger(__name__)

def _quip_manage(client, channel, nick, message, args):
    """ Add/remove quip/phrase to stash """
    if args[0] == 'drop':
        db.helga_quip.entries.drop()
    elif args[0] == 'dump':
        quips = [p['regex'] + ' | ' + p['kind'] for p in db.helga_quip.entries.find()]
        if not quips:
            return "Quip database empty"
        payload = {'title':'helga-quip dump', 'content': '\n'.join(quips)}
        r = requests.post("http://dpaste.com/api/v2/", payload)
        return r.headers['location']
    else:
        valid_options=['-q']

        # Filter out any option that is invalid and turn them into a
        # dict
        options = dict(map(lambda o: (o[:2], o[2:]), filter(lambda o: o[:2] in valid_options, args[3:])))
        
        phrase = {'kind':args[1], 'regex':args[2], 'options':options}
        if args[0] == 'add':
            phrase['nick'] = nick
            try:
                re.compile(phrase['regex'])
            except:
                return 'Invalid regex: %s' % phrase['regex']
            db.helga_quip.entries.insert(phrase)
        elif args[0] == 'remove':
            db.helga_quip.entries.remove(phrase)
    return random_ack()

def _quip_respond(message):
    """ Search for matching quip, respond if exists """
    for phrase in db.helga_quip.entries.find():
        result = re.search(phrase['regex'], message, re.I)
        if result:
            quip = phrase['kind']

            # get the quote list option; if it doesn't exist set it to
            # empty list.
            quotelist = phrase['options'].get('-q', None)
            quotelist = quotelist.split(",") if quotelist else []

            # TODO this will handle either named groups or positional. it needs
            # some work to support hybrid backreferenced named and positonal
            # groups, but I may implement in the near future. putting in this
            # current work as value added, but hopefully I'll not be lazy soon.

            # take care of backreferenced named groups, ez mode
            if result.groupdict():
                try:
                    quip = quip.format(**quote_groupdict(result.groupdict(), quotelist))
                except IndexError:
                    # really python, no partial format support? i have
                    # to write my own formatter (using different $ syntax) or
                    # override a dictionaries __missing__? lame, defer for now
                    # http://stackoverflow.com/questions/11283961/partial-string-formatting
                    pass
            # take care of positional arguments
            else:
                quip = quip.format(*quote_group(result.groups(), quotelist))
            return ('success', quip)

@match(_quip_respond)
@command('quip', aliases=['joke', 'quips'], help=_help_text, shlex=True)
def quip(client, channel, nick, message, *args):
    """ Helga endpoint for plugin """
    # hacky because this could be either match which already populated args or
    # regular command, which we need to process. surely theres a cleaner way.
    if len(args) == 2 and isinstance(args[1], (list,)):
        return _quip_manage(client, channel, nick, message, args[1])
    if args[0][0] == 'success':
        return args[0][1]
