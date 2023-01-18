import datetime

from django.conf import settings
from django.db.models import F
from django.db import models
from django.utils import timezone


class League(models.Model):
    league_name = models.CharField(max_length=200)

    def __str__(self):
        return self.league_name


class Player(models.Model):
    name = models.CharField('Ник игрока', max_length=50, unique=True)
    in_club = models.BooleanField('Резидент', default=False)

    # Game.objects.filter(players__contain = F('Player__name'))
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Game(models.Model):
    league = models.ForeignKey(League, null=True, on_delete=models.SET_NULL)
    game_date = models.DateField('Game date', default=timezone.now)
    players = models.ManyToManyField(Player)

    class Meta:
        ordering = ['game_date']

    def __str__(self):
        return f'Game {self.game_date}'

months = {
    '1': 'Январь',
    '2': 'Февраль',
    '3': 'Март',
    '4': 'Апрель',
    '5': 'Май',
    '6': 'Июнь',
    '7': 'Июль',
    '8': 'Август',
    '9': 'Сентябрь',
    '10': 'Октябрь',
    '11': 'Ноябрь',
    '12': 'Декабрь'
}

class Payment(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)
    payment_date = models.DateField('Дата платежа', default=timezone.now)

    class Meta:
        ordering = ['payment_date']

    def __str__(self):
        return f'{Player.objects.get(name=self.player_id)} - {months[str(self.payment_date.month)]}'
