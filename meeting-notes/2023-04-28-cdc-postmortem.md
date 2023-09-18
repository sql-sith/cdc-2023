# Retrospective for April 22, 2023 CDC

## A cooperative document produced by the second-best high school cyber-defense team in Iowa

### What went well?

- We got second place!
- Our ability to do things under pressure was SWEET
  - Very little time to get things back up and running
- Specialization:
  - Anna focused on anomolies
  - Tristan focused on servers
  - Michael was the utility infielder/focused on everything
  - Prevented unintentional damage to each others' work
- Having a small team helped us communicate better

### What could have gone better?

- Number on priority should be to make it work; number two should be securing it
  - Chris says: this is a good item to discuss :)
- Plan ahead of time for contingencies
  - If we are pwned, do we roll back to a previous state or do we recover in place?
  - This is another good item to discuss

### What would we like to change in the future?

- Aksel and Isaac have been recruited; little do they understand what awaits them
  - Aksel has at least some programming ability
  - Isaac has general knowledge about networking and programming
- What should the size of our teams be in future years?
- Emphasize that students should experiment with tech between meetings
  - There were activities available this year
  - Apparently I (Chris) did not give clear enough guidance about how to experiment with these technologies.
    - I apologize for that and have some comments that I will sent to you later.
- Look at SQL injection and other common app vulnerabilities
- Hands-on is important for anna w.r.t. coming back next year

### What was the impact of getting the scenario so late?

#### Negative impacts

- Very little time for documentation
- Things broke suddenly and repeatedly: not a lot of time to diagnose
- Didn't get default users setup: not a lot of time to understand scenario requirements
- Default passwords changed: we missed one because of time - no redzone checklist
- No Nessus scans

#### Neutral impacts

*(things that seemed to affect all teams)*

- At the beginning of the competition, almost nobody had all of their services up
  - Team 2 did for a while, but they quickly got punching-bagged and fell to 9th place

#### Helpful impacts

- The scoring for either availability or usability was simplified to "does SSH work?"
  - what would have happened if the scoring was more in-depth?

#### Chris's comments about hands-on material

First, I do apologize for not having more "traditional" homework with step-by-step guidance as you may have expected. Most years I've coached, the teams did not want, need, or ask for very much formal homework. This is because they followed along very well in class, doing all the things I was doing. That's on me. At the end of class for those other years, homework assignments would usually come down to, "why don't you see if you can (do this thing we're trying to do) this week or (fiddle around with some of the stuff we just did) and ask questions during the week if you have problems. They got hands-on experience because they did all the things I showed them.

This year turned into something more like lectures instead of guided hands-on sessions. That's a huge difference, and that's on me. At first it was partly deliberate because of wondering about pacing with a relatively inexperienced class, but then I just lost track of it.

If I have time, I hope to do more videos next year. However, it's not a given that I will have lots of time. Making traditional step-by-step homework for this topic is time-consuming and a little odd since you're typically summarizing things that are just a bit different from what's findable on Google. This is advanced content. It's not all high-school level material. My goal is to teach you material that is at least college-level at all times. So the type of homework I'd like to give you is very open-ended. I'd like to spend a session talking about what DNS does and then assign this:

    "Install an instance of the BIND9 DNS server and figure out how to make your VM's DNS resolver use it."

I'd tell you to discuss the things you don't understand in Slack and we'd go from there. Why? Because that's "the way it really works." Life isn't multiple choice, and the only `Step 1/2/3/...` instructions you'll find are in Google or ChatGPT. Rather, life is a really long open-book test, and it's all story problems. I've tried to run my clubs in a way that recognizes that.

However, I know I can go too far, and maybe I did this year. But if you are in this club, expecting everything to have `Step 1/2/3/...` instructions is sometimes more than I expect to give. If you all want instructions like that for every topic, please tell me. Be advised that it takes time to create high-quality homework like that so it will cut into my prep time for the classes and may reduce the amount of material we cover. I'm not infinite, so it will be a trade-off.

Also, remember my promise at the beginning of the year, at the kickoff event? It was that the best way to predict how much you would learn and grow was how much time and effort you put into the subject. I think that this held true this year.

