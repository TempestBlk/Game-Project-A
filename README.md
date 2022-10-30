# A Turn-Based PVE Module
## Goals -
    1. Build a module to handle turn based combat
    2. Build a display window module
## Update Log -
> v0.2.1
- added player character levelup
-  moved Encounter prints to Interface

> v0.2.0 - Rebuilt Update
- rebuilt module from the ground up...

> v0.1.5
- added 'Flesh Butcher' to entities
- tested encounter w/ npc w/ multiple attacks

> v0.1.4
- added 'show stats' option to main menu for displaying importantant stats
- added exp and lvl to PlayerCharacter
  - added related methods to PlayerCharacter
  - checks for levelup at end of encounter
- consolidated get and set methods in entities.py
- new Attacks class for tracking info on all atks

> v0.1.3
- added target and attack menus on player turn
- made random_encounter into Encounter class with run_encounter method
- added pc, enemies, allies, downed_list, & turn_order to Encounter class attributes
- added optional enemies & allies arguments to Encounter
- if no enemies are passed to Encounter, it will generate a default set on run_encounter
- added optional name argument to entities
- added detection for first letters of a given menu option but commented it out due to possibility of options/attacks/entities with shared first letters
- changed class Humanoid to Entity
- removed currently unused attributes from Entity
- implements add_atk method for Entity (takes a list of attack dicts)
- cannot choose "random encounter" from main menu if player hp <= 0
- other minor improvements to run_encounter, & option_menu

> v0.1.2
- fixed issue where player downed caused other turns in round to be skipped
- debug functions are now methods of class Debug
- minor optimizations to random_encounter

> v0.1.1
- on their turn, npcs will choose an attack from their attack list and use it on a random enemy
- combatant rolls attack checked against target ac, then rolls for and inflicts damage
- if a combatant's hp >= 0 then they get "downed" status
- downed combatants are added to encounter's downed_list at end of current turn
- npcs can wait on their turn if no more hostile targets
- if pc is downed, encounter ends when round concludes
- minor changes, setup for player turns

> v0.1.0
- new project