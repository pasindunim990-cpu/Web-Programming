from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=60, unique=True)
    specialist = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        label = " (specialist)" if self.specialist else ""
        return f"{self.name}{label}"


class Player(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    team = models.CharField(max_length=80)
    age = models.PositiveSmallIntegerField()
    positions = models.ManyToManyField(Position, related_name="players", blank=True)
    # Only positions listed here can be selected if they are specialist positions.
    approved_specialist_positions = models.ManyToManyField(
        Position, related_name="approved_players", blank=True,
        help_text="Specialist positions for which this player has been approved."
    )

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.team}"

    def can_play_position(self, position):
        if not self.positions.filter(pk=position.pk).exists():
            return False
        if position.specialist:
            return self.approved_specialist_positions.filter(pk=position.pk).exists()
        return True
