from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
class CoronaVirusSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(CoronaVirusSkill, self).__init__(name="CoronaVirus")

    @intent_handler(IntentBuilder("").require("Definition"))
    def handle_hello_world_intent(self):
        self.speak_dialog("corona.definition")

    @intent_handler(IntentBuilder("").require("symptoms"))
    def handle_count_intent(self):
        self.speak_dialog("corona.symptoms")

    @intent_handler(IntentBuilder("").require('prevention'))
    def handle_focus_history(self):
        self.speak_dialog('corona.prevention')

def create_skill():
    return CoronaVirusSkill()
