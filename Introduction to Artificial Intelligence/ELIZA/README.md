### ELIZA in Python

This is a little version of ELIZA, a famous natural-language AI demo from the 1960s,
packaged up as a Python module.  It's all smoke and mirrors; the program doesn't
have a clue what it is saying and it's not difficult to catch it out, but it's amusing
and it means your chatbot always has something to say.

The eliza.py module includes an interactive mode, so you can get a feel for how it performs. Just grab the code
and `python eliza.py`.  To use the it from with in your own script do something like

``` python
import eliza

therapist = eliza.eliza()
while some_condition:
  #get input from somewhere
  reply = therapist.respond(input)
  #send reply somewhere
```
## Chatbot ELIZA's conversational approach
EIZA acts as a therapist. Not just any therapist, though: a Rogerian psychotherapist.

This is key information in this case because Rogerian psychotherapy employs a unique approach called 'person-centered'. A Rogerian psychotherapist's process is to interact with the patient with complete empathy and lack of judgement.

To do this, the psychotherapist asks person-centric questions to the patient. For instance, if a patient were to say 'I feel depressed', a Rogerian psychotherapist would try to dig further by asking 'Why do you feel down?'.

This type of therapy is a back and forth of statements from the patient and questions from the therapist. The goal is to uncover realisations by digging deeper and deeper.

Ok, this concludes our lesson on psychotherapy. Why does all of this matter?

It matters because it dictates how ELIZA actually interacts with its users. It allows ELIZA to respond to input with accuracy without ever having to really understand what the user says.

## How does ELIZA actually work

The DOCTOR script that powers ELIZA is relatively simple. It assigns a value to each word of a sentence a user inputs and uses the value to reorder the words in the form of a question. The value of the word is determined by its importance within the sentence (which is where the smart stuff happens).

Let's take an example. Taking the sentence 'I want to run away from my parents'.

ELIZA attributes low values to pronouns (I), slightly higher values to action verbs (want to), and the highest value to the actual action (run away from my parents). This allows the programme to know exactly how to flip the sentence around to ask a digging question.
for more information check [here](https://blog.ubisend.com/discover-chatbots/chatbot-eliza)


## References
J. Weizenbaum, [ELIZA - A Computer Program For the Study of Natural Language Communication Between Man And Machine](http://www.cse.buffalo.edu/~rapaport/572/S02/weizenbaum.eliza.1966.pdf) _Communications of the ACM, Vol 9, No 1, January 1966_

## License

Original code written by Joe Strout, with some updates by Jeff Epler.  Converted to a module and updated for Python 3 by Jez Higgins.

Copyright (c) 2002-2017 [JezUK Ltd](http://www.jezuk.co.uk), Joe Strout, Jeff Epler

Licensed under the terms of the MIT License.
