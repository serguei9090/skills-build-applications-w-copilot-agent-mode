from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='john.doe@example.com', name='John Doe'),
            User(id=ObjectId(), email='jane.smith@example.com', name='Jane Smith'),
            User(id=ObjectId(), email='alice.jones@example.com', name='Alice Jones'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team(id=ObjectId(), name='Team Alpha', members=users)
        team.save()

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Running', duration=30, date=date(2025, 4, 1)),
            Activity(id=ObjectId(), user=users[1], type='Cycling', duration=45, date=date(2025, 4, 2)),
            Activity(id=ObjectId(), user=users[2], type='Swimming', duration=60, date=date(2025, 4, 3)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=team, score=100),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Morning Run', description='A quick morning run to start the day'),
            Workout(id=ObjectId(), name='Evening Yoga', description='Relaxing yoga session in the evening'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
