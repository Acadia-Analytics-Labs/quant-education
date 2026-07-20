# The Case of the Mystery Bag 🔍

A friend hands you one of **two bags** and won't tell you which. Both are full of marbles:

- 🟢 **Green Bag:** mostly green marbles (and a few red).
- 🔴 **Red Bag:** half green, half red.

You can't peek inside. But you *can* reach in and pull one marble at a time. Every marble you pull is a **clue** — and a good detective changes their guess as clues arrive.

```comic
{
  "title": "Which Bag Do I Have?",
  "panels": [
    {"emoji": "🎒", "caption": "Two bags. One is mostly green, one is half-and-half. You get one but don't know which.", "bubble": "Hmm..."},
    {"emoji": "🤷", "caption": "With no clues yet, it's a totally even guess: 50/50.", "bubble": "Could be either!"},
    {"emoji": "🟢", "caption": "You reach in and pull a GREEN marble.", "bubble": "A clue!"},
    {"emoji": "🕵️", "caption": "Green marbles are more common in the Green Bag. So green makes THAT bag more likely.", "bubble": "Leaning green..."},
    {"emoji": "🟢", "caption": "You pull another green marble. Two greens in a row!", "bubble": "Whoa."},
    {"emoji": "📈", "caption": "Now you're really sure — probably the Green Bag. The clues stacked up.", "bubble": "Pretty confident!"},
    {"emoji": "🔴", "caption": "But watch: one red marble would nudge your guess back the other way.", "bubble": "Stay open!"},
    {"emoji": "💡", "caption": "Big idea: new information changes the odds. Update every time a clue lands.", "bubble": "That's the trick!"}
  ]
}
```

## The one-sentence idea

> **When you learn something new, your best guess should change.**

Before you pull any marble, both bags are equally likely — a plain **50/50**. That first guess is called your **prior** (your "before" belief).

Then a clue arrives. A green marble is *more likely* to come from the bag with more green in it. So pulling green makes that bag a better bet. Your new, smarter guess is called the **posterior** (your "after" belief). Pull another green? Update again. Pull a red? Update the other way.

## Why this matters

This is exactly how a good detective thinks. They don't lock in one suspect and ignore the clues — they start with an open mind and let each new fact tip the scales. 🔍

Grown-ups have a famous rule for doing this with numbers. It's called **Bayes' theorem**, and it's really just a careful recipe for the same thing you did with the marbles:

**start with a guess → see a clue → update → repeat.** 🟢➡️📈
