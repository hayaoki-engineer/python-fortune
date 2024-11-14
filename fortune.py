import random
from datetime import date

FORTUNE_OUTPUT_TEMPLATE = """
{today} の {name} さんの運勢は、

ラッキーカラー: {lucky_color}
ラッキーナンバー: {lucky_number}
"""

LUCKY_COLORS = ["red", "green", "blue"]
LUCKY_NUMBERS = [1, 2, 3]

def tell_fortune(name, birthday, today):
  lucky_color = random.choice(LUCKY_COLORS)
  lucky_number = random.choice(LUCKY_NUMBERS)

  return FORTUNE_OUTPUT_TEMPLATE.format(
    today=today,
    name=name,
    lucky_color=lucky_color,
    lucky_number=lucky_number
  )

def main():
  name = "Alice"
  birthday = date(2000, 1, 1)
  today = date.today()

  result = tell_fortune(name, birthday, today)
  print(result)

if __name__ == "__main__":
  main()