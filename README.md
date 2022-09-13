# CS:GO KillWell
😂 'KillWell' exploit developed for CS:GO (Counter-Strike: Global Offensive) that allows the exploiter to force bots to target a specific player and turn on literal AI aimbot. The AI will ignore any other players and shoot through walls, they can also flick within literal milliseconds and it makes the game unplayable for your target. This only lasts until the round is over, you can target only 1 person at a time unfortunately.

## Explaination
When sending a packet to the CS:GO official servers, we can send a specially crafted packet that requires 0 client-server authentication and essentially tells the server to make bots target a specific player (based on steamID) with actual aimbot. LOL.

**Simple explaination**
```
+-----------+       +---------+
| EXPLOITER |-------| Server  |
+-----------+       +----+----+
                         |
+-----------+       +----+----+
| VICTIM    |-------|  Bots   |
+-----------+       +---------+
```
