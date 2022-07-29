from abc import ABC, abstractmethod


# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
#         self.stats = {
#             "HP": 128,  # health points
#             "MP": 42,  # magic points,
#             "SP": 100,  # skill points
#             "Strength": 15,  # сила
#             "Perception": 4,  # восприятие
#             "Endurance": 8,  # выносливость
#             "Charisma": 2,  # харизма
#             "Intelligence": 3,  # интеллект
#             "Agility": 8,  # ловкость
#             "Luck": 1  # удача
#         }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def get_positive_effects(self):
        return self.obj.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.obj.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        return self.obj.get_stats()


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.obj.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.obj.get_positive_effects()


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        return self.obj.get_positive_effects() + ['Berserk']

    def get_stats(self):
        stats = self.obj.get_stats()
        for x in "Strength", "Endurance", "Agility", "Luck":
            stats[x] += 7
        for x in "Perception", "Charisma", "Intelligence":
            stats[x] -= 3
        stats["HP"] += 50
        return stats


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        return self.obj.get_positive_effects() + ['Blessing']

    def get_stats(self):
        stats = self.obj.get_stats()
        for x in "Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck":
            stats[x] += 2
        return stats


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        return self.obj.get_negative_effects() + ['Weakness']

    def get_stats(self):
        stats = self.obj.get_stats()
        for x in "Strength", "Endurance", "Agility":
            stats[x] -= 4
        return stats


class Curse(AbstractNegative):
    def get_negative_effects(self):
        return self.obj.get_negative_effects() + ['Curse']

    def get_stats(self):
        stats = self.obj.get_stats()
        for x in "Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck":
            stats[x] -= 2
        return stats


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        return self.obj.get_negative_effects() + ['EvilEye']

    def get_stats(self):
        stats = self.obj.get_stats()
        stats["Luck"] -= 10
        return stats


# # создаем героя
# hero = Hero()
# hero.get_stats()
# # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
# print(hero.stats)
# # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
# print(hero.get_negative_effects())
# # []
# print(hero.get_positive_effects())
# # []
#
# # накладываем эффект
# brs1 = Berserk(hero)
# print(brs1.get_stats())
# # {'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 22, 'Perception': 1, 'Endurance': 15, 'Charisma': -1, 'Intelligence': 0, 'Agility': 15, 'Luck': 8}
# print(brs1.get_negative_effects())
# # [ ]
# print(brs1.get_positive_effects())
# # ['Berserk']
#
# # накладываем эффекты
# brs2 = Berserk(brs1)
# cur1 = Curse(brs2)
# print(cur1.get_stats())
# # {'HP': 228, 'MP': 42, 'SP': 100, 'Strength': 27, 'Perception': -4, 'Endurance': 20, 'Charisma': -6, 'Intelligence': -5, 'Agility': 20, 'Luck': 13}
# print(cur1.get_positive_effects())
# # ['Berserk', 'Berserk']
# print(cur1.get_negative_effects())
# # ['Curse']
# # снимаем эффект Berserk
# cur1.base = brs1
# print(cur1.get_stats())
# # {'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 20, 'Perception': -1, 'Endurance': 13, 'Charisma': -3, 'Intelligence': -2, 'Agility': 13, 'Luck': 6}
# print(cur1.get_positive_effects())
# # ['Berserk']
# print(cur1.get_negative_effects())
# # ['Curse']
