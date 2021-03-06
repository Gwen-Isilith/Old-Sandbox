# Sarah

# Appearance
appearance_dictionary = {
    "Head": {
        "Hair": {
            "Description": "self.appearance_dictionary[\"Head\"][\"Hair\"][\"Length\"] + \" \" + self.appearance_dictionary[\"Head\"][\"Hair\"][\"Color\"] + \" hair.\"",
            "Length": "long",
            "Color": "black",
        },
        "Eyes": {

        },
        "Ears": {

        },
        "Nose": {

        },
        "Mouth": {

        },
    },
    "Arms": {
        "Hands": {
            "Description": "",
        }
    },
    "Body": {

    },
    "Lower Body": {

    },
    "Legs": {

    },
}
# Dialogue
dialogue_intro = "Hey there! What did you want to talk about?"
dialogue_ask_to_continue = "Was there something else you wanted to talk about?"
dialogue_continue = "What else did you want to talk about?"
dialogue_initiate = "Hey, do you want to talk?"
dialogue_rejected = "Oh... Okay"
dialogue_dictionary = {
    "Weekend": {
        "True": "if self.friendship < 10:\n"
                "   self.friendship += 1\n"
                "self.__say__(\"I like to spend my weekends out, I'm sure you'll catch me at one of the bars around "
                "here if you like to dance.\") ",
    },
    "Hold_Hands": {
        "not self.Hold_Hands_state and self.friendship >= 10 or self.romance >= 5": "self.Hold_Hands(approval=["
                                                                                    "\"Asked\",True])",
        "not self.my_turn and not self.Hold_Hands_state": "self.Hold_Hands(approval=[\"Asked\",False])",
        "not self.my_turn and self.Hold_Hands_state": "self.Stop(\"Hold_Hands\")",
        "self.Hold_Hands_state and self.friendship < 10 and self.romance < 10 and self.my_turn": "self.Stop("
                                                                                                 "\"Hold_Hands\")",
        "Ask": "Could I hold your hand?",
        "Accept": "if self.friendship < 20:\n"
                  "   self.friendship += 1\n"
                  "elif self.friendship >= 20 and romance < 5:\n"
                  "   self.romance += 1\n"
                  "self.__say__(\"I'd love to hold your hand!\")",
        "Reject": "self.__say__(\"I don't think so.\")",
        "Rejected": "self.friendship -= 1\n"
                    "self.loneliness += 1\n"
                    "self.__say__(\"Oh...sorry, I thought...\")",
        "Ask Stop": "Could we stop holding hands?",
        "Force": "self.loneliness > 20",
        "Forced": "self.friendship -= 2\n"
                  "self.romance -= 2\n"
                  "self.__say__(\"P-please let go.\")",
        "Forcing": "self.romance += 1\nself.__say__(\"I just really need this right now.\")",
        "CNC": "self.__say__(\"Huh?! Oh. You could have just asked to hold hands you know.\")",
        "Stopped": "pass",
        "In progress": "self.__say__(\"We're already holding hands silly!\")",
        "Initiated": "if self.friendship < 20:\n"
                     "  self.friendship += 1\n"
                     "elif self.friendship >= 20 and self.romance < 5:\n"
                     "  self.romance += 1\n"
                     "self.__say__(\"Yay!\")",
    },
}
# Schedule
schedule = {
    "Monday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Park",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
    "Tuesday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Park",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
    "Wednesday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Success",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
    "Thursday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Park",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
    "Friday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Park",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
    "Saturday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Park",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
    "Sunday": {
        "1AM": {
            "True": "Park",
        },
        "2AM": {
            "True": "Park",
        },
        "3AM": {
            "True": "Park",
        },
        "4AM": {
            "True": "Park",
        },
        "5AM": {
            "True": "Park",
        },
        "6AM": {
            "True": "Park",
        },
        "7AM": {
            "True": "Park",
        },
        "8AM": {
            "True": "Park",
        },
        "9AM": {
            "True": "Park",
        },
        "10AM": {
            "True": "Park",
        },
        "11AM": {
            "True": "Park",
        },
        "12AM": {
            "True": "Park",
        },
        "1PM": {
            "True": "Park",
        },
        "2PM": {
            "True": "Park",
        },
        "3PM": {
            "True": "Park",
        },
        "4PM": {
            "True": "Park",
        },
        "5PM": {
            "True": "Park",
        },
        "6PM": {
            "True": "Park",
        },
        "7PM": {
            "True": "Park",
        },
        "8PM": {
            "True": "Park",
        },
        "9PM": {
            "True": "Park",
        },
        "10PM": {
            "True": "Park",
        },
        "11PM": {
            "True": "Park",
        },
        "12PM": {
            "True": "Park",
        },
    },
}
# Stats
stats_dictionary = {
    "friendship": 0,
    "romance": 0,
    "loneliness": 0,
}
