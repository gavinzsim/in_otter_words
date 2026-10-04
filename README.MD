# In Otter Words

### In Otter Words

**When the world needs more than simply being as is. In Otter Words, a change...**

**In Otter Words** is an environmental visual novel created for **StormHacks 2026**.

The story follows **Yinny**, an otter living in a city where things are clearly starting to go wrong. Garbage is piling up, the river is polluted, infrastructure is falling behind, and more people are starting to question whether meaningful change is even possible.

Instead of watching those problems happen from the sidelines, the player gets to do something about them.

Throughout the game, Yinny works with four other otters to tackle different parts of the city's problems. Players make decisions about community action, spending, sustainability, technology, and responsibility. Those choices shape the city, Yinny's relationships, and the future they eventually create.

The characters are inspired by the mascots of **SFU Surge**, the student organization behind StormHacks. We wanted the project to feel connected to the hackathon itself while giving each mascot a personality and role that fits into the story.

At its core, **In Otter Words** is about one idea:

> Change does not have to be perfect to matter.

## Featuring

### Stormy 🔵
The group's inventor. Stormy's story focuses on innovation, teamwork, and responsible technology.

### Sparky 🟠
Energetic but skeptical. Sparky explores optimism, cynicism, and whether change is still worth pursuing.

### Trendy 🩷
Social, expressive, and great at getting people involved. Trendy helps turn the city's garbage problem into a community effort.

### Spendy 🟢
Practical and cost-conscious. Spendy focuses on balancing environmental improvements with what the city can realistically afford.

---

# The Problem

Environmental issues can feel overwhelming.

Climate change, pollution, waste, infrastructure, and sustainability are massive problems, and it is easy to feel like one person's choices cannot possibly make a difference. At the same time, real environmental decisions are rarely simple.

Cities have to balance:

- environmental impact
- cost
- public support
- infrastructure
- safety
- technology
- long-term consequences

The most sustainable solution is not always the most realistic one, and that is what we wanted to explore.

**In Otter Words** turns these problems into choices the player actually has to make. Instead of simply telling players what is right or wrong, the game lets them weigh different options, see the consequences, and decide what kind of change is worth pursuing.

The message behind the game is simple:

> You do not need to fix everything at once. You just need to start making things better.

---

# Sustainable Development Goals

## Primary Goal: SDG 11, Sustainable Cities and Communities

**In Otter Words** is built primarily around **United Nations Sustainable Development Goal 11: Sustainable Cities and Communities**.

SDG 11 focuses on making cities safer, more resilient, more inclusive, and more sustainable.

That is also the central challenge of the game.

Yinny is not trying to solve one isolated environmental problem. The player is trying to improve an entire city while dealing with waste, water, infrastructure, public participation, limited resources, and new technology.

Each story arc explores a different part of building a sustainable community:

| Story Arc | Challenge | Connection to SDG 11 |
| --- | --- | --- |
| **Trendy** | Garbage and low community involvement | Building cleaner communities through public participation and collective action |
| **Spendy** | Polluted water and limited budgets | Improving city infrastructure while keeping solutions realistic and affordable |
| **Sparky** | Cynicism and lack of motivation | Encouraging people to stay involved in long-term community improvement |
| **Stormy** | New technology and its risks | Using innovation responsibly to improve how a city functions |
| **Yinny** | Bringing everything together | Showing how individual decisions can contribute to wider city-level change |

The city changes throughout the game based on what the player chooses to prioritize. A more sustainable outcome requires more than simply picking the most environmentally friendly answer. Players also have to consider whether a solution is affordable, safe, supported by the community, and realistic enough to actually work.

That balance is at the heart of SDG 11 and at the heart of **In Otter Words**.

## Supporting SDGs

The game's problems also connect directly to several other UN Sustainable Development Goals.

### SDG 6: Clean Water and Sanitation

Water pollution is one of the city's biggest problems.

Through Spendy's story and the river cleanup minigame, players deal with polluted waterways, water quality, and the infrastructure needed to keep water systems healthy.

### SDG 12: Responsible Consumption and Production

