
# TAPIRE: Tool for Assisting Protocol Inference and Reverse Engineering


This is a tool developed by Conix security: http://www.conix.fr/

The aim of the project is to make protocol reverse engineering easy and automate some of the work for the engineer.
It does not aim to replace the reverser and should be considered as a help for reverse engineering, not a solution.
Right now the tool supports TCP and UDP based protocol reverse engineering as well as unkown file format reverse engineering.

The tool needs a modified version of [Netzob](https://github.com/netzob/netzob) ([netgoblin fork](https://github.com/warsang/netzob)) in order to make efficient use of all methods.
It is under continuous development and hence can be unstable when it comes to some features.

This project began as a script. Hence, some parts of the code are not very pythonic (ex: circular imports etc.). I do intend to reformat (make it more Object oriented, get rid of circular imports, get rid of click etc.) the code but have not found the courage to do so yet.

The main mantainer of the project is warsang. Please contact him at theodore.riera@gmail.com

### Includes:

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
* Gui window to display symbols
* ClusterizebyAlignment
* Wrong symbol or field selection
* Wireshark dissector export
* Kaitai export
* Dynamic analysis (send a sequence of message and get answer)
* Get netgoblin log output for IPseeker, CRC32Seeker, SizeSeeker
* Documentation/Tutorial
* EntropyFinder
* File format reverse engineering
* And probably more...

## TODO:

* Check for error in RelationFinder
* Value search
* Split fields by index
* Header separation based on field name
* Code reformating
* ClusterizebyApplicativeData
* Helpstrings
* Dynamic analysis (automaton generation, fuzzing, live capture and live display of new fields improvement)
* Interface with REWARDS pintool to get type and semantic inference
* HelpStrings
* Dockerfile
* Display messages in different encodings (cyrilic, utf-16 etc.)


## Tool usage:

Let's walk through some of the tool's basic features:

First and foremost you might want to check the options available when using the CLI. You can get more info by typing

    ./tapire.py -h

[![help](https://asciinema.org/a/LzfETFAE5pCO9dLxFqfJZAIkp.png)](https://asciinema.org/a/LzfETFAE5pCO9dLxFqfJZAIkp)

Let's go over each option:
 
- The "-n / --network" option:
Tapire has two modes, a network mode and a non network mode specified by the -n option Network mode is taylored to analyze messages contained in pcaps. It also enables Tapire networking capabilities such as replaying a sequence of messages and (not yet implemented) will also allow live capture.

- The "-a / --analyze" option:
This allows the user to load either a pcap (in network mode) or an unknown file format as input for Tapire. As netzob makes use of [differential analysis](http://www.digitalbond.com/blog/2014/10/15/protocol-differential-analysis/) for it's base inference methods, at least two files should be specified as input.

- The "-l / --load" option:
Tapire allows to save Reverse Engineering projects. Projects are saved by serializing a symbol:messages dictionnary using [python pickle](https://docs.python.org/3/library/pickle.html) and saving it to a file. Loading just deserializes the object.

- The "-g / --gui" option:
Sometimes, displaying  large messages can have rather unexpected results in the terminal and be extremly difficult to read. Tapire aims to be minimal, but also to help the Reverse engineer. Hence, a limited graphical interface is available allowing to display outputs that may lead to confusion in the terminal inside scrollable windows.

- The "-v / --verbose" option:
This option taks either C,E,W,I,D as an argument. It allows to define netgoblin logging verbosity. (C: critical, E: Error, W: Warning, I: Info , D: Debug) please refer to [this link](https://docs.python.org/3/library/logging.html) for more information.

- The "--version" option:
Will print the version of Tapire.

## Walk-through:

The idea behind differential analysis is to find similarities between fields by comparing two or more given files.

Before reading this, you'll need to be familiar with the notion of symbol.

A symbol is a netzob object which groups messages according to a common attribute such as size, applicative data etc.

Hence, **symbol = group of messages** 

### Networking mode
Part of this walkthrough is heavily based on the [official netzob tutorial](http://doc.netzob.org/en/latest/tutorials/discover_features.html#discover-features).


First and foremost download the following files:

[Pcap1](https://dev.netzob.org/attachments/download/182/target_src_v1_session1.pcap)
[Pcap2](https://dev.netzob.org/attachments/download/181/target_src_v1_session2.pcap)
[Pcap3](https://dev.netzob.org/attachments/download/181/target_src_v1_session3.pcap)

These files are pcap captures taken from a fake botnet protocol. Ideally, in real life when doing differential analysis, it is best to focus on pcap captures of one simple action. (For example when RE the protocol of a connected coffe machine, you might want to only focus on pcap captures of one same action such as turning off the coffe machine rather than compare straight away a pcap to make coffe with a pcap to upload a new firmware to the machine.)

Now that we have all three files we can load them in Tapire using the -a option:
(I named my pcaps toto, but trust me, they are the very same (or similar as I did not do a sha1sum) as the ones you downloaded)

[![Start tapire](https://asciinema.org/a/KX3SsEFAjTiyEhWdUQ5ZRIWZs.png)](https://asciinema.org/a/KX3SsEFAjTiyEhWdUQ5ZRIWZs)

As you can see we also add the -n option as we are analyzing messages inside a pcap(ng) file and the -g option because we want to use the GUI (that will not be displayed in asciinema).
Once the files are loaded, we are greeted by a nice Ascii art of a tapire! :)
Only one symbol named "Symbol\_0"  is available at start. It groups all messages from the different pcaps.

Now that our pcaps are loaded we probably want to have a look at what the communication looks like.

As you noticed, we are greeted by several menus when opening Tapire. Because we want to know what the pcap exchange looks like, we will select menu 1.

Inside menu 1, several different options are available:

- Option 1 displays the messages as raw hexdump using scapy.
- Option 2 displays the message as an ISO-8859-1 decoded leveraging netzob built in message representation. Why ISO-8859-1? Because it has a rather large charset and may put in light some interesting strings (TODO: add more types of encodings)
- Option 3 Displays the pcap communication with the fields obtained during inference. It is probably better to export a wireshark dissector and look at the communication using the dissector, nevertheless it allows for a quick idea of what the communication looks like with it's fields. It's quite usefull to identify a counter field which increments for each sent message.
- Option 4 Displays the symbols in chronological order. This allows to keep in mind the time relation between different symbols as netzob gets rid of it after manipulating symbols.
- Most menus in Tapire have a "B" option which allows to go back to the previous menu.

At first, as we only have one symbol named "Symbol\_0", we can also take a look at this symbol to visualize the communication.

To do so, we head back to the main menu ("B") and select the manipulate menu "2".
Once we are in the manipulate menu, we choose option "1" (display symbols) in order to display "Symbol\_0".

All messages are displayed in chronological order. 
As we did not begin protocol inference, there are very few default fields:

- Session: Which displays the file name from which the message was extracted
- Source: (IP and port source address)
- Destination: (IP and port destination)
- Field: Default data field (what we will be focusing our inference on)

[![Display communication](https://asciinema.org/a/fOcz0aPvfduTwZ5yQiWy9CpG2.png)](https://asciinema.org/a/fOcz0aPvfduTwZ5yQiWy9CpG2)

Well in this use case, we can see that all messages have a "#" this is a field delimiter similar to http's "\r\n" separation for headers.
Hence we want to split the messages using "#" as a delimiter.
To do so, inside the manipulate menu ("2") we go in the split menu ("3"). And select the split delimiter.
As there is no "b" in front of the string, we know we are dealing with ascii. Hence the "#" is an ascii delimiter. We can now select the Ascii type ("1") for the split delimiter and choose "#" as the delimiter.
When we display our symbol again, we can clearly see the separated fields. However, a loose "#" at the end created two extra fields. As these are "false positives" we want to get rid of them. Hence we'll merge these fields in Field-2.
To do so we go back to the manipulate menu and select the "Field manipulate menu" ("7"). The user is asked to select a field there. You probably noticed that the second field called "Feild-sep-23" changed. Tapire appended it a uuid so that it is unique as Tapire has trouble manipulating fields with the same name. We select **the field on the left** that we wish to merge. By selecting option "4" the "Field merger" we are asked to select a second field. We select the one on the right.
The Fields are merged. We do the same a second time and obtain the right output!
 
 [![Split with delimiter and merge fields](https://asciinema.org/a/KVXlHFETNrFEe6LQXyvYDSZXz.png)](https://asciinema.org/a/KVXlHFETNrFEe6LQXyvYDSZXz)
 
Now we quickly notic that the first field appears several times. Hence we want to cluster the messages by fields.
We can select the Clusterize menu "2" to do so. Several clusterize options are available. Clusterize by field or by applicative data are usually quite usefull for text based protocols. Clusterize by size is good for fixed size protocols such as most SCADA protocols. ClusterbyCRC32 will separate messages in a group which includes messages with CRC32 and one without Here we select Cluster by key field ("5").

[![Cluster by key field](https://asciinema.org/a/UirbXRW27DnoknmIFBVUln09A.png)](https://asciinema.org/a/UirbXRW27DnoknmIFBVUln09A)

Please note that the wildcard selector "*" is supported in some menus in TAPIRE. However not all options are available for the wild card selector, most of the time because they induce an important overhead!

We can now try to detect relations between fields. There are two types of relation finders in TAPIRE:
- The ones that work with wildcard "*" selector
- The ones that work without it. Netzob is not multithreaded. Neither is Netgoblin. Hence some relation finders cause a very large overhead. It was decided in Tapire that the slower ones would not work with the "*" attribute. Detecting a relation is usually fast. The longer process is automated field creation. You might want to create fields manually (using the IPython console) after detection in order to reduce overhead.

To run the basic Relation Finder implemented in Netzob, once inside the manipulate menu, select alls symbols and go to the simple relation finder menu "R" and select "Relation Finder" -> "2"
You should then get the following result:

![Relation finder results](https://ibb.co/jdrHba)

TAPIRE does not automate field creation through the basic Relation finder (yet) so you will need to script it. The netzob tutorial explains how to do so in a simple manner:

    for symbol in symbols.values():
    rels = RelationFinder.findOnSymbol(symbol)

    for rel in rels:

        # Apply first found relationship
        rel = rels[0]
        rel["x_fields"][0].domain = Size(rel["y_fields"], factor=1/8.0)

    print("[+] Symbol structure:")
    print(symbol._str_debug())

However, if the field relation is a Size Relation, you might want to try using the netgoblin complex Size relation which includes automated field creation.
To do so, select the symbol in the manipulate menu in which you want to create the relation, then select "9" and "4" to go to the size relation seeker. It will ask you if you wish to create fields and will ask you for a base search index. Here we could point it after the first text field as we know that it is not our Size field.

The following shows the automated Size field creation:

[![Size Relation Finder and field creation](https://asciinema.org/a/WfML0rMJNS30s4FTEQaU5g7op.png)](https://asciinema.org/a/WfML0rMJNS30s4FTEQaU5g7op)

Now that we have our fields define, we can export the parser to a wireshark dissector and visualize the pcap with netzob infered fields directly in wireshark. To run wireshark with our lua dissector, we use:

    wireshark -X lua_script:<my_script.lua>

### File analysis mode

We can also use TAPIRE to reverse engineer an unknown file format.

In this example we are going to make use of three simple gif files. When Reverse engineering a file with Tapire, try to use small files as you might have an important overhead with larger files.

This time we will run tapire without the "-n" option:

    ./tapire.py -a ../demo_tapire/gif_files/ajax-loader.gif ../demo_tapire/gif_files/loading_icon.gif ../demo_tapire/gif_files/texasflag.gif -g
    
However, I am using the "-g" (gui) option as file inference usually results with very long strings of bytes hard to look at on a terminal.

In the manipulate menu, I chose to start by splitting the buffers using the split aligned method.
I chose this method as there would probably be very similare fields in the files but they might not be at the same position. Hence, this would allow to align these similar fields.
Then I displayed the symbol to visualize the result. The result is long to load as unfortunately, netzob and netgoblin are not multi-threaded...
The first few fields: Session, Source and Destination are from the networking mode and have not yet been disabled in TAPIRE for non networking mode. They show the Session (file source) as well as the source (same value as the Session) and a destination field of "None".

![Result](https://image.ibb.co/cRYT7v/Selection_015.png)

The first few fields are the ones we are interested in as the rest is probably just raw data for the file format.

![After a bit of formatting](https://i.imgur.com/tA7MFXU.png)

I renamed the fields according to the GIF structure exposed in [kaitai Web IDE](https://ide.kaitai.io/)

The first Field contains the file Magic string. A unique string which identifies the file format. This string here is "\x47\x49\x46" which is hex for "GIF". The following value 89a is the GIF version.
The next two fields are Screen width and height. Then comes a flag which is the color table flag.
In the "ajax loader" gif image, this flag is 0XF2 which is "ò" in ASCII. This flag gives us several informations on the gif file:

To check if the file has a color table we check :
     
    flags & 0b10000000 != 0

Here:

    0xF2 & 0x80 = 0x80
If the value is not null we have a color table.
The size of the color table is given by:

    2 << (flags & 7)

Here:
    
    2 << (0XF2 & 7) = 8

The next value in this field is the BG color index. "\x04" for the second file.

Finally the following field "Field01502691-24e6-44ba-bd40-fac61efbcf09" is the pixel ratio. Appart from this, we also notice that it is a separator field between the data and header part of the file. TAPIRE has several methods to separate header fields from data fields. However, I have not yet implemented separating header and data by using a specific field name.










