# Guess My Score 📚

Your whole class writes down two things: **how many hours each kid studied** and **the test score they got**. Now a new kid asks: *"I studied 5 hours — what score will I get?"*

You don't have a crystal ball. But you have a cloud of dots and a ruler. That's basically all that **regression** is — a fancy word for *drawing the line that best follows the dots so you can guess the next one.*


```comic
{
  "title": "Guess My Score",
  "panels": [
    {"emoji": "📚", "caption": "Everyone writes down: hours studied and the score they got.", "bubble": "Let's map it!"},
    {"emoji": "🔵", "caption": "You plot one dot per kid. More studying usually means a higher score.", "bubble": "Dots everywhere"},
    {"emoji": "📏", "caption": "You lay a ruler down and draw ONE straight line that hugs the cloud of dots.", "bubble": "Best fit!"},
    {"emoji": "🔮", "caption": "New kid studied 5 hours. Slide up the line — it predicts about 80.", "bubble": "80-ish!"},
    {"emoji": "🤏", "caption": "The BEST line is the one where the dots sit as close to it as possible.", "bubble": "Tiny gaps win"},
    {"emoji": "✅", "caption": "New question: will they PASS or FAIL? That's a yes/no, not a number.", "bubble": "Pass or fail?"},
    {"emoji": "〰️", "caption": "For yes/no you use an S-shaped line. It gives a chance, like '90% likely to pass'.", "bubble": "90% pass!"},
    {"emoji": "🧰", "caption": "Two tools: a straight line guesses a NUMBER, the S-line guesses YES or NO."}
  ]
}
```


## The straight line: guess a number

When you want to guess a **number** — a test score, how tall someone is, tomorrow's temperature — you draw a straight line through the dots. To pick the *best* line, you look at the little gap between each dot and the line, and you choose the line that makes all those gaps as small as possible.

Then predicting is easy: find 5 hours on the bottom, go straight up to the line, and read the score across. Done.


```ascii
 score
  100 |                 •      /  <- the best-fit line
      |            •      /
      |        •    /  •
      |     •  /  •
      |   /  •
      +--------------------------> hours studied
```


## The S-line: guess yes or no

Sometimes you don't want a number — you want a **yes or no**. *Will this kid pass?* A straight line is bad here, because it could say "score of 140" or "score of −20," which makes no sense as a yes/no.

So you switch to a special curve shaped like the letter **S**. It never goes below 0 or above 1, so its answer is always a **chance**: 0.90 means "90% likely to pass," 0.10 means "probably not." If the chance is over halfway (more than 0.5), you guess **yes**.

## Same idea, two shapes 🧰

Both tools do the exact same thing at heart: they take what you *know* (hours studied) and turn it into a good guess about what you *don't* know. Use the **straight line** when the answer is a number, and the **S-line** when the answer is yes-or-no. Grown-ups call them **linear regression** and **logistic regression** — but really, it's just the best line through a cloud of dots. 🔵📏