The garbage problem highlights how everyday consumption creates waste that communities eventually have to manage. Trendy's story focuses on cleanup, awareness, and encouraging people to take more responsibility for the waste around them.

### SDG 13: Climate Action

The wider message of the game is that environmental progress depends on people being willing to act. Sparky's story especially focuses on the feeling that environmental problems are too large to change. The game challenges that idea by showing how smaller actions, community involvement, and long-term thinking can build toward something larger.

Together, these goals support the main idea behind the project:

> Sustainable cities are not created by one perfect solution. They are created through many decisions about people, resources, infrastructure, and the environment.

---

# Gameplay

**In Otter Words** is a choice-driven visual novel where the player controls Yinny through four main story arcs.

The player's choices affect:

- environmental progress
- relationships
- community support
- responsibility
- practicality
- optimism
- innovation

There is not always an obvious correct answer. A choice might be better for the environment but far more expensive. Another might be easier to implement but less effective.

The player has to decide what matters most.

---

# River Cleanup Minigame

The game also includes a 60-second river cleanup minigame.

- Garbage gives **+1 point**
- Wildlife gives **-1 point**

The player's result is saved and contributes to the state of the city later in the story.

---

# Your Choices Matter

Important decisions are recorded throughout the game and grouped into three general levels:

- strong
- reasonable
- poor

The game also tracks traits and relationships with Trendy, Spendy, Sparky, and Stormy. No single decision defines the player's run. Instead, the game looks at the full pattern of choices they made. By the end, all of those decisions add up.

---

# The Finale

The ending is built around the player's journey.

The game considers:

- major decisions
- relationships
- environmental progress
- river cleanup performance
- community support
- the outcome of Stormy's machine

Those pieces are combined into a personalized finale that reflects the kind of city the player helped create. A strong playthrough can leave the city cleaner, healthier, and more hopeful. Poor decisions can leave projects unfinished, relationships damaged, or the city in a worse position. A mixed playthrough creates something in between, where progress has been made but the work is far from over.

The goal is for the ending to feel earned.

---

# Technology

The project is built primarily with **Ren'Py 8.5** and Python at **1920×1080**.

```text
Opening
   ↓
Trendy: Community & Garbage
   ↓
Spendy: Water & Practical Solutions
   ↓
River Cleanup Minigame
   ↓
Sparky: Progress & Optimism
   ↓
Stormy: Innovation & Responsibility
   ↓
Finale
```

Ren'Py handles the dialogue, choices, character states, UI, animations, and minigame.

A central decision system records important player choices and uses them to shape the final outcome of the story.

The finale can also generate a personalized continuation based on the player's decisions, with a built-in fallback ending if needed.

---

# How to Run

1. Install **Ren'Py 8.5**.
2. Download or clone this repository.
3. Open the Ren'Py Launcher.
4. Add or select the **In Otter Words** project folder.
5. Click **Launch Project**.

For the personalized finale, add your OpenRouter API key to `game/secrets.rpy` or set the `OPENROUTER_API_KEY` environment variable.

The rest of the game can still run with the built-in fallback ending if no API key is provided.

---

# Art and UI

The project includes more than **60 visual assets**, including character sprites, expressions, city environments, river scenes, wildlife, garbage, and interior locations.

The art direction is colourful and lighthearted on purpose.

We wanted to talk about serious environmental issues without making the experience feel heavy or discouraging. The characters and visual style make those ideas more approachable while still giving the player's decisions real weight.

---

# Built With

- **Ren'Py 8.5**
- **Python**
- **OpenRouter**
- **GLM-5.3-Flash**
- **PowerShell**
- **System.Drawing**

---

# Why We Built It

A lot of conversations about sustainability focus on how bad things are. We wanted to focus more on what happens next. What do you do when the river is polluted, when the best solution costs too much, or when people start to feel like change is pointless? **In Otter Words** turns those questions into a story where the player has to make those decisions for themselves.

We built this game because we wanted sustainability to feel more personal, interactive, and hopeful without pretending the problems are simple. Sometimes change takes technology, sometimes it takes money, and sometimes it takes getting people to care. Most of the time, it starts with something small.

**In Otter Words, every small change matters.**



