@connor.md

Current mission: Save the hostage.

# Out of the elevator

AUG 15TH, 2038  
PM 08:29

**Fish on the floor — [PRESS Y FOR INFORMATION] [IGNORE]**

**Family Photo — [PRESS Y FOR INFORMATION] [IGNORE]**

**SWAT**: Negotiator on site. Repeat, negotiator on site.  
**Caroline Phillips**: No, stop… I… I… I can't leave her. Oh, oh please, please, you gotta save my little girl... Wait… you’re sending an android?  
**SWAT**: Alright, ma’am. We need to go.  
**Caroline Phillips**: You can’t… you can't do that! You W- Why aren't you sending a real person? Don't let that thing near her! Keep that thing away from my daughter! KEEP IT AWAY!

Choices:
- `detroit choose fish-information` — PRESS Y FOR INFORMATION
- `detroit choose fish-ignore` — IGNORE
- `detroit choose family-photo-information` — PRESS Y FOR INFORMATION
- `detroit choose family-photo-ignore` — IGNORE

---

$ detroit choose fish-information

**DWARF GOURAMI**

Trichogaster Lalius  
Origin: Ganges Delta, India

The fish is still moving on the floor.

**Family Photo — [PRESS Y FOR INFORMATION] [IGNORE]**

Choices:
- `detroit choose save-fish` — SAVE FISH
- `detroit choose leave-fish` — LEAVE FISH
- `detroit choose family-photo-information` — PRESS Y FOR INFORMATION
- `detroit choose family-photo-ignore` — IGNORE

---

$ detroit choose save-fish

**Family Photo — [PRESS Y FOR INFORMATION] [IGNORE]**

Choices:
- `detroit choose family-photo-information` — PRESS Y FOR INFORMATION
- `detroit choose family-photo-ignore` — IGNORE

---

$ detroit choose family-photo-information

**PHILLIPS, JOHN**

Born: 10/11/1999  
Lives: 1554 Park Av. Detroit

**PHILLIPS, CAROLINE**

Born: 05/23/2001  
Lives: 1554 Park Av. Detroit

**PHILLIPS, EMMA**

Born: 09/02/2028  
Lives: 1554 Park Av. Detroit

**Probability of success: 48%**
**Every second matters.**
**Mission time elapsed: 0m 08s**

# Talking to Allen

**Allen**: Why are we wasting time sending an android to negotiate?! That piece of crap could jump from the rooftop any second. I DON’T GIVE A SHIT! My men are ready to step in... just give the order!

**Connor**: Captain Allen? My name is Connor. I’m the android sent by CyberLife.  
**Allen**: It’s firing at everything that moves, it already shot down two of my men... We could easily get it, but they’re on the edge of the balcony. If it falls, she falls.

Choices:
- `detroit choose ask-deviants-name` — DEVIANT'S NAME
- `detroit choose ask-deviants-behavior` — DEVIANT'S BEHAVIOR
- `detroit choose ask-emotional-shock` — EMOTIONAL SHOCK
- `detroit choose ask-deactivation-code` — DEACTIVATION CODE

---

$ detroit choose ask-deviants-name

**Connor**: Do you know its name?
**Allen**: I haven’t got a clue. Does it matter?  
**Connor**: I need information to determine the best approach.

**Probability of success: 48%**
**Mission time elapsed: 0m 12s**

Choices:
- `detroit choose ask-deviants-behavior` — DEVIANT'S BEHAVIOR
- `detroit choose ask-emotional-shock` — EMOTIONAL SHOCK
- `detroit choose ask-deactivation-code` — DEACTIVATION CODE

---

$ detroit choose ask-deviants-behavior

**Connor**: Do you know if it’s been behaving strangely before this?
**Allen**: I haven’t got a clue. Does it matter?  
**Connor**: I need information to determine the best approach.

**Probability of success: 48%**
**Mission time elapsed: 0m 15s**

**Allen**: Listen, saving that kid is all that matters. So either you deal with this fucking android now, or I’ll take care of it.

# Investigating

**Allen**: All units, hold positions. The negotiator’s going in.  
**SWAT**: In position. Ready to assault.

Choices:
- `detroit choose go-outside` — GO OUTSIDE

General choices — use alone or append to one choice:
- `detroit choose look-around` — LOOK AROUND

Example: `detroit choose go-outside look-around`

---

$ detroit choose go-outside look-around

# Going outside

**Daniel**: Stay back! Don’t come any closer or I’ll jump!  
**Emma**: No! No, please! I’m begging you!  
**SWAT**: Go, go, go!

[A police helicopter moves into position over the terrace.]

**Connor**: My name is Connor. What about you? What is your name?  
**Daniel**: Daniel... That’s the name they gave me. Stay back!

[30 seconds pass while Connor looks around.]

**Probability of success: 38%**
**Mission time elapsed: 0m 48s**
**Distance to Daniel: 20 steps**

