import re
import sys
import json
from .chatParser import WhatsAppChatParser
from .slideGenerator import SlideGenerator 

def ConvertTextFileToPPT( inputfile , outputfile ):
    chatparser = WhatsAppChatParser(inputfile)
    generator = SlideGenerator(outputfile)
    
    while True:
        try:
           generator.addSlide(chatparser.getNextQuote())
        except:
           break
    generator.save()  
