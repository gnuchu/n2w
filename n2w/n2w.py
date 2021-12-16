import logging

DEBUG_LEVEL = logging.INFO

class n2w:
  
  def __init__(self, n):
    self.number = n
    self.logger = logging.getLogger()
    self.logger.setLevel(level=DEBUG_LEVEL)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    self.logger.addHandler(handler)

  
  def get(self):
    self.logger.debug("In get()")
    return self.number

  def words(self):
    self.logger.debug("In words()")
    return self.__number_as_words().replace("  ", " ").rstrip()
  
  def __number_as_words(self):
    self.logger.debug("In __number_as_words()")
    data = self.__data()
    number_length = len(str(self.number))
    
    if number_length < 3:
      return self.__process_less_than_a_hundred(self.number)
        
    elif number_length == 3:
      return self.__process_three_digit_number(self.number)

    elif number_length > 3 or number_length < 7:
      start = str(self.number)[:-3]
      end = str(self.number)[-3:]

      first_part = ""
      joiner = ""
      last_part = ""

      if int(start) < 100:
        first_part = self.__process_less_than_a_hundred(start)
      else:
        first_part = self.__process_three_digit_number(start)


      if int(end) > 0 and int(end) < 100:
        joiner = ' ' + data['000'] + ' and ' 
      else:
        joiner = ' ' + data['000'] + ' '
      
      if int(end) > 0 and int(end) < 100:
          last_part = self.__process_less_than_a_hundred(end)
      elif int(end) > 99:
        last_part = self.__process_three_digit_number(end)

      return first_part + joiner + last_part
    
    else:
      return("Only numbers < 1_000_000 dealt with at the moment")

  def __process_less_than_a_hundred(self, n):
    self.logger.debug("__process_less_than_a_hundred()")
    data = self.__data()
    n = int(n)
    number_length = len(str(n))

    if number_length == 1:
      return data[str(n)]
    
    elif number_length == 2:
      if n < 21:
        return data[str(n)]
      else:
        return self.__process_tens(n)


  def __process_three_digit_number(self, n):
    h = str(n)[0]
    tu = str(n)[1:]

    if tu == '': 
      return tu
    
    hundreds = self.__process_hundreds(h)

    if int(tu) == 0:
      return hundreds
    else:
      return hundreds + ' and ' + self.__process_tens(tu)

  def __process_hundreds(self, x):
    data = self.__data()
    h = str(x)[0]
    return data[str(h)] + ' ' + data['00']


  def __process_tens(self, tu):
    data = self.__data()
    tu = int(tu)
    if tu < 21:
      return data[str(tu)]

    t = str(tu)[0]
    u = str(tu)[1]

    if t == '0':
      tens = ''
    else:
      tens = data[t + "0"]

    units = data[u]
    
    if u == "0":
      return tens
    else:
      return tens + ' ' + units

  def __data(self):
    return {
      "0": "zero",
      "1": "one",
      "2": "two",
      "3": "three",
      "4": "four",
      "5": "five",
      "6": "six",
      "7": "seven",
      "8": "eight",
      "9": "nine",
      "10": "ten",
      "11": "eleven",
      "12": "twelve",
      "13": "thirteen",
      "14": "fourteen",
      "15": "fifteen",
      "16": "sixteen",
      "17": "seventeen",
      "18": "eighteen",
      "19": "nineteen",
      "20": "twenty",
      "30": "thirty",
      "40": "fourty",
      "50": "fifty",
      "60": "sixty",
      "70": "seventy",
      "80": "eighty",
      "90": "ninety",
      "00" : "hundred",
      "000" : "thousand",
      "000000" : "million",
      "000000000" : "billion"
    }