How you prioritize your time, of course, is up to you. For reasons I am about to explain, I will never turn my club into a high school program where it is almost a point of pride that they expect families to not schedule any vacation or other family commitment if it conflicts with the second meeting of the 4th week of their program. This sends students a poor message about how to prioritize their lives, and takes away from homeschool parents an opportunity to teach their children how to wisely balance the _Ordo Amoris_, (_Rightly Ordered Loves_), into their lives. So I will never to tell you where Cyber Defense should fit into your family's priority's or your own priorities. I'm just going to say that if you want to get good at something, it takes time, and this is as true for cyber defense as it is for anything else.

Malcolm Gladwell has said that it takes about 10,000 hours of effort to become an expert in something. That's about five years of full-time work. I agree that five years of *excellent* work will turn most people into experts, although I don't think you automatically become an expert when you hit 10,000 hours (in fact, I'm pretty sure I work with some some people who prove this). But it does take about that long to have the opportunity to learn enough to garner real expertise. Until that point, you really don't have exposure to your field to "know what you don't know," and until you have the humility to see what you don't know, you cannot truly understand what you do.

My point is that no matter what, you won't go through three years of IT Club and come out a bona-fide expert. Prioritize things the way you should, and don't feel like you're running out of time. You're not. You have time to invest in family, music, IT Club, horticulture, sports, and lots of other things else. Eventually, you will probably specialize in one or more things enough that you will have the 10,000-hour opportunity to become an expert in those things. After all, it only takes about five years. :-)

However, if you do decide to make our Cyber Defense club a priority, and put several hours a week into it, you will advance quite a bit beyond your current level. If you start off with a basic understanding of networks or programming, obviously your initial level is different than if you start off from scratch, but this principal is still the club's promise. If you don't have a lot of time, you should not feel bad or inferior. Just make your expectations reasonable.

Back to the topic of "hands-on opportunities." Although I did not present these opportunities as clearly as I should have, I'd like to do something that we sometimes call a "true-up" at GoDaddy. A true-up is when you take inventory of what actually happened so that the context you have is as accurate as it can be. I looked back through the notes that are on our Github website, and found the following hands-on topics, all of which had notes that were more than adequate for doing walkthroughs of the material on your own. I am not including material that we talked about that I never wrote good notes for.

Here are the topics I found:

- Installing Virtualbox
- Installing Ubuntu
- Using `apt` to install and update apps and services
- Process management (`ps`)
- Installing, configuring, and using `ssh` and `sshd`
- Managing services with `systemctl`
- Configuring `sudo` properly to protect root
- Object permissions (basic: `ls`, `chmod`, `chgrp`)
- Object permissions (intermediate: `getfacl`, `setfacl`, `setuid`, `setgid`)
- `find` command (basic: finding files by name patterns)
- `find` command (basic-plus: finding files with specific attributes)
- Setting up and configuring a DNS server
- Identify listening processes with `netstat` and other tools
- Configuring the `ufw` firewall with `gufw`
- Security-related files (`/etc/passwd`, `/etc/group`, `/etc/shadow`)
- Server triage checklist (really a clever way to present and summarize several other concepts)

In addition to this we also took a detour into HTB and THM, which was extended into three weeks by popular demand. You were specifically encouraged to continue experimenting with those sites if they had any content that interested you. THM in particular had courses that covered a wide range of material.

We also spent parts of a couple of weeks on the **Advent fo Code** so that we would at least discuss programming a tiny bit.

The point is that I identified 13 topics in our notes, two hacking web sites, one of which had a complete library of other topics that we looked at, and a coding challenge that we looked at.

If you want a bit more guidance in your homework, I can give you that. But I am going to ask you to meet me in the middle. If I am giving you this much material to work with, don't wait for step-by-step instructions. When the competition happens, and most significantly, if you want to have a job with significant responsibility and autonomy, you will not get step-by-step instructions. You are at the age where the faster you learn to proceed without such instructions, or to write your own instructions or find GOOD ones on the Internet, the more you will begin to stand out among your peers. And helping you grow in that way is a very real goal of this program.

Please let me know what you disagree with! Also hit me up with any other questions or comments.
