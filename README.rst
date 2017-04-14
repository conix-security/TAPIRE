==========================================
TAPIRE: Tool for Assisting Protocol Inference and Reverse Engineering
==========================================

This is a tool developed by Conix: http://www.conix.fr/en/

The tool needs a modified version of NETZOB (netgoblin fork) in order to make efficient use of all methods.
It is still under developement.
The main mantainer of the project is warsang. Please contact him at theodore.riera@conix.fr

Includes:
=========
* IPseeker
* Sizeseeker
* CRCseeker
* HeaderSeeker
* Netzob RelationFinder (only between fields => Size,equality,data)
* SizeClustering
* KeyFieldClustering
* CRC32Clustering
* Displays PCAPS using the netzob displayer or scapy
* SplitStatic
* SplitAligned
* SplitDelimiter
* Symbol renaming, description
* Field renaming, description, merging
* Most netzob methods

TODO:
=====
* ClusterizebyAlignment
* ClusterizebyApplicativeData
* Helpstrings
* Wrong symbol or field selection
* Gui window to display symbols
* Dynamic analysis (message generation from infered symbols, automaton generation, fuzzing, live capture and live display of new fields)
* Wireshark dissector
* Get netgoblin log output for IPseeker, CRC32Seeker, SizeSeeker
* HelpStrings
* Documentation/Tutorial
* Finsih the EntropyFinder (To detect possible cryptofunctions)



