hero_name = '鲁班七号'
hero_speed = 450
hero_hp = 3000
hero_atk = 100

# hero attribute


# player info


user_name = '张大仙'
user_gender = 'female'
user_team = 'XYG'
user_dan = '王者荣耀'


def get_user_info():
    print(f'玩家的属性：名字：{user_name} 性别：{user_gender}'
          f'战队：{user_team} 段位{user_dan}')


def set_user_name(name):
    global user_name
    user_name = name


class Hero:
    hero_work = '射手'
    count = 0

    def __init__(self, name, speed, hp, atk):
        self.name = name
        self.speed = speed
        self.hp = hp
        self.atk = atk
        self.equipment = []
        Hero.count += 1

    def get_hero_info(self):
        print(f'英雄的属性：名字：{hero_name} 移速：{hero_speed}'
              f'生命值：{hero_hp} 攻击力：{hero_atk}')

    def set_hero_speed(self, speed_plus):
        global hero_speed
        hero_speed += speed_plus

    def buy_equipment(self, e_name):
        self.equipment.append(e_name)


# 属性访问

hero1_obj = Hero('鲁班七号', 450, 3000, 100)
hero2_obj = Hero('后羿', 460, 3100, 110)
hero3_obj = Hero('虞姬', 470, 3200, 120)
hero3_obj.hero_work = '法师'


hero1_obj.buy_equipment('反甲')
hero2_obj.buy_equipment('复活甲')
hero3_obj.buy_equipment('末世')

print(hero1_obj.equipment)
print(hero2_obj.equipment)
print(hero3_obj.equipment)

