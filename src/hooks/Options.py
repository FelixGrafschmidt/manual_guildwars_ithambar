# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################

class PossibleStarts(Choice):
    """Which campaigns do you want to include in your possible start locations?"""
    display_name = "Possible Starts"
    option_all = 0
    option_prophecies = 1
    option_factions = 2
    option_nightfall = 3
    option_prophecies_factions = 4
    option_prophecies_nightfall = 5
    option_factions_nightfall = 6
    default = 6


class PossibleGoals(Choice):
    """Which campaigns do you want to include in your possible goal locations?"""
    display_name = "Possible Goals"
    option_all = 0
    option_prophecies = 1
    option_prophecies_factions = 2
    option_prophecies_nightfall = 3
    option_prophecies_eotn = 4
    option_prophecies_factions_nightfall = 5
    option_prophecies_factions_eotn = 6
    option_prophecies_nightfall_eotn = 7
    option_factions = 8
    option_factions_nightfall = 9
    option_factions_eotn = 10
    option_factions_nightfall_eotn = 11
    option_nightfall = 12
    option_nightfall_eotn = 13
    option_eotn = 14
    default = 0

class ElonaReachBonus(Toggle):
    """Should the Elona Reach bonus be enabled?"""
    display_name = "Elona Reach Bonus"
    default = False

class StartingProfessionsAmount(Range):
    """How many professions should players start with?"""
    display_name = "Starting Professions Amount"
    range_start = 1
    range_end = 8
    default = 1

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["possible_starts"] = PossibleStarts
    options["possible_goals"] = PossibleGoals
    options["elona_reach_bonus"] = ElonaReachBonus
    options["starting_professions_amount"] = StartingProfessionsAmount
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options
