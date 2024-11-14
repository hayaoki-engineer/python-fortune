import random
from datetime import date

FORTUNE_OUTPUT_TEMPLATE = """
{today} の {name} さんの運勢は、

ラッキーカラー: {lucky_color}
ラッキーナンバー: {lucky_number}
"""

LUCKY_COLORS = ["red", "green", "blue"]
LUCKY_NUMBERS = [1, 2, 3]

class UserProfile:
  def __init__(self, name, birthday):
    self.name = name
    self.birthday = birthday


def tell_fortune(user_profile, today):
  lucky_color = random.choice(LUCKY_COLORS)
  lucky_number = random.choice(LUCKY_NUMBERS)

  return FORTUNE_OUTPUT_TEMPLATE.format(
    today=today,
    name=user_profile.name,
    lucky_color=lucky_color,
    lucky_number=lucky_number
  )

def main():
  name = "Alice"
  birthday = date(2000, 1, 1)
  user_profile = UserProfile(name, birthday)
  print(user_profile.name)
  print(user_profile.birthday)
  today = date.today()

  result = tell_fortune(user_profile, today)
  print(result)

if __name__ == "__main__":
  main()