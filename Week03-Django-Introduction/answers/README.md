# Week 03 answer - Rugby teams and positions

This implements the explicit ToDo at the end of the tutorial. Create a Django project named `rugbyproject` and an app named `teams`, add `teams` to `INSTALLED_APPS`, then copy the Python files from this folder into the matching app files. Run `python manage.py makemigrations`, `python manage.py migrate`, and `python manage.py createsuperuser`; then run the server and visit `/admin/`.

Install the packages with `pip install -r requirements.txt`. The model uses a many-to-many relationship because a player can play multiple positions and a position can be associated with multiple players. The `specialist` flag identifies restricted positions; `can_play_position` only permits a player who has been approved for that specialist position. Sample data can be loaded with `python manage.py shell` then `from teams.load_sample_data import load; load()`.
