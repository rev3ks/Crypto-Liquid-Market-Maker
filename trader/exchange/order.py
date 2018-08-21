from . import trading
import time
import logging


logging.basicConfig(filename='info.log', level=logging.INFO)


class Order():

  def __init__(self, pair, side, size, price, test=False):
    self.pair = pair
    self.side = side
    self.size = size
    self.price = price
    self.status = "created"
    self.id = ""
    self.history = []
    self.responses = []
    self.test = test
    self.post_only = True

    self.update_history("Created")

  @property
  def pair(self):
    return self._pair

  @pair.setter
  def pair(self, value):
    if value not in ["BTC-USD", "ETH-USD", "LTC-USD", "BCH-USD", "ETH-BTC",
                     "LTC-USD", "BCH-USD"]:
      raise ValueError("%s is an invalid trading pair." % value)

    self._pair = value

  @property
  def side(self):
    return self._side

  @side.setter
  def side(self, value):
    if value not in ["buy", "sell"]:
      raise ValueError("side must be 'buy' or 'sell'.")

    self._side = value

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self, value):
    if type(value) not in [float, int]:
      raise TypeError("{} is not a number.".format(value))

    self._size = value

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    if type(value) not in [float, int]:
      raise TypeError("{} is not a number".format(value))

    self._price = value

  def __str__(self):
    return "pair: {}, side: {}, size: {}, price: {}".format(
      self.pair,
      self.side,
      self.size,
      self.price)

  def update_history(self, message):
    self.history.append(
      {"time": time.time(), "status": message}
    )

  def allow_market_trade(self):
    self.post_only = False

  def send_order(self):
    trading.send_order(self)

  def cancel_placed_order(self):
    trading.cancel_order(self)