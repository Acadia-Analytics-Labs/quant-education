# How Sure Are You? 🎲

Some things you *know* for sure. The sun will come up tomorrow. Other things you're *not* sure about at all. Will it rain? Will you win the game? **Probability** is just a way to put a number on **how sure you are.**

The number always lives between **0 and 1**:

- **0** = "no way, impossible." 🚫
- **1** = "for sure, definitely." ✅
- **0.5** = "eh, could go either way." 🤷

A weather app that says "70% chance of rain" is really saying **0.7** — pretty sure, but not certain. Bring an umbrella!

```comic
{
  "title": "Two Ways to Guess a Coin",
  "panels": [
    {"emoji": "🪙", "caption": "You're about to flip a coin. Heads or tails?", "bubble": "Hmm..."},
    {"emoji": "🤔", "caption": "Before flipping, you guess: 'I feel 50% sure it's heads.'", "bubble": "0.5!"},
    {"emoji": "💭", "caption": "That's a BELIEF — a number for how sure you feel right now."},
    {"emoji": "🔁", "caption": "Your friend does it differently: she flips it 1000 times.", "bubble": "Again!"},
    {"emoji": "✏️", "caption": "She counts: 503 heads, 497 tails. About half heads!"},
    {"emoji": "📊", "caption": "That's a FREQUENCY — measured by actually doing it a zillion times."},
    {"emoji": "🧠", "caption": "Both got 0.5. Two paths to the same 'how sure' number!"}
  ]
}
```

## The two thinking styles

**The believer (Bayesian).** You guess *before* anything happens, using what you already know. Peeking at a wrapped gift and thinking "I'm 80% sure it's the video game I asked for" — that's a belief. If you shake the box and hear a rattle, you *update* your guess. New clues change how sure you feel.

**The counter (Frequentist).** You don't guess feelings — you *repeat the experiment* a huge number of times and count. Flip the coin 1000 times, and the fraction that came up heads *is* your probability. One unlucky tails doesn't change anything; it's just one flip out of many.

```ascii
  0 ----------- 0.5 ----------- 1
  never        maybe         for sure
   🚫            🤷            ✅
```

## Why have two?

Some things you can repeat over and over, like coin flips — the counter's style works great. But some things happen only *once*, like "will it snow on my birthday this year?" You can't repeat that a thousand times, so you use a **belief** instead.

Smart people use **both**. Probability is just a number from 0 to 1 that says how sure you are — and there's more than one good way to find it. 🎯
