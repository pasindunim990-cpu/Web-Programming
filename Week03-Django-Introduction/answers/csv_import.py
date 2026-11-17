"""Example CSV importer. Run from manage.py shell: from teams.csv_import import run; run()"""
import csv
from pathlib import Path
from .models import Player, Position


def run():
    csv_path = Path(__file__).with_name("players.csv")
    with csv_path.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            player, _ = Player.objects.update_or_create(
                first_name=row["first_name"], last_name=row["last_name"],
                team=row["team"], defaults={"age": int(row["age"])}
            )
            roles = [name.strip() for name in row["positions"].split("|") if name.strip()]
            approved = [name.strip() for name in row["approved_specialist_positions"].split("|") if name.strip()]
            player.positions.set(Position.objects.filter(name__in=roles))
            player.approved_specialist_positions.set(Position.objects.filter(name__in=approved))
    print("CSV import complete")
