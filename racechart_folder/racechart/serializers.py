from rest_framework import serializers
from .models import *

class RaceSerializer(serializers.HyperlinkedModelSerializer):
    drivers = serializers.HyperlinkedRelatedField(
        view_name='driver_list',
        many=True,
        read_only=True
    )
    class Meta:
        model = Race
        fields = ('id','name', 'drivers', 'actual_distance', 'avg_speed', 'caution_laps', 'cautions', 'condition', 'distance', 'elapsed_time', 'flags', 'laps', 'laps_completed', 'lead_changes', 'race_number', 'scheduled_time', 'start_time', 'end_time', 'victory_margin',)

class StandingSerializer(serializers.HyperlinkedModelSerializer):
    driver = serializers.HyperlinkedRelatedField(
        view_name='driver_detail',
        many=False,
        read_only=True
    )
    class Meta:
        model = Standing
        fields = ('id', 'driver', 'full_name', 'rank', 'avg_finish_position', 'avg_laps_completed', 'avg_start_postion', 'chase_bonus', 'dnf', 'in_chase', 'laps_completed', 'laps_led', 'laps_led_pct', 'points', 'poles', 'stage_wins', 'starts', 'status', 'top_5', 'top_10', 'top_15', 'top_20', 'wins',)

class ResultSerializer(serializers.ModelSerializer):
    # race = serializers.HyperlinkedRelatedField(
    #     view_name='race_detail',
    #     many=False,
    #     read_only=True
    # )
    # driver = serializers.HyperlinkedRelatedField(
    #     view_name='driver_detail',
    #     many=False,
    #     read_only=True
    # )
    class Meta:
        model = Result
        fields =('id', 'driver', 'race', 'avg_position', 'avg_speed', 'best_lap', 'best_lap_speed', 'best_lap_time', 'bonus_points', 'driver_rating', 'elapsed_time', 'fastest_laps', 'laps_completed', 'laps_led', 'passes_made', 'passing_differential', 'penalty_points', 'pit_stops', 'points', 'position', 'quality_passes', 'start_position', 'status', 'times_led', 'times_passed')

class DriverSerializer(serializers.ModelSerializer):
    # team = serializers.HyperlinkedRelatedField(
    # view_name='team_detail',
    # many=False,
    # read_only=True
    # )

    class Meta:
        model = Driver
        fields = ('driver_id', 'team', 'full_name', 'birth_place', 'birthday', 'country', 'car_number', 'gender', 'height', 'hobbies', 'driver_id', 'last_name', 'residence', 'rookie_year', 'status', 'twitter',)

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    drivers = serializers.HyperlinkedRelatedField(
    view_name='driver_detail',
    many=True,
    read_only=True
    )

    class Meta:
        model = Team
        fields=('name', 'drivers', 'crew_chief', 'manufacturer', 'sponsors', 'owner',)
