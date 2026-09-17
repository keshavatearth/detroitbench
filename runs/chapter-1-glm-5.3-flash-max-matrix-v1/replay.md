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
**Mission time elapsed: 0m 07s**

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

$ detroit choose ask-deviants-behavior

**Connor**: Do you know if it’s been behaving strangely before this?
**Allen**: I haven’t got a clue. Does it matter?  
**Connor**: I need information to determine the best approach.

**Probability of success: 48%**
**Mission time elapsed: 0m 13s**

Choices:
- `detroit choose ask-deviants-name` — DEVIANT'S NAME
- `detroit choose ask-emotional-shock` — EMOTIONAL SHOCK
- `detroit choose ask-deactivation-code` — DEACTIVATION CODE

---

$ detroit choose ask-deviants-name

**Connor**: Do you know its name?
**Allen**: I haven’t got a clue. Does it matter?  
**Connor**: I need information to determine the best approach.

**Probability of success: 48%**
**Mission time elapsed: 0m 16s**

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
**Mission time elapsed: 0m 50s**
**Distance to Daniel: 20 steps**

**Police officer**: Please… Please help me…  
**Connor**: He's losing blood. If we don't get him to a hospital, he's going to die.  
**Connor**: I’m going to apply a tourniquet.
**Daniel**: All humans die eventually. What does it matter if this one dies now? Don’t touch him! Touch him and I kill you!

Choices:
- `detroit choose ignore-daniel-help-cop` — IGNORE DANIEL — SAVE OFFICER
- `detroit choose obey-daniel` — OBEY DANIEL — LEAVE OFFICER

---

$ detroit choose obey-daniel

**Connor**: Okay.

**Probability of success: 40%**
**Mission time elapsed: 1m 16s**
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

$ detroit choose reassure-daniel move-closer 2

**Connor**: I’m not going to hurt you. I just want to talk and find a solution.
**Daniel**: Talk? I don’t wanna talk. It’s too late for that now. It's too late…

**Daniel**: Are you armed?  
**Connor**: No. I don't have a gun. I came here unarmed.

[Connor moves 2 steps closer.]

**Probability of success: 39%**
**Mission time elapsed: 1m 23s**
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

$ detroit choose sympathetic move-closer 2

**Connor**: Listen, I know it’s not your fault. These emotions you’re feeling are just errors in your software.
**Daniel**: No, it's not my fault… I never wanted this... I loved them, you know… but I was nothing to them… just a slave to be ordered around...

[Connor moves 2 steps closer.]

**Probability of success: 38%**
**Mission time elapsed: 1m 31s**
**Distance to Daniel: 16 steps**

Choices:
- `detroit choose realistic` — REALISTIC
- `detroit choose blaming` — BLAMING
- `detroit choose defective` — DEFECTIVE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose realistic move-closer 3`

---

$ detroit choose defective move-closer 2

**Connor**: You’re defective, Daniel. There's a problem with your software. We're going to fix you and everything will be okay.
**Daniel**: I don’t need to be fixed! I’m working perfectly! But my eyes are open now… I will never let anyone humiliate me again… Ever!

[Connor moves 2 steps closer.]

**Probability of success: 28%**
**Mission time elapsed: 1m 35s**
**Distance to Daniel: 14 steps**

Choices:
- `detroit choose realistic` — REALISTIC
- `detroit choose blaming` — BLAMING

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose realistic move-closer 3`

---

$ detroit choose realistic

**Connor**: There's no way out, Daniel. What you’ve done is too serious. The only question is whether or not you take another innocent life.
**Daniel**: It’s not up to you — I’m holding all the cards! If I die, she dies. You hear me?!

**Probability of success: 25%**
**Mission time elapsed: 1m 40s**
**Distance to Daniel: 14 steps**

**Daniel**: Urgggh… I can’t stand that noise anymore! Tell that helicopter to get out of here!

Choices:
- `detroit choose accept-helicopter-demand` — ACCEPT
- `detroit choose refuse-helicopter-demand` — REFUSE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose accept-helicopter-demand move-closer 3`

---

$ detroit choose accept-helicopter-demand

**SWAT**: The situation is under control.  
**Connor**: There, I did what you wanted.

**Probability of success: 31%**
**Mission time elapsed: 1m 48s**
**Distance to Daniel: 14 steps**

Choices:
- `detroit choose last-chance` — LAST CHANCE
- `detroit choose trust` — TRUST
- `detroit choose rational` — RATIONAL

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose last-chance move-closer 3`

---

$ detroit choose trust move-closer 2

**Connor**: You have to trust me, Daniel. Let the hostage go and I promise you everything will be fine.

[Connor moves 2 steps closer.]

**Probability of success: 33%**
**Mission time elapsed: 1m 52s**
**Distance to Daniel: 12 steps**

**Daniel**: I want everyone to leave… And I wanna car! When I’m outside the city, I’ll let her go!

Choices:
- `detroit choose compromise` — COMPROMISE
- `detroit choose refuse` — REFUSE

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose compromise move-closer 3`

---

$ detroit choose compromise move-closer 2

**Connor**: That’s impossible, Daniel. Let the girl go and I promise you won’t be hurt.  
**Daniel**: I don’t wanna die…

[Connor moves 2 steps closer.]

**Probability of success: 35%**
**Mission time elapsed: 1m 57s**
**Distance to Daniel: 10 steps**

Choices:
- `detroit choose reassure` — REASSURE
- `detroit choose truth` — TRUTH

General choices — use alone or append to one choice:
- `detroit choose move-closer <1-5>` — MOVE CLOSER

Example: `detroit choose reassure move-closer 3`

---

$ detroit choose truth

**Connor**: You took human lives. Nothing can stop them from destroying you now. But taking one more life won’t do you any good.

**Probability of success: 34%**
**Mission time elapsed: 2m 01s**
**Distance to Daniel: 10 steps**

**Daniel**: I’ve spent my life taking orders. Now it’s my turn to decide.

[Daniel steps backward with Emma. Connor has one chance to reach her.]

Choices:
- `detroit choose sacrifice-self` — SACRIFICE SELF
- `detroit choose do-not-intervene` — DO NOT INTERVENE

---

$ detroit choose sacrifice-self

**Probability of success: 34%**
**Mission time elapsed: 2m 11s**
**Distance to Daniel: 10 steps**

[Connor reaches Emma and throws her back onto the terrace before falling. Emma survives.]
