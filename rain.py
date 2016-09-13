'''
Use TextBlog spelling correction on the sentence 'the raain in sspain stayss mainly on the plane'
'''

# make the textblog package available
import textblob

# our phrase to correct
sentence = 'the raain in sspain stayss mainly on the plane'

# create an instance of TextBlog using our sentence

blog = textblob.TextBlob(sentence)

# correct the spelling errors
corrected = blog.correct()

print(corrected)

