# Chasing a Firefly in the Fog 🌫️

It's a foggy night and a **firefly** is drifting across your backyard. Every few seconds it *blinks*. You want to know where it *really* is — but the fog smears every blink, so each one looks a little off from the truth.

Here's the trick people use to follow it: **keep a best guess, then gently correct it with each new blurry blink.** You never fully believe any single blink (the fog lies a little), and you never ignore them either. You blend.

Grown-ups call this a **Kalman filter**. It's a fancy name for "smooth out wobbly clues to track something you can't see clearly."


```comic
{
  "title": "Following the Firefly",
  "panels": [
    {"emoji": "🌫️", "caption": "Foggy night. A firefly is drifting somewhere out there.", "bubble": "Where is it really?"},
    {"emoji": "✨", "caption": "It blinks — but the fog smears every blink a little off."},
    {"emoji": "🧠", "caption": "You keep ONE best guess of where the firefly truly is.", "bubble": "About... there."},
    {"emoji": "➡️", "caption": "Before the next blink, you guess where it will drift next.", "bubble": "Predict!"},
    {"emoji": "👀", "caption": "A new blink appears — a fresh, blurry clue."},
    {"emoji": "🎯", "caption": "You nudge your guess partway toward the blink.", "bubble": "Update!"},
    {"emoji": "🐛", "caption": "Repeat, and your smooth path hugs the firefly — even though every clue was fuzzy."}
  ]
}
```


## The two-step dance: predict, then peek

Watch what your brain does over and over:

1. **Predict.** "Last I saw, it was floating left and up. So next it's probably a little more left and up." You move your guess *before* the new blink even shows up.
2. **Update.** A blink appears. You slide your guess **partway** toward it — not all the way.

How far you slide is the whole secret. If the fog is thick and the blink looks wild, you barely move (trust your smooth guess). If the air clears and the blink is sharp, you move a lot (trust the clue). That "how much do I trust this new clue?" dial has a name: the **Kalman gain**.


```ascii
  blinks (blurry):   •   •      •   •     •   •
  your smooth path:  ────────────────────────────►
                     (wobbles are gone, the firefly is easy to follow)
```


## Why this is a superpower

A phone's **GPS dot** does the exact same thing. Raw GPS jumps around like a nervous bug, but your map shows a smooth dot gliding down the road — because it *predicts* where you're driving and only *nudges* toward each jittery reading.

Traders use the very same idea. A stock's price flickers up and down all day from tiny random bumps. Underneath the flicker there's a calmer "true" value drifting along. The filter keeps a best guess of that hidden value and gently corrects it tick by tick — turning a jumpy line into a smooth one you can actually plan around.

The big lesson: **you don't have to trust any single blurry clue. Keep a guess, predict, and correct a little at a time — and the fog stops fooling you.** 🐛✨
