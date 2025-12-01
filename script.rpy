# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch = Character("CHARLOTTE", color="#da91ec")
define r = Character("RYAN", color="#9a3bfa")
define a = Character("ADA", color="#86bfe5")
define b = Character("BARRY", color="#913b82")

label splashscreen:

    scene splash with fade

    show text "{color=#000}Made with Renpy Visual Novel Engine{/color}" at left # for voice enabled
    $ renpy.pause(3, hard=True)

    scene bg black with fade

    return 

# The game starts here.

label start:

    ## prologue
    $ quick_menu = False

    scene bg murchison with fade

    $ renpy.pause(1.5, hard=True)

    show screen TextDisplay1("Inyarrimanha Ilgari Bundara", 0.05, 0.05)

    $ renpy.pause(1.2, hard=True)

    show screen TextDisplay4("CSIRO Murchison Radio-astronomy Observatory.", 0.1, 0.05)

    $ renpy.pause(3, hard=True)

    show screen TextDisplay2("Wajarri Yamaji Country, Western Australia.", 0.15, 0.05)

    $ renpy.pause(3, hard=True)

    hide screen TextDisplay1 with dissolve
    hide screen TextDisplay4 with dissolve
    hide screen TextDisplay2 with dissolve

    scene bg black with fade

    show screen TextDisplay3("{b}11:32 PM, February 27th, 2054.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    scene bg control with fade
    $ quick_menu = True

    "Charlotte's car skidded to a stop outside the MRO control building. She jumped out, and jogged to the entrance."

    "Ryan was waiting for her outside the inner door. Impatiently tapping his foot."

    ch "Talk to me."
    "He walked with her to the offices."
    r "It's still transmitting; Has been for approximately forty-five minutes."
    "Barry stood behind his chair, hunched over, peering at a monitor. A dozen bright screens tracked incoming data from the ASKAP antennas."
    "Ryan led her to one of the screens visualising the signal. A bright line waved across the graph. It sat well above the background radiation. Charlotte stared at it for a few seconds; mesmerised."
    
    image screen:
        "Signal/bg signal 1.png"
        pause 0.75
        "Signal/bg signal 2.png"
        pause 0.75
        "Signal/bg signal 3.png"
        pause 0.75
        "Signal/bg signal 4.png"
        pause 0.75
        "Signal/bg signal 5.png"
        pause 0.75
        "Signal/bg signal 6.png"
        pause 0.75
        "Signal/bg signal 7.png"
        pause 0.75
        "Signal/bg signal 8.png"
        pause 0.75
        "Signal/bg signal 9.png"
        pause 0.75
        "Signal/bg signal 10.png"
        pause 0.75
        "Signal/bg signal 11.png"
        pause 0.75
        repeat

    scene screen with fade
    $ renpy.pause(3, hard=True)

    ch "It's fluctuating."
    r "It's oscillating between three different amplitudes. We think it's ternary."
    ch "Ternary?"
    b "Base three."
    ch "Yes {i}I know{/i}, Barry. So- You're saying they're sending us a message?"
    r "Yep, and a long one at that. Everything they've sent so far has been unique. Hasn't repeated or looped once."
    scene bg control with fade
    "Charlotte took a step back, and ran her hands through her hair. Barry moved from one computer to another."
    ch "Okay… let's start from the beginning. Is anybody else hearing this?"
    b "We've checked with SKA-Mid in South Africa. They're reading the same thing we are."
    ch "And you're certain this is extra-terrestrial?"
    "The AI beeped from one of the computer's speakers."
    a "If I may interject, ma'am?"
    ch "Go ahead."
    a "I've been crunching the numbers ma'am. Trying to figure out whether this signal could be reflected off something, or maybe emitted from a satellite."
    ch "So could it?"
    a "So far? Not likely."
    ch "How likely is {i}not likely{/i}, Ada?"
    a "I don't see anything that {i}could{/i}. In the area the antennas are searching, the sky's empty."
    b "It's transmitting at 1420 megahertz. The hydrogen line's a protected frequency; Nobody from Earth should even be using it."
    ch "But it's possible it's coming from a satellite we don't know about?"
    r "Charlotte, you can't exactly launch a rocket into space without people knowing about it."
    ch "But it's {i}possible?{/i}"
    "Ryan sighed."
    r "Yes, it's possible."
    r "But you know what's also possible- hell, {i}probable at this point{/i}? Fucking aliens! I mean, we haven't gotten something like this in…"
    "Ryan paused."
    r " Shit."
    ch "What?"
    "Ryan spun around to look at the monitors again. Muttering something under his breath. He brought up a new window from a different screen."
    r "I think we've gotten this signal before."
    ch "What? When?"
    r "Charlotte, have you ever heard of the Wow signal?"
    "After a second of silence between the three, the AI chimed in."
    a "The 'Wow!' Signal was a powerful and mysterious radio signal detected on August 15th 1977 with the 'Big Ear' Radio Telescope at Ohio State University, USA."
    "Ryan grinned, and pointed at the computer without looking away from Charlotte."
    r "And what was the frequency of that signal?"
    a "1420 megahertz. Its intensity measured thirty times the background radiation."
    r "And the intensity of our signal now is…?"
    a "Thirty times background radiation."
    r "Charlotte, it's the same signal."
    c "Okay, if it {i}was{/i} the same, how come it wasn't a big deal back then?"
    a "The ‘Big Ear' telescope only sampled the sky every twelve seconds. If there {i}was{/i} data in the signal, the telescope might not have been precise enough to see it."
    c "But that was what, eighty years ago? Why wait until now to send another message?"
    "Silence."
    a "The only issue I see with your theory, sir, is that we aren't pointed at Sagittarius. That's where the original signal came from."
    r "Are we nearby?"
    a "Nope, other side of the planet."
    r "Then what {i}are{/i} we pointing at?"
    b "Nothing."
    ch "Nothing?"
    "The group turned their heads back to the monitors. The signal was still coming in, modulating between the three amplitudes."
    ch "… What are they trying to tell us?"

label scene1:

    $ _history_list = []

    define c = Character("CONNOR", color="#b84da6")
    define s = Character("SASHA", color="#4e73c4")
    define e = Character("ELISE", color="#76baf1")

    $ quick_menu = False
    scene bg perth with Fade(1,1,1 )

    $ renpy.pause(1.5, hard=True)

    show screen TextDisplay1("Perth.", 0.05, 0.05)

    $ renpy.pause(1.2, hard=True)

    show screen TextDisplay4("Whadjuk Noongar country, Western Australia.", 0.1, 0.05)

    $ renpy.pause(3, hard=True)

    hide screen TextDisplay1 with dissolve
    hide screen TextDisplay4 with dissolve
    hide screen TextDisplay2 with dissolve

    scene bg black with fade

    show screen TextDisplay3("{b}4:22 AM, May 15th, 2058.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    scene bg bed with fade
    $ quick_menu = True

    "Connor was awoken by a knock at the door."
    "It was still pitch black. His alarm clock read four-thirty."
    "He sat up, and waited for another round of knocks before getting up. He headed over to the door, and looked through the peephole."
    "Standing in the doorway were two women in black suits. The taller one pulled a badge from her jacket, and held it up to the peephole."
    "{color=#4e73c4}WOMAN{/color}" "Open the door please, Mr. Lovell."
    "Connor thought for a second, then slowly pulled the door open."
    c "Who are you?"
    s "My name's Sasha, and with me is Elise. We're ASIO Intelligence Officers."
    "They both showed their badges again."
    e "We're sorry to wake you."
    c "What is this about? Have I done something wrong?"   
    "Elise smiled."
    e "Of course not."
    "Sasha procured a small envelope."
    s "This here is a letter from the Director-general of Security, we'd like you to come with us."
    "Connor took the letter from her, and quickly read it over."
    c "This doesn't tell me anything. What is this ‘meeting' about? Why do you want {i}me{/i}?"
    e "You've been selected to be part of a team. It's optional, of course, but you won't know what it's for unless you agree to come."
    s "It regards the radio message you co-authored with your ex-boyfriend, Ryan Araki."
    c "Ryan… Will he be there?"
    s "If you were selected because of this message, chances are he was too."
    "Connor looked over the letter again. “{i}...It would be an honour to offer you this opportunity…{/i}”"
    "His thoughts wandered to Ryan. Was he really willing to attend some top secret meeting just in the hopes of seeing him again?"
    "He looked back up at the two women."
    c "… Alright. I'll go."

label scene2:

    $ _history_list = []
    $ quick_menu = False

    scene bg black with fade

    show screen TextDisplay3("{b}6:04 AM, May 15th, 2058.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    scene bg plane with fade
    $ quick_menu = True

    "The trip to… {i}wherever they were going{/i}, made Conner realise that this was a bigger deal than he had originally thought."
    "The two intelligence officers drove him to the airport, where they boarded a small jet."
    "There were around half a dozen others on the plane. They were all academics: Astronomers, biologists, linguists, chemists."
    "Connor was starting to get a picture of what might just be happening."
    "They flew for about an hour, travelling inland, into the outback."
    "On the plane, one of the intelligence officers handed him a card. Around the size of a business card, along with his name, all it said was: {i}Arecibo{/i}."
    "Connor was told to hold on to it, but not given a reason why."
    "The sun was starting to creep over the horizon when they came in to land on a dirt runway."
    scene bg alley_day with fade
    "Everyone left the plane, and was directed through a bustling complex. Tents and canvas structures dotted on top of red dirt. All together it was the size of a small town."
    "A few helicopters were coming and going. Some carried large crates from attachments, others carrying people."
    scene bg slide_0 with fade
    "The group was ushered into a large hall. A large number of people were already seated, facing a projector at the front."
    "Standing at the front of the room was a woman Connor recognised. With a messily tied bun and bags under her eyes, she was attaching a microphone to the collar of her shirt."
    "After confirmation that everyone was seated, she stepped out in front of the projector."
    ch "Hello everyone. Some of you may know me, my name is Charlotte Duval. I head the Murchison Observatory just around the corner. I'm here to tell you what the hell is going on."
    ch "You're questions will be answered, but I've got a little presentation to show you first, okay?"
    "She pressed a button on a small remote she was holding, and the projector lit up."
    scene bg slide_1 with dissolve
    ch "Now, as you all know, four years ago we received a transmission that was undoubtedly of extra-terrestrial origin."
    ch "We soon realised that, because of the differing angles each telescope reported seeing the signal on, that it originated from within our solar system."
    ch "Of course by that point the signal had vanished. Along with our hopes of ever finding the satellite that sent it."
    ch "But we searched. And it was an {i}expensive{/i} search."
    ch "And thanks to the big budgets of the Japanese and the Americans, we {i}actually{/i} did it."
    "Charlotte pressed a button on her remote; the projector flicked to the next side."
    scene bg slide_2 with dissolve
    $ renpy.pause(3, hard=True)
    "The room was speechless."
    "Charlotte waited a moment to make sure that the crowd was actually listening."
    ch "This is a photo taken by the satellite {i}Goodwill{/i}, just over two months ago."
    "Connor was sure most people in this room already knew life was out there. But for the average person, a modulated signal that vanished after a few hours was still pretty easy to deny."
    "But this…"
    "This was real."
    ch "{i}Goodwill{/i} has been studying the satellite for the past month. {i}Your job here{/i}, is to analyse what it's collected so far. Their technology, propulsion, communication."
    ch "We want to know how it got here, how long it's been here, and who sent it."
    ch "Everyone here has been chosen because of their particular skills. If you accept, of course—you will be assembled into teams to analyse certain parts of the satellite. I.e. its physical structure, design, computing."
    ch "You each would have been given a card on your way here. That's your group you've been placed in."
    "Connor, and many others, looked down at their card again."
    ch "This is your chance to help us—{i}all of humanity{/i}. To be a part of history in the making."
    ch "I hope you make the right choice."

label scene3:
    
    $ _history_list = []

    scene bg alley_day with fade
    "Those who stayed (almost everyone) were directed down an alley full of identical tents."
    "By the entrance to each tent was a group name written on a whiteboard. {i}Arecibo{/i} was near the end; Connor made his way inside."
    scene bg tent with fade
    "It was a fairly spacious room."
    "There was a large table in the middle, with desks with computers around the outside. A few whiteboards and a projector were at the back of the room. The room was lit with two long fluorescent lights."
    "There were three others in the room. Two women and a man stood by one of the whiteboards. Chatting as they wrote stuff down."
    "Connor turned around to face a new person he heard enter."
    "It was Ryan."
    "He looked different to when Connor last saw him. He'd cut his hair, for one thing."
    "Maybe a bit skinnier."
    "He was carrying a large mailing tube under his arm."
    r "Connor."
    "Ryan's smile immediately put Connor at ease. It always did."
    c "… Hey."
    r "It's really good to see you here."
    c "You too…"
    "Connor had been hoping he would see Ryan, but hadn't put any thought into what he'd actually say when he did."
    c "Are you still living in South Africa?"
    r "Yep. Still working at SKA-Mid."
    c "They flew you out from there?"
    r "Yeah. I've actually been here for about a week."
    c "Really?"
    r "I've been helping Charlotte. She asked me to head one of the research teams."
    c "… This one?"
    r "Yep."
    "Connor smiled."
    c "You named it Arecibo didn't you."
    "Ryan laughed. Another thing Connor didn't realise he'd missed."
    r "Charlotte let me name all of them, otherwise they would have just been numbers."
    "He looked over at the others by the whiteboard."
    r "Oh good. Everyone's here."
    "He waved Connor over."
    c "Come on, let me introduce you."
    "They hadn't noticed him approach; still talking in front of the whiteboard."
    r "Hello everyone. I'm Ryan, I'll be heading this research team."
    "He motioned to one of the women."
    "This is Linh, she's a mathematician."

    define l = Character("LINH", color="#7e73db")

    l "Hey."
    r "Then there's Pamela, astrophysicist, and Shuyun, astronomer."
    "They both nodded their hello's."
    r "This is Connor, also an astronomer."
    l "… Wait. Connor Lovell?"
    "He nodded."
    "Linh looked to Ryan."
    l "And Ryan Araki?"
    r "Yep."
    l "Oh I'm definitely right then."
    r "Hm?"
    "Linh motioned to the whiteboard. Scribbled down were a list of ideas."
    "{i}New transmission? Logs?{/i}"
    "{i}Satellite origin {s}/ trajectory{/s}{/i}"
    "{i}Wow 2 signal.{/i}"
    l "We were trying to figure out what our group's assignment was."
    l "I figured because of the name {i}Arecibo{/i}, that we'd be looking over the Wow 2 signal again. Maybe all this new data could help us crack it."
    l "And now we've got the two authors of the Wow 2 reply."
    "Ryan smiled."
    r "That's a good guess, but we aren't looking at an old message, we're looking at a new one."
    "Ryan popped the cap of the mailing tube, and pulled out three large sheets of paper, which he set on the table."
    scene bg plaques with fade
    $ renpy.pause(3, hard=True)

    "Being too stunned for words seemed to be a common occurrence today."
    r "These are scans of plaques that were affixed to the hull of the satellite."
    r "Our task is simply to translate them."
    l "Oh my God…"
    "The three plaques were completely different. Some were full of images, others were entirely script."
    "Linh pointed to a section of the second plaque."
    scene bg figures with fade
    $ renpy.pause(2, hard=True)
    l "Is that… them?"
    "Nobody said anything."
    l "They have three eyes."
    "{color=#88cfff}PAMELA{/color}" "… It looks like a bird."
    "They all just stared at the plaques for a moment, taking it all in."
    scene bg plaques with fade
    "Linh traced her hand along a line of braille like dots on the side of the first plaque."
    l "These are numbers."
    "She stared at it for a moment. Then she asked:"
    l "Did this plaque have any colour?"
    r "No, that's what they looked like. Is something wrong?"
    l "No, it's just this numbering system doesn't make any sense."
    r "What is it?"
    l "It's clearly base three—look, they've got unary right next to it—but the symbol for zero and two look the same. I must be missing something."
    "{color=#8cb3e6}SHUYUN{/color}" "What if it {i}is{/i} in different colours, just ones the camera couldn't detect?"
    "Ryan called out to the AI."
    r "Ada?"
    a "Yes sir?"
    r "Can you get the {i}Goodwill{/i} to send us some more pictures of the plaques, this time with a wider spectrum of light?"
    a "Sure thing! Just give it a minute for the transmission delay to and from the satellite."
    "The group gathered around the printer as the new scan was churned out."
    scene bg plaques_colour with fade
    "It was like an entirely new image."
    "Spots of violet and indigo spread evenly throughout the plaque. Highlighting and contrasting certain areas."
    "Linh laughed, and pointed to the numbers."
    l "Look at that, the twos are a different colour."
    "{color=#88cfff}PAMELA{/color}" "But why write it in a colour we can't even see?"
    "{color=#8cb3e6}SHUYUN{/color}" "Animals like birds or butterflies can see ultraviolet light, maybe whoever wrote this can too?"
    c "It's still a strange assumption."
    "Ryan placed a hand on Linh's shoulder."
    r "Well done."

    scene bg tent with fade

    "They made good ground for the first day."
    "Each plaque seemed to focus on a different subject. The first one was full of what looked like math equations and graphs."
    "Now with a proper view of the plaque, Linh had good fun deciphering their arithmetic, describing how it worked with terms Connor didn't understand."
    l "I feel like a kid on Christmas morning."
    "The second focused on the aliens themselves. It had depictions of their star system, planet, and position within the Milky Way."
    "By the looks of it, they weren't far from Earth. On a galactic scale, anyways."
    "The third was what Connor and Ryan found the most interesting. It looked like schematics, or blueprints, detailing the workings of a small device attached to the side of the satellite."
    "Ryan thought they were instructions, but wasn't sure what of. Connor reckoned it looked like some sort of antenna. Though the satellite already had several much larger ones."
    "They had been offered to join breakfast about an hour after arriving at the camp. Most declined; too enveloped in their work."
    "They had split into groups based on their specialities. Linh was deciphering the aliens' mathematics on the first plaque. Pamela and Shuyun were using the maps and diagrams on the second to try and find the aliens' home system."
    "Connor and Ryan were working together on the third plaque to figure out what the significance of the small device was."
    "There was much work to be done."

label scene4:

    $ _history_list = []
    $ quick_menu = False

    scene bg black with fade

    show screen TextDisplay3("{b}5:49 AM, May 16th, 2058.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    scene bg tent with fade
    $ quick_menu = True

    "Connor had no idea when he'd fallen asleep. He had no intention of doing so."
    "When he woke up, hunched over a desk, Ryan was at his side. He pulled a whiteboard from under Conner, which had left some marks across his forearm, and helped him up."
    r "Come on, you're going to miss breakfast."
    c "What time is it?"
    r "About six."
    c "In the morning?"
    "Ryan smiled."
    r "Yes, in the morning."
    c "It's a clock."
    r "What?"
    "Still half asleep, Connor muttered the next few words."
    c "The symbol isn't showing a frequency, it's showing how fast it changes states, like a clock signal."
    "He gently shook Conner by the shoulders."
    r "{i}Breakfast time{/i}, Connor."
    scene bg alley_day with fade
    "Ryan led him down the alley. Connor wiped the sleep from his eyes."
    "As they walked, Ryan nudged Connor with his shoulder."
    r "I'm really glad you came."
    r "I wouldn't want to be doing this with anyone else."
    c "… Reminds me of when we first met. Staying up all night scribbling down codes and symbols."
    r "And now we're doing the reverse."
    scene bg cafeteria with fade
    "It was the liveliest cafeteria Connor had ever seen."
    "Everybody was chatting to somebody, going over what they learned yesterday."
    "MAN" "{i}So they come all this way, just to sit there with their big antennas, and do nothing for eighty years? It's got to be up to something we don't know about.{/i}"
    "WOMAN" "{i}You say that like it's doing something sinister, maybe it's just talking to us with a technology we can't even perceive? ‘Any sufficiently advanced-{/i}"
    "MAN" "{i}Oh don't give me that crap.{/i}"
    "It was pretty obvious that nobody else in the room got any sleep."
    "The two of them grabbed some food, and sat next to Linh. She was chatting with some computer scientists."
    define w = Character("WOMAN", color="#6ac2c5")
    define m = Character("MAN", color="#6ac581")
    w "Get this: {i}optical computing.{/i}"
    "The woman enunciated the phrase with her hands."
    w "They shoot fuckin' laser beams through the ship to deliver data signals."
    c "Don't we have optical computers?"
    m "We have optical {i}chips{/i}, and boards, but ultimately they still talk to the rest of the computer with electricity."
    r "So how far ahead of us does that make them?"
    w "Hard to say. All I know is that it took us all day just to realise what we were looking at."
    "The pair left to chase after some aerospace engineers. Linh turned to Ryan and Connor."
    l "I just wanted to say I'm a big fan of your work together."
    r "Our work?"
    l "On the Wow 2 reply. I think it's amazing how fast you put that together."
    c "It was based on a paper I wrote in university."
    l "Yes, I read it. You had to convert the whole thing to ternary. How did you decide what to do with the additional dimension?…"


label scene5:

    $ _history_list = []
    $ quick_menu = False

    scene bg black with Fade(1.0,0.0,1.0)

    show screen TextDisplay3("{b}8:12 PM, May 19th, 2058.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    $ quick_menu = True

    scene bg tent with fade

    "The whiteboards at the back of the {i}Arecibo{/i} tent were filled with the scribblings of a madwoman. Linh had fully translated the first plaque."
    "It appeared its purpose was in establishing a counting system, and arithmetic rules and operators."
    "Common symbols used across the plaques were also defined there: {i}Wavelength, Frequency, input, speed{/i}. They even had their own symbols for certain elements."
    "Units of measurement for distance and time (which Linh had lovingly named gleeps and glorps) had been confirmed using the plaques provided methods of error checking."
    "The rest of the group argued that this achievement earned her some proper sleep. Linh disagreed."
    "Pamela and Shuyun hadn't found their home system yet, but they were crossing off stars; it was still progress."
    "They had two clues: the makeup of the system itself. A binary star system with three planets; and a map detailing the emission spectra of nearby stars."
    "Finding it would require a lot of searching the sky."


label scene6:

    $ _history_list = []
    $ quick_menu = False

    scene bg black with Fade(1.0,0.0,1.0)

    show screen TextDisplay3("{b}10:46 PM, May 23rd, 2058.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    $ quick_menu = True

    scene bg tent with fade

    "A few days had passed and Ryan and Connor hadn't made any headway with the third plaque."
    "Thanks to Linh, they had most of the technical specifications down for the device described on the plaque."
    "It was definitely an antenna, a lot smaller and less powerful than the satellite's main four, but it was somehow deemed significant enough to deserve it's own plaque."
    "It was possible that they were just sharing the technology with them, but Ryan couldn't help but feel that the plaque was some sort of instruction manual."
    "Connor trusted Ryan's feeling."
    "Connor decided to take a break, and disappeared out the tent."
    "Ryan stayed behind for a little while, before following."
    scene bg stars with fade
    "He found Connor just outside the camp. He hadn't gone far—probably too afraid of snakes and spiders and possibly giant lizards."
    "He was sat on a rock, head tilted up to the stars."
    r "Hey."
    c "Hey."
    "Connor scooted over on the rock. Ryan sat down with him, and looked up at the sky."
    c "How far away do you think it is?"
    r "The satellite?"
    c "Their home system."
    r "… I don't know."
    c "Any one of these stars could be theirs."
    c "The same sky humans have been looking up at for thousands of years. They've been there the whole time."
    r "… Do you get these profound thoughts often?"
    "Connor smiled."
    c "Shut up."
    "Neither of them said anything for a long while. Connor rested his head on Ryan's shoulder."
    c "The only reason I came here was because I thought I'd see you."
    r "… I don't believe that for a second."
    c "Well, it was a {i}contributing factor{/i}."
    r "Uh-huh."
    c "A pretty big one, I might add."
    "Ryan giggles."
    "They sat in contented silence for a long while."
    c "Have you ever thought that maybe the aliens did the same?"
    r "… What do you mean?"
    c "Everybody's stressing about what the aliens want. Why did they send the probe? What are they doing?"
    c "I had no idea what I was signing up for when I came here, I just knew why I was going."
    c "Maybe they just… Wanted to see us. To talk to us."
    r "… That's pretty self centred, isn't it?"
    c "We've spent {i}hundreds{/i} of years looking up at the stars, {i}searching{/i} for others like us."
    c "If we found out about {i}them{/i}. The {i}only known intelligent life{/i} besides us, wouldn't we do the same?"
    r "But the satellite {i}isn't{/i} talking to us. It's only sent two messages in eighty years."
    c "Well talking goes two…"
    "Connor paused, then jerked his head up."
    c "It's waiting."
    r "Waiting for what?"
    c "For us. It's waiting for us!"
    "Connor stood up, grabbed Ryan's hands, and dragged him to his feet."
    c "It's not a science vessel, it's not a war machine."
    c "Ryan, it's a comms relay."
    c "They've told us they're here, now they're just waiting for us to pick up the phone."
    "Connor took Ryan's face in his hands, and kissed him."
    c "You're amazing."
    r "I didn't do anything!"
    c "I know."
    "Connor took Ryan's hand and led them back towards the camp."
    scene bg alley_night with fade
    c "{i}That's{/i} what the third plaque is. It's instructions on how to operate the antenna. It's not describing how it sends signals, but what to send so it understands what it {i}receives.{/i}"
    c "I mean, this might hold the key to faster than light communication. Or even {i}travel{/i}. They {i}had{/i} to have-"
    "Ryan stopped Connor up against one of the tents, and kissed him again. And a few more times after that."
    "They broke apart slowly. Connor stared into his eyes."
    c "… How did I ever let you leave?"
    r "You have a life in Perth, I understood that."
    "Connor hugged his arms around Ryan's neck."
    c "I don't want to let you go again."
    c "I want to go with you. To South Africa… Or wherever you go after this."
    "Ryan said nothing for a moment. Connor started to blush."
    c "T- Tell me if I'm overstepping. I get it if-"
    r "Yes."
    c "… Hm?"
    "Connor wasn't sure what Ryan had said yes to."
    "A kiss on Connor's cheek answered that question."
    c "What do you say we go figure out how to talk to them?"
    "Ryan nuzzled into Connor's neck."
    r "In a minute."

label epilogue:

    $ _history_list = []

    $ quick_menu = False
    scene bg vega with Fade(2,3,2)

    $ renpy.pause(2, hard=True)

    show screen TextDisplay1("Vega (Alpha Lyrae) A.", 0.05, 0.05)

    $ renpy.pause(2, hard=True)

    show screen TextDisplay4("26 light years from Earth.", 0.1, 0.05)

    $ renpy.pause(3, hard=True)

    hide screen TextDisplay1 with dissolve
    hide screen TextDisplay4 with dissolve

    scene bg black with fade

    show screen TextDisplay3("{b}14:29:15Z, December 7th, 2232.{/b}", 0.35, 0.05)

    $ renpy.pause(4, hard=True)

    hide screen TextDisplay3 with dissolve

    scene bg module with fade
    $ quick_menu = True

    "London anxiously flipped between the different camera modes on her visor."
    "The pitch black module flicked in and out of sight as she viewed it through night vision and ultraviolet lenses."
    "Their species was sensitive to light, so the only real illumination in the module came from dim strips across the front of each of her group's helmets."
    "Meers checked the translator device. {i}Again{/i}. The waiting was making everyone nervous."
    "The ship creaked. A chime over the intercom indicated that their ship had just docked. A few seconds later, the hatch in front of them shifted."
    "London and her group straightened their stances."
    "They were {i}only{/i} the representatives of the entire human race, who had travelled twenty-six light years to the halfway star between their civilisations, to make a good first impression."
    "No pressure."
    "The hatch slowly creeped open."
    scene bg alien with Fade(1.0,0.0,1.0)
    $ renpy.pause(4, hard=True)
    "Meers' translator blinked to life."
    $ quick_menu = False
    # scene bg black with Fade(2,0,2)
    # # play sound
    # show screen TextBox1("{noalt}Hello.{/noalt}", 0.5,0.5) 
    # $ renpy.pause(3, hard=True)
    # hide screen TextBox1


label end:

    $ quick_menu = False
    scene bg black with Fade(2.0,1.5,2.0)

    show screen TextBox("A Starless Void", 0.5,0.5) with dissolve
    $ renpy.pause(3, hard=True)
    hide screen TextBox with dissolve

    $ renpy.pause(1, hard=True)

    show screen TextBox("A Game by Liam Latz", 0.5,0.5) with dissolve

    $ renpy.pause(3, hard=True)

    hide screen TextBox with dissolve

    $ quick_menu = True
    return
