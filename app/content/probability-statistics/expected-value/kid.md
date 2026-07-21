# The Carnival Spinner 🎡

You're at the fair with a pocket of tokens. A spinner game costs **1 token** to play. Sometimes you win a little, and once in a while you win a lot. The big question isn't *"will I win this spin?"* — nobody knows that. The smart question is: **"if I played this forever, how many tokens would I win on average each spin?"**

That average has a grown-up name: **expected value**. And there's a simple trick to find it.


```comic
{
  "title": "The Carnival Spinner",
  "panels": [
    {"emoji": "🎡", "caption": "A spinner game at the fair. It costs 1 token to play.", "bubble": "Round and round!"},
    {"emoji": "🟢", "caption": "Most of the wheel is green: 9 out of 10 spins win you 1 token."},
    {"emoji": "🌟", "caption": "A thin gold slice: 1 out of 10 spins wins a jackpot of 10 tokens!", "bubble": "Jackpot?"},
    {"emoji": "🤔", "caption": "Is it worth a token? Don't guess — find the AVERAGE win per spin."},
    {"emoji": "✖️", "caption": "The trick: multiply each prize by its chance, then add them all up."},
    {"emoji": "➕", "caption": "(9/10 × 1) + (1/10 × 10) = 0.9 + 1.0 = 1.9 tokens per spin."},
    {"emoji": "🔁", "caption": "Any ONE spin is luck. Over hundreds of spins, 1.9 shows up.", "bubble": "Keep going!"},
    {"emoji": "⭐", "caption": "Pay 1, get 1.9 back on average. That average is the EXPECTED VALUE."}
  ]
}
```


## The one trick, in one sentence

> **Expected value = add up (each prize × its chance).**

That's the whole idea. You don't add the prizes by themselves — you give a *big* prize a *small* weight if it's rare, and a *small* prize a *big* weight if it happens a lot. Then you total everything up.

For our spinner: the small 1-token win happens a lot (9 times out of 10), and the giant 10-token win is rare (1 time out of 10). Weigh each one by how often it happens and you get **1.9 tokens per spin, on average.** Since a spin only costs 1 token, you come out ahead — this is a *good* game to keep playing.

## Why "forever" matters

Here's the sneaky part: on any single spin you'll usually just win 1 token, and sometimes 10. You almost never win exactly 1.9 — that number is an *average*, not a promise.


```ascii
  spins:   1 tok, 1 tok, 10 tok, 1 tok, 1 tok, 1 tok, 10 tok ...
  average settles toward:  ~1.9 tokens per spin
  (the more you spin, the closer the average gets)
```


One spin is a coin toss — pure luck. But the more you play, the more the luck cancels out and the true average shows up. That's why a good spinner (average win bigger than the cost) slowly stacks up tokens if you keep playing, and a bad one slowly empties your pocket no matter how exciting a jackpot feels. 🎡⭐

So next time you see a game, don't ask "can I win?" Ask "what's the average?" Multiply each prize by its chance, add it up, and compare it to what the game costs. That little sum is the difference between a game worth playing and one that just *looks* fun.
