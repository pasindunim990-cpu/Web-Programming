"""Run from `python manage.py shell` with: from teams.load_sample_data import load; load()"""
from .models import Player, Position

POSITIONS = [
    ("Tight Head Prop", True), ("Hooker", True), ("Loose Head Prop", True),
    ("Second Row", True), ("Open Side Flanker", False),
    ("Blind Side Flanker", False), ("Number 8", False),
    ("Scrum Half", False), ("Fly Half", False), ("Inside Centre", False),
    ("Outside Centre", False), ("Left Wing", False), ("Right Wing", False),
    ("Full Back", False),
]


def load():
    position_objects = {}
    for name, specialist in POSITIONS:
        position, _ = Position.objects.update_or_create(
            name=name, defaults={"specialist": specialist}
        )
        position_objects[name] = position

    examples = [
        ("Kamal", "Perera", "Colombo RFC", 21, ["Scrum Half"], []),
        ("Nimal", "Fernando", "Kandy RFC", 22, ["Tight Head Prop"], ["Tight Head Prop"]),
        ("Sahan", "Silva", "Galle RFC", 20, ["Fly Half", "Full Back"], []),
        ("Ruwan", "Jayasinghe", "Colombo RFC", 23, ["Hooker"], ["Hooker"]),
    ]
    for first, last, team, age, roles, approved in examples:
        player, _ = Player.objects.get_or_create(
            first_name=first, last_name=last, team=team,
            defaults={"age": age},
        )
        player.age = age
        player.save()
        player.positions.set([position_objects[name] for name in roles])
        player.approved_specialist_positions.set([position_objects[name] for name in approved])
    print("Rugby positions and sample players loaded.")
