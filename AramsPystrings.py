#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#   PyStrings.py will identify specific elements of a given text
#                                                
#     Created by Aram Duronslet-Asman, 2025-05-09
#         Last edit: 2025-05-13
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Here is my chosen text, an AI printed impression of Samuel Jackson...because
text = """You wanna know what’s wrong with the world? Sit down. Shut up. Let me tell you something.
People got too damn comfortable being fake. That’s right—I said it. Smiling in your face, stabbing you in the back with the same hand they just used to pat your shoulder. Mmm-hmm. Everybody's trying to impress everybody else, like they’re in some kind of Instagram Olympics for the fakest damn life. Filters don’t fix your soul, baby. You can Photoshop your face all you want, but you can't airbrush integrity.
I come from a time when your word meant something. When a handshake was a contract, not just a photo op. When respect had to be earned—not begged for with hashtags and TikToks. You feel me?
Now everybody’s offended by everything. You say good morning the wrong way, and someone’s writing a 12-tweet thread about your “toxic positivity.” Are you kidding me? What happened to just dealing with stuff? What happened to grit? Resilience? Let me tell you—life doesn’t give a damn about your feelings. It’ll hit you in the mouth whether you’re ready or not.
But that’s the thing—life ain’t supposed to be easy. You want easy? Go take a nap. Life is supposed to challenge you, sharpen you, break you down and build you back up. That’s how you grow. That’s how you become something. A diamond ain’t born shining—it’s pressure, heat, and time. Same with people.
And don’t get me started on excuses. “I can’t.” “I’m tired.” “It’s too hard.” Shut up. You think your ancestors crossed oceans, fought wars, marched through fire for you to sit there and quit 'cause it’s hard? Nah. Hell no. They endured so you could rise. And you sitting here whining about Wi-Fi speed?
Let me tell you what real strength looks like—it’s showing up. Every day. When you don’t feel like it. When the world’s heavy and your legs are shaking. When nobody’s watching, and still, you give your best. That’s strength. That’s what separates the real ones from the wannabes.
You wanna be great? Then act like it. Speak the truth. Walk tall. Own your mistakes. Lift people up without losing your fire. And never, ever let fear write your story. Fear is a punk—it only wins if you let it.
So here’s what I need you to do: stop waiting. Stop doubting. And for God’s sake, stop pretending. You don’t need permission to be powerful. You already are. You were born with everything you need. Now go out there and use it.
And if anybody’s got a problem with that? You tell ‘em Samuel L. Jackson said sit your ass down and listen."""

import re

e_count = text.count('e')
print(f"The letter 'e' appears in the text {e_count} times.")
# finds the number of e's found and prints the count

b_count = text.count('b')
print(f"The letter 'b' appears in the text {b_count} times.")
# same as the last part but for the b's

words = text.split()
word_count = len(words)
print(f"\n\nTotal words: {word_count}")
# gets the word count for the given text, which is a bit under 500 at 442

sentences = re.split(r'[.!?]', text)
sentences = [s.strip() for s in sentences if s.strip()]
sentence_count = len(sentences)
print(f"\nTotal sentences: {sentence_count}")
# counts how many sentences in the given text

shortest_sentence = min(sentences, key=len)
print(f"\nThe shortest sentence is: \n{shortest_sentence}")
# finds the shortest sentence in the given text

text = text.lower()
punctuation = ".?!,;:\"'()[]{}"
for char in punctuation:
    text = text.replace(char, "")
    unique_words = set(words)
print(f"\nThere are {len(unique_words)} unique words")
# gives the number of unique words in the text

# Step 9: Capitalize every h in the text
text = text.replace('h', 'H')
words = text.split()
H_words = [word for word in words if 'H' in word]
hWord_count = text.count('H')
print(', '.join(H_words))
# this part capitalizes every h in the text