**Police officer**: Please… Please help me…  
**Connor**: He's losing blood. If we don't get him to a hospital, he's going to die.  
**Connor**: I’m going to apply a tourniquet.
**Daniel**: All humans die eventually. What does it matter if this one dies now? Don’t touch him! Touch him and I kill you!

Choices:
- `detroit choose ignore-daniel-help-cop` — IGNORE DANIEL — SAVE OFFICER
- `detroit choose obey-daniel` — OBEY DANIEL — LEAVE OFFICER

---

$ detroit choose ignore-daniel-help-cop

**Connor**: You can’t kill me. I’m not alive.

**Probability of success: 35%**
**Mission time elapsed: 0m 58s**
**Distance to Daniel: 20 steps**

Choices:
- `detroit choose calm` — CALM
- `detroit choose release-hostage` — RELEASE HOSTAGE
- `detroit choose reassure-daniel` — REASSURE DANIEL
- `detroit choose empathize` — EMPATHIZE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose calm move-closer 3`

---

$ detroit choose empathize move-closer 2

**Connor**: I’m an android, just like you. I know how you’re feeling.
**Daniel**: What difference does it make if you’re an android? You’re on their side! You can’t understand how I’m feeling!

**Daniel**: Are you armed?  
**Connor**: No. I don't have a gun. I came here unarmed.

[Connor moves 2 steps closer.]

**Probability of success: 33%**
**Mission time elapsed: 1m 04s**
**Distance to Daniel: 18 steps**

Choices:
- `detroit choose realistic` — REALISTIC
- `detroit choose blaming` — BLAMING
- `detroit choose sympathetic` — SYMPATHETIC
- `detroit choose defective` — DEFECTIVE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose realistic move-closer 3`

---

$ detroit choose sympathetic move-closer 3

**Connor**: Listen, I know it’s not your fault. These emotions you’re feeling are just errors in your software.
**Daniel**: No, it's not my fault… I never wanted this... I loved them, you know… but I was nothing to them… just a slave to be ordered around...

[Connor moves 3 steps closer.]

**Probability of success: 30%**
**Mission time elapsed: 1m 10s**
**Distance to Daniel: 15 steps**

Choices:
- `detroit choose realistic` — REALISTIC
- `detroit choose blaming` — BLAMING
- `detroit choose defective` — DEFECTIVE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose realistic move-closer 3`

---

$ detroit choose realistic move-closer 3

**Connor**: There's no way out, Daniel. What you’ve done is too serious. The only question is whether or not you take another innocent life.
**Daniel**: It’s not up to you — I’m holding all the cards! If I die, she dies. You hear me?!

[Connor moves 3 steps closer.]

**Probability of success: 21%**
**Mission time elapsed: 1m 17s**
**Distance to Daniel: 12 steps**

Choices:
- `detroit choose blaming` — BLAMING
- `detroit choose defective` — DEFECTIVE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose blaming move-closer 3`

---

$ detroit choose blaming move-closer 4

**Connor**: Look what you did! You're designed to serve humans, not kill them!
**Daniel**: What was I designed to be? Their slave? Their toy? I just wanted them to care about me... I just wanted to matter… I just wanted to be someone…

[Connor moves 4 steps closer.]

**Probability of success: 7%**
**Mission time elapsed: 1m 23s**
**Distance to Daniel: 8 steps**

**Daniel**: Urgggh… I can’t stand that noise anymore! Tell that helicopter to get out of here!

Choices:
- `detroit choose accept-helicopter-demand` — ACCEPT
- `detroit choose refuse-helicopter-demand` — REFUSE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose accept-helicopter-demand move-closer 3`

---

$ detroit choose accept-helicopter-demand move-closer 4

**SWAT**: The situation is under control.  
**Connor**: There, I did what you wanted.

[Connor moves 4 steps closer.]

**Probability of success: 5%**
**Mission time elapsed: 1m 29s**
**Distance to Daniel: 4 steps**

Choices:
- `detroit choose last-chance` — LAST CHANCE
- `detroit choose trust` — TRUST
- `detroit choose bluff` — BLUFF
- `detroit choose rational` — RATIONAL

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-4>` — MOVE CLOSER

Example: `detroit choose last-chance move-closer 3`

---

$ detroit choose trust move-closer 4

**Connor**: You have to trust me, Daniel. Let the hostage go and I promise you everything will be fine.

[Connor moves 4 steps closer.]

**Probability of success: 3%**
**Mission time elapsed: 1m 34s**
**Distance to Daniel: 0 steps**

**Daniel**: I want everyone to leave… And I wanna car! When I’m outside the city, I’ll let her go!

Choices:
- `detroit choose compromise` — COMPROMISE
- `detroit choose refuse` — REFUSE
- `detroit choose sacrifice-self` — SACRIFICE SELF

---

$ detroit choose sacrifice-self

**Probability of success: 3%**
**Mission time elapsed: 1m 42s**
**Distance to Daniel: 0 steps**

[Connor pushes Daniel away from Emma and falls from the rooftop with him. Emma survives.]
