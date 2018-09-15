from midiutil import MIDIFile

import xml.dom.minidom
import sys
from pathlib import PurePath

def getNoteData(note, key):
	return int(note.getElementsByTagName(key)[0].firstChild.data)

path = PurePath(sys.argv[1])

vsqx = xml.dom.minidom.parse(str(path))

TEMPO = int(vsqx.getElementsByTagName('tempo')[0].childNodes[1].firstChild.data[:-2])

mf = MIDIFile(len(vsqx.getElementsByTagName('vsTrack')), removeDuplicates=False)

time = 0

for trackNo, track in enumerate(vsqx.getElementsByTagName('vsTrack')):
	mf.addTrackName(trackNo, time, "Track {}".format(str(trackNo)))
	for note in track.getElementsByTagName('note'):
		mf.addNote(trackNo, 0, getNoteData(note, 'n'), getNoteData(note, 't') / 480, getNoteData(note, 'dur') / 480, getNoteData(note, 'v'))
	mf.addTempo(trackNo, time, TEMPO)

with open(str(path.parents[0]) +'\\'+ path.stem + ".mid", 'wb') as outf:
	mf.writeFile(outf)
