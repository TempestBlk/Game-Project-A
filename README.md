# A Turn-Based PVE Module
## Intent -
    To prototype combat based encounters for integration with a larger project
## Update Log -
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