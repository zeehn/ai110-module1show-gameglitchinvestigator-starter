# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  After installing dependencies, the game ran without any errors. When I started playing in 'Normal Difficulty (range 1-100)' with 'Developer Debug Info' open and gave a guess lower than the secret. It kept asking me to go lower which was incorrect. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The first bug I noticed immediately was the range for hard was lower (1-50) than range for normal which was (1-100). I figured it should be other way around as range for easy is (1-20).
  2. Second bug I noticed was in the game logic. The game incorrectly directs you towards wrong direction. When secret is 25 and you gave a guess as 20, it asks to go lower. 
  3. New Game button does not work.
  4. The range for easy is 1-20 but the secret was 45.
  5. The list of attempts history in debug info does not insert the last attempt. Game is over before the last attempt is appended. 
  6. Attempts allowed for easy are 6 and normal are 8. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used CodePilot in VSCode.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Suggested me to add .venv to .gitignore file.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Suggested me that it can generate .gitignore file, although the file already exists.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I tested by running the app, also did a dry run to see how code has changed. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the test where it checks for ranges assigned to difficuly levels of the game.
- Did AI help you design or understand any tests? How?
  AI just suggested to implement the tests, I collaborated with it in implementing the tests for specific functions.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  Streamlit reruns the entire script on every widget interaction, that's why on each rerun it produced a new number.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit has short-term memory loss problem. It forgets the data on each rerun. That's why we have to keep it a place where it should check if it has data before producing new one. That place is state.
- What change did you make that finally gave the game a stable secret number?
  By storing secret in st.session_state and initializing only if the secret is not present. Removed any code logic that regenerated the secret. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    That making changes in small chunks make it easier to think about code and also learn from the changes. Just asking AI to fix it gets you lost and I don't enjoy working when I don't understand what is happening.
- What is one thing you would do differently next time you work with AI on a coding task?
  That I first understand the code by painting a bigger picture using ASK mode. And then moving step by step, fixing bugs and commiting them. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  It got me familiar with working with AI. Helped me remove many assumptions I had about AI.

---

