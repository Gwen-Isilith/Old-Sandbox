# Character name (note file must be Charactername.py with the characters name being capitalized)

# Dialogue
dialogue_intro = "This is what a character will say upon initiating dialogue."
dialogue_ask_to_continue = "This is what a character will say when asking if the character wants to continue dialogue."
dialogue_continue = "This is what a character will say when asking what topic a continued conversation should be about."
dialogue_initiate = "This is what a character will say when asking the player to talk with them."
dialogue_rejected = "This is what a character will say when the player declines to talk to them."
dialogue_dictionary = {
    "Topic": {
        "condition == bool": "print(\"Text you want the character to say goes inside of the parentheses\".)\nprint("
                             "\"You can use as many print statements or other function calls on the same line (you "
                             "can also use \\n for multi line dialogue instead of a new print statement. And ' can be "
                             "used for apostrophes as long as one uses quotation marks as shown here.))",
        "condition != \"string\" and condition2 == additional value": "print(\"Whichever response evaluates as true "
                                                                      "first (from the top) will be the only "
                                                                      "one used. No two conditions can be "
                                                                      "exactly the same. (You can have "
                                                                      "friendship > 0 and friendship > 0 "
                                                                      "and romance > 0 but not friendship > "
                                                                      "0 and friendship > 0). To use "
                                                                      "character stats or other character "
                                                                      "related data self. must be prefixed to "
                                                                      "the condition (such as self.friendship > "
                                                                      "0).)\") ",
        "condition == value": "self.function(\"parameter1\",\"parameter2\")\nprint(\"Functions, including character "
                              "methods (denoted by self.) can be called along side dialogue. For example this can be "
                              "used to call actions or change a characters stats.\")",
        "True": "print(\"Set the last condition to True to create a default response, this response will be said if no "
                "conditional responses are. You can only have one default response per topic. If you want a character "
                "to always say the same thing for a topic this should be the only conditional in this topic. If this "
                "is a topic that shouldn't be brought up by the character unless one of the conditions is met (such "
                "as for actions) you should set this default statement to \"if not self.my_turn\" which will always "
                "evaluate True if it is the players turn but not on the Characters turn.\") ",

    },
    "Action": {
        "condition == bool": "print(\"Each action must have a topic of the same name within the dictionary. When asking"
                             " to do an action, either through talking or just through the action itself these "
                             "conditions will be used to determine whether or not the action is carried through and "
                             "so the conditions should always include:\")\nself.Action(approval=[\"Asked\","
                             "True])\nprint(\"If the action should be performed if this condition is true. "
                             "Or:\")\nself.Action(approval=[\"Asked\",False]\nprint(\"if the action should not be "
                             "performed\") ",
        "Keyword": "print(\"Actions have certain keywords for certain responses to actions these should be listed after"
                   "all of the conditions so they don't attempt to be evaluated before the default response. Listed "
                   "below are all of the Keywords for the base game with a description of it's use as it's value.\")",
        "Ask": "What the character says when asking to do the action",
        "Accept": "self.__say__(\"What the character says when they accept to the action after being asked.\")",
        "Reject": "self.__say__(\"What the character says when they dont accept to the action after being asked.\")",
        "Rejected": "self.friendship -= 1\nself.__say__(\"What the character says when their attempt to initiate the "
                    "action is rejected. As shown in this example, keywords that are executed (shown by the inclusion "
                    "of self.__say__) can also change character stats. \")",
        "Ask Stop": "What the character says when they ask the player to stop.",
        "Force": "the condition that if met the character will attempt to force the player to do the action if they "
                 "say no. For example: self.loneliness > 20. Set to False if the character should never force the "
                 "character to do action (for characters that will never force the character to do anything this "
                 "keyword should be set to False for all actions).",
        "Forced": "self.__say__(\"What the character says when they are being forced to participate in the action.\")",
        "Forcing": "self.__say__(\"What the character says if they are forcing the player to participate in the "
                   "action.\")",
        "CNC": "self.__say__(\"What the character says when they are forced to participate in the action, "
               "but they would have consented if asked. If a character should not disguish between if they would have "
               "of consented or not you can set this equal to \"self.[topic][\"Forced\"]\". \")",
        "Stopped": "pass\nself.__say__(\"pass can be used so that nothing unique is said by the character and the "
                   "action is handled as normal. This is what the character says when the action is stopped by the "
                   "player.\")",
        "In progress": "self.__say__(\"This is what the character says when the player tries to do an action that is "
                       "already happening.\")",
        "Initiated": "self.__say__(\"What the character says when they initiate the action and the player consents.\")"
    }
}
# Stats (Note stats must have an initial value in order to be used by the character, even if that value is 0 (or None))
stats_dictionary = {
    "stat": "value",
    "stat2": 0
}
