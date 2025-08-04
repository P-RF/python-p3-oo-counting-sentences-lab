#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    """Gets the string value"""
    return self._value

  @value.setter
  def value(self, new_value):
    """Sets the string value if it is a string"""
    if not isinstance(new_value, str):
      print('The value must be a string.')
    self._value = new_value

  def is_sentence(self):
    """Returns True if value ends with a period and False otherwise"""
    return self.value.endswith('.')

  def is_question(self):
    """Returns True if value ends with a question mark and False otherwise"""
    return self.value.endswith('?')

  def is_exclamation(self):
    """Returns True if value ends with an exclamation mark and False otherwise"""
    return self.value.endswith('!')

  def count_sentences(self):
    replace_punctuation = self.value.replace('?', '.').replace('!', '.')
    separate_string = replace_punctuation.split('.')
    filter_string = [part.strip() for part in separate_string if part.strip() != '']
    return len(filter_string)