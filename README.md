General Description:

When playing Othello, the following components are considered:
* There are 2 players → the black and wite tiles.
* An initial Board (8x8) where 4 tiles are positioned: 2 for each color.

The player with the black tiles is the one who starts the game. Othello consists of positioning new tiles, these tiles need to flank your opposite's tiles. To accomplishing that you have a maximum of 8 movements which are:
    -   Right
    -   Left
    -   Up
    -   Down
    -   Up to the Right
    -   Up to the Left
    -   Down to the Right
    -   Down to the Left

If the player wants to positionante a tile, the flank rule must be considered. You can't positionate your tile wherever you want. So the players have to play smart and positionate the tile where they can flank more opposite positions. 
The game is over when there are no more possible empty spaces to position a tile or when there are empty spaces but no possible flank tiles. 


We want to program an intelligent game where the computer is able to find the best position to flank more tiles. 
In this case, given that we have 2 players,  we will follow the Adversarial search techniques:
    -   Initial State: As it was mentioned before, the initial state consists of a board with 4 tiles. 
    -   Final State: The final state is the board where there are no empty spaces or possible flank tiles. 
    -   Players: The two players are the human and the computer.
    -   Actions: As it was indicated, depending on the tile you are considering, the player has a maximum of 8 possible positions. 
    -   Result: Giving the board, the position and the player, the result will be the board where the tile is positioned and the corresponding tile(s) was/were flanked.
    -   Utility: Given a final state, the utility function calculated a valyue to express if the player wins or loses. 
    -   Terminal Test: It determines if the game is over. 

As required, the program has been evaluted with these heuristics functions
    -   Heuristic 1
        def otello_heuristic(state:ndarray):
            return state.sum()
    -   Heuristic 2
    -   Heuristic 3
    We have chosen the .......
Hence we are working with the MinMaxWithDepth algorithm, we won't expand the whole game three, that's why the heuristics  represent an approach to the utility value and these will be used when the depth is reached. 

The Cut-Off algorithm has been implemented and different 'Depth' values have been evaluated:
    -   Value 1
    -......
    The best Depth is.... 

Alpha-Beta pruning is an other algorithm that helps us to get an efficient behavior, because we will prun the unnecesary states. When this optimization is applied...... 