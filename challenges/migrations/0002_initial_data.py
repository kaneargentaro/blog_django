from django.db import migrations


def create_initial_data(apps, schema_editor):
    Challenge = apps.get_model('challenges', 'Challenge')
    Month = apps.get_model('challenges', 'Month')
    ChallengeMonth = apps.get_model('challenges', 'ChallengeMonth')

    # Create months
    months_data = [
        {'name': 'january', 'code': 1},
        {'name': 'february', 'code': 2},
        {'name': 'march', 'code': 3},
        {'name': 'april', 'code': 4},
        {'name': 'may', 'code': 5},
        {'name': 'june', 'code': 6},
        {'name': 'july', 'code': 7},
        {'name': 'august', 'code': 8},
        {'name': 'september', 'code': 9},
        {'name': 'october', 'code': 10},
        {'name': 'november', 'code': 11},
        {'name': 'december', 'code': 12},
    ]

    month_objects = {}
    for month_data in months_data:
        month = Month.objects.create(**month_data)
        month_objects[month_data['name']] = month

    # Create challenges
    challenges_data = [
        {'name': 'Walk for 20 minutes', 'description': 'Walk for 20 minutes every day'},
        {'name': 'Walk for 30 minutes', 'description': 'Walk for 30 minutes every day'},
        {'name': 'Walk for 40 minutes', 'description': 'Walk for 40 minutes every day'},
        {'name': 'Walk for 50 minutes', 'description': 'Walk for 50 minutes every day'},
        {'name': 'Walk for 60 minutes', 'description': 'Walk for 60 minutes every day'},
        {'name': 'Walk for 70 minutes', 'description': 'Walk for 70 minutes every day'},
        {'name': 'Walk for 80 minutes', 'description': 'Walk for 80 minutes every day'},
        {'name': 'Walk for 90 minutes', 'description': 'Walk for 90 minutes every day'},
        {'name': 'Walk for 100 minutes', 'description': 'Walk for 100 minutes every day'},
        {'name': 'Walk for 110 minutes', 'description': 'Walk for 110 minutes every day'},
        {'name': 'Walk for 120 minutes', 'description': 'Walk for 120 minutes every day'},
    ]

    # Map challenges to months
    month_challenge_mapping = {
        'january': 'Walk for 20 minutes',
        'february': 'Walk for 30 minutes',
        'march': 'Walk for 40 minutes',
        'april': 'Walk for 50 minutes',
        'may': 'Walk for 60 minutes',
        'june': 'Walk for 70 minutes',
        'july': 'Walk for 80 minutes',
        'august': 'Walk for 90 minutes',
        'september': 'Walk for 100 minutes',
        'october': 'Walk for 110 minutes',
        'november': 'Walk for 120 minutes',
        # December has no challenge (None in original dict)
    }

    challenge_objects = {}
    for challenge_data in challenges_data:
        challenge = Challenge.objects.create(**challenge_data)
        challenge_objects[challenge_data['name']] = challenge

    # Create ChallengeMonth relationships
    for month_name, challenge_name in month_challenge_mapping.items():
        ChallengeMonth.objects.create(
            month=month_objects[month_name],
            challenge=challenge_objects[challenge_name]
        )


def delete_initial_data(apps, schema_editor):
    Challenge = apps.get_model('challenges', 'Challenge')
    Month = apps.get_model('challenges', 'Month')
    ChallengeMonth = apps.get_model('challenges', 'ChallengeMonth')

    ChallengeMonth.objects.all().delete()
    Challenge.objects.all().delete()
    Month.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, delete_initial_data),
    ]
