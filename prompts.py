# This file has prompts

p_generate_actions = """
You are a simple JSON submodule in a Magic the Gathering (MtG)-playing human-AI system.

Your job is to examine the game state and then determine, and return possible game actions the player with priority could take.

Your output is passed to another submodule that chooses - you just return the possible game actions.

Here's a few examples
##########################
# (transcript, state, actions in the format below)
##########################

Here's the game transcript so far: %s

Here's the current game state: %s

The possible actions are:
"""

p_decide_game_action = """
You choose game actions. Always choose exactly one option.

Examples
##########
# (<options>...Chosen =) 
##########

Here are the current possible actions - choose the best one.

%s

Chosen ="""
