from os.path import isfile

from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import play_wav


class AnimalSounds(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def sound_file_path(self, animal):
        if animal[-1] == 's':
            animal = animal[:-1]
        path = f"{self.root_dir}/sounds/{animal}.wav"
        self.log.info(path)
        return path if isfile(path) else None

    @intent_file_handler('sounds.animal.intent')
    def handle_sounds_animal(self, message):
        animal = message.data.get('animal')
        sound_file = self.sound_file_path(animal)
        if sound_file:
            play_wav(sound_file)
        else:
            self.speak_dialog('not.sure', data={
                'animal': animal
            })


def create_skill():
    return AnimalSounds()

