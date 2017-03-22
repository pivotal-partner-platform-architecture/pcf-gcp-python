#!/usr/bin/env python

from pcfgcp import PcfGcp
from google.cloud import language
import sys

def print_result(annotations):
  score = annotations.sentiment.score
  magnitude = annotations.sentiment.magnitude

  for index, sentence in enumerate(annotations.sentences):
    sentence_sentiment = sentence.sentiment.score
    print('Sentence {} has a sentiment score of {}'.format(index, sentence_sentiment))
    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return 0

    print('Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0

def analyze(client, text):
  document = client.document_from_text(text)
  annotations = document.annotate_text(include_sentiment=True,
                                       include_syntax=False,
                                       include_entities=False)
  # Print the results
  print_result(annotations)

pg = PcfGcp()
lang = pg.getLanguage()
analyze(lang, ' '.join(sys.argv[1:]))

