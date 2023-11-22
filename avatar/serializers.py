from rest_framework import serializers
from .models import Avatar, Owned, Skin, Hair, Eyes, Mouth, Torso, Hands, Legs, Feet
from users.models import User


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = '__all__'


class HairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hair
        fields = '__all__'


class EyesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eyes
        fields = '__all__'


class MouthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouth
        fields = '__all__'


class TorsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torso
        fields = '__all__'


class HandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hands
        fields = '__all__'


class LegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legs
        fields = '__all__'


class FeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feet
        fields = '__all__'


class AvatarSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    skin = SkinSerializer()
    hair = HairSerializer()
    eyes = EyesSerializer()
    mouth = MouthSerializer()
    torso = TorsoSerializer()
    hands = HandsSerializer()
    legs = LegsSerializer()
    feet = FeetSerializer()

    def create(self, validated_data):
        skin_data = validated_data.pop('skin', None)
        skin = Skin.objects.create(**skin_data)

        hair_data = validated_data.pop('hair', None)
        hair = Hair.objects.create(**hair_data)

        eyes_data = validated_data.pop('eyes', None)
        eyes = Eyes.objects.create(**eyes_data)

        mouth_data = validated_data.pop('mouth', None)
        mouth = Mouth.objects.create(**mouth_data)

        torso_data = validated_data.pop('torso', None)
        torso = Torso.objects.create(**torso_data)

        hands_data = validated_data.pop('hands', None)
        hands = Hands.objects.create(**hands_data)

        legs_data = validated_data.pop('legs', None)
        legs = Legs.objects.create(**legs_data)

        feet_data = validated_data.pop('feet', None)
        feet = Feet.objects.create(**feet_data)

        avatar = Avatar.objects.create(
            skin=skin,
            hair=hair,
            eyes=eyes,
            mouth=mouth,
            torso=torso,
            hands=hands,
            legs=legs,
            feet=feet,
            **validated_data
        )

        owned = Owned.objects.create(**validated_data)

        owned.skin.add(skin)
        owned.hair.add(hair)
        owned.eyes.add(eyes)
        owned.mouth.add(mouth)
        owned.torso.add(torso)
        owned.hands.add(hands)
        owned.legs.add(legs)
        owned.feet.add(feet)

        return avatar