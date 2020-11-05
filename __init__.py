from mycroft import MycroftSkill, intent_file_handler


class AnimalSounds(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sounds.animal.intent')
    def handle_sounds_animal(self, message):
        animal = message.data.get('animal')

        self.speak_dialog('sounds.animal', data={
            'animal': animal
        })


def create_skill():
    return AnimalSounds()

