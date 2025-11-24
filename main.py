import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as players_file:
        players = json.load(players_file)
    for player_name, data in players.items():

        race_name = data["race"]["name"]
        race_description = data["race"].get("description", "")
        race_skills = data["race"].get("skills", [])

        player_race, _ = Race.objects.get_or_create(
            name=race_name,
            description = race_description
        )

        for skill_data in race_skills:
            Skill.objects.get_or_create(
                name = skill_data["name"],
                race = player_race,
                bonus = skill_data["bonus"]
            )


        player_guild = None
        if data["guild"]:
            guild_name = data["guild"].get("name", "")
            guild_description = data["guild"].get("description", "")
            player_guild, _ = Guild.objects.get_or_create(
                name = guild_name,
                description = guild_description
            )

        Player.objects.get_or_create(
            nickname = player_name,
            email= data["email"],
            bio= data["bio"],
            race = player_race,
            guild = player_guild
                    )








if __name__ == "__main__":
    main()
