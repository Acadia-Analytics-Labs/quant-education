# A Team of Tiny Switch-Flippers 🔦

Imagine a giant relay race where the runners don't carry a baton — they carry **notes**. A photo comes in one end, gets passed from row to row of tiny helpers, and by the time it reaches the other end, the team shouts the answer: **"It's a cat!"**

That relay team is a **neural network**. Each little helper is a **neuron**: a switch-flipper that looks at the notes it gets, decides how excited to be, and passes its own note forward. No single helper knows what a cat is. But *together*, row by row, they figure it out.


```comic
{
  "title": "The Note-Passing Team That Learned to See a Cat",
  "panels": [
    {"emoji": "🖼️", "caption": "A picture comes in. To the team it's just a pile of tiny dots.", "bubble": "New picture!"},
    {"emoji": "🔦", "caption": "The first row of switch-flippers each hunt for ONE tiny thing — a line, a dot, an edge."},
    {"emoji": "📝", "caption": "Each one scribbles a note: 'I see a slanted line!' and passes it forward.", "bubble": "Note passed!"},
    {"emoji": "🧩", "caption": "The next row reads many notes and combines them: 'pointy ear? round eye? whiskers?'"},
    {"emoji": "🐱", "caption": "The last flipper adds it all up and makes the call.", "bubble": "It's a CAT!"},
    {"emoji": "❌", "caption": "At first the team is terrible — it yells 'DOG!' at a cat. A coach says how wrong it was."},
    {"emoji": "🔧", "caption": "So the team turns little knobs: listen MORE to helpful notes, LESS to useless ones.", "bubble": "Tweak, tweak"},
    {"emoji": "🏆", "caption": "After thousands of practice pictures, the knobs are just right. Now it nails it!"}
  ]
}
```


## How does the team get smart?

Nobody *tells* the helpers what a cat is. They **practice**. Every time the team guesses, a coach shows the right answer and says how far off they were. Then every helper nudges its **knobs** — grown-ups call these **weights** — a tiny bit, so next time it leans a little closer to right.

- 🔊 A **loud** knob means "this note matters a lot."
- 🔇 A **quiet** knob means "ignore this one."
- 🔁 Do this thousands of times and the whole team slowly gets brilliant.

## The two ways it can mess up

- 😴 **Too lazy (underfitting):** the team barely tries and guesses "cat" for everything, even a bus. Not enough helpers, or not enough practice.
- 🤯 **Too obsessed (overfitting):** the team memorizes the *exact* practice photos — even a smudge on one picture — so it's perfect on those but clueless on a brand-new cat. The trick is to learn the *idea* of a cat, not the smudges.

## What's this got to do with money?

Traders use these note-passing teams too. Instead of dots in a photo, the inputs are numbers about a stock — how much it moved, how jumpy it's been, how many people are buying. The team passes notes and guesses "up" or "down." Same relay race, different notes. And the same rule holds: a team that just memorizes the past is useless tomorrow. 🐱📈
