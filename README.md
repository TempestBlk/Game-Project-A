# Game Project "A"

## Goals
    Version 0.3
      - Player controlled turns
      - Stamina System
      - Items & Inventory
      - Wearable System
      - Gold Flakes
      - Leveling
      - Differing Encounters

## Update Log
> v0.2.6
- rebuilt encounter system

> v0.2.5
- added 'press enter to go back' menu hints
- Wearables now lose durability when hit
- npc dialogue now handled by npcs
- inventory menu now handled by Inventory
- improved Weapon and Wearable

> v0.2.4
- Wearables now provide Protection
  - each body part recieves slash, pierce, blunt protection
  - only torse protection applies for now
  - every 5 protection reduces damage by 1
  - every 10 protection decreases toHit by 1
- updated Merchant menu
  - can sell items for gold flakes
  - buyPrice and sellPrice modifiers
- "p" in main menu displays current protection
- turn report now shows combatant weapons
- updated Inventory to handle wearables
- modified Attack stats

> v0.2.3
- added Equipped section to Inventory
- improved npc menus

> v0.2.2
- added Merchant, Doctor, and Inventory
- added gold flakes as currency
- improved encounter menu
- player character now recieves +2 max_hp on levelup
- added humanoid.unequip
- improved Encounters.buildEnemies

> v0.2.1
- added player character levelup
- Interface now handles Encounter prints

> v0.2.0 - First Major Update!
  
    Rebuilt this module from the ground up!
    The original update log is below.

### Before Version 0.2

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
