from midiutil import MIDIFile

import xml.dom.minidom
import sys

def getNoteData(note, key):
	return int(note.getElementsByTagName(key)[0].firstChild.data)

vsqx = xml.dom.minidom.parse(sys.argv[1])

TEMPO = int(vsqx.getElementsByTagName('tempo')[0].childNodes[1].firstChild.data[:-2])

mf = MIDIFile(1, removeDuplicates=False)
track = 0

time = 0
mf.addTrackName(track, time, "Sample")
mf.addTempo(track, time, TEMPO)

for note in vsqx.getElementsByTagName('note'):
	mf.addNote(track, 0, getNoteData(note, 'n'), getNoteData(note, 't') / 480, getNoteData(note, 'dur') / 480, getNoteData(note, 'v'))

with open("vsqxmidi.mid", 'wb') as outf:
	mf.writeFile(outf)