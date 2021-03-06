helga-quip
======================

"Always with the witty retorts, that one"
-quote that totally happened by a wise and ausipicious gentleman in reference
to helga-quip

Purpose
-------

Match quips and other witticisms. It notes double entendre, hyperbole,
metaphors, and other figures of speech.

Usage
-----

Quip may be used for oneliners or elaborate your mom or thats what she said
jokes. The syntax is:

``!quip add <quip_kind> <quip_regex>``

quip_kind is the kind of quip you'd like to respond with, and can be a templated
response. It could simply be "Your mom" or "That's what she said", but the user
may wish to include the matched regex in the response. This may be done with
{0}, which will be replaced with the matched group. Other positionals may be
used, or named groups are supported now similar to (?P<name>expression).

quip_regex is the searched regular expression to be matched. Any regex should
do, like "that (sounds|is|was) really hard". The search is case insensitive.

Example::

    !quip add "thats what she said" "(it|that|this) (sounds|is|was) really hard"
    <unwitting user>: i took this test last night, and it was really hard
    <bot>: thats what she said
    <unwitting user>: aww bot, your wit knows no bounds! ha ha!

Example2::

    !quip add "your mom {0}" "(looks|is) really (leet|fat|awesome)"
    <irc noob>: huh this game looks really awesome
    <bot>: your mom looks really awesome
    <irc noob>: oh bot! you and the jokes, they keep coming so hard!

Example3 (named backreferences)::

    !quip add "your mom is {action}" "(?:(?:i|he|you) (?:is|am)) (?P<action>excited|giddy)"
    <foolish scrub>: man, i am excited for the concert!
    <bot>: your mom is excited
    <foolish scrub>: YOUR MOM IS...
    <foolish scrub> has left the chat

Example4 (positonals)::

    !quip add "your mom is {0} of {1}" "[am|is] (lord|king) of (me|him|her|she|he)"
    <naive user>: ...man, i am lord of him! shot right in the face, and he wasn't doing nothin'!
    <bot>: your mom is lord of him
    <naive user> sobs at the truth of it all

``!quip dump``

Dumps to the paste service dpaste with | delimited entries of 'regex | kind'

License
-------

Copyright (c) 2015 Jon Robison

See included LICENSE for licensing information
