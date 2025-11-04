import json
import random
import copy
import math

# This Game data is what defines the rules and the cards available in the game.
GAME_DATA = {
    "gameInfo": {"name": "The War of the Ages"},
    "gameRules": {
        "players": 2,
        "startingPlayerHP": 25,
        "startingHandSize": 7,
        "cardsDrawnPerTurn": 1,
        "cardsPlayablePerTurn": 1,
        "attacksPerTurn": 1,
    },
    "cardDatabase": [
        {
            "id": "woa-001",
            "tier": "Common",
            "name": "Goblin Skirmisher",
            "atk": 1,
            "def": 1,
            "hp": 3,
        },
        {
            "id": "woa-002",
            "tier": "Common",
            "name": "Orc Archer",
            "atk": 2,
            "def": 1,
            "hp": 3,
        },
        {
            "id": "woa-003",
            "tier": "Common",
            "name": "Gondor Footman",
            "atk": 2,
            "def": 2,
            "hp": 4,
        },
        {
            "id": "woa-004",
            "tier": "Common",
            "name": "Lórien Lookout",
            "atk": 2,
            "def": 2,
            "hp": 3,
        },
        {
            "id": "woa-005",
            "tier": "Common",
            "name": "Elven Scout",
            "atk": 3,
            "def": 1,
            "hp": 3,
        },
        {
            "id": "woa-006",
            "tier": "Common",
            "name": "Dwarven Miner",
            "atk": 1,
            "def": 3,
            "hp": 5,
        },
        {
            "id": "woa-007",
            "tier": "Common",
            "name": "Rohan Stablehand",
            "atk": 1,
            "def": 2,
            "hp": 4,
        },
        {
            "id": "woa-008",
            "tier": "Common",
            "name": "Misty Mountain Warg",
            "atk": 3,
            "def": 1,
            "hp": 4,
        },
        {
            "id": "woa-009",
            "tier": "Common",
            "name": "Hill-troll Runt",
            "atk": 3,
            "def": 2,
            "hp": 5,
        },
        {
            "id": "woa-010",
            "tier": "Common",
            "name": "Shadow-spawn",
            "atk": 2,
            "def": 1,
            "hp": 3,
        },
        {
            "id": "woa-011",
            "tier": "Uncommon",
            "name": "Rivendell Bladesman",
            "atk": 4,
            "def": 3,
            "hp": 6,
        },
        {
            "id": "woa-012",
            "tier": "Uncommon",
            "name": "Knight of the White Tower",
            "atk": 4,
            "def": 4,
            "hp": 6,
        },
        {
            "id": "woa-013",
            "tier": "Uncommon",
            "name": "Mirkwood Ranger",
            "atk": 5,
            "def": 2,
            "hp": 5,
        },
        {
            "id": "woa-014",
            "tier": "Uncommon",
            "name": "Iron Hills Veteran",
            "atk": 3,
            "def": 5,
            "hp": 7,
        },
        {
            "id": "woa-015",
            "tier": "Uncommon",
            "name": "Uruk-hai Captain",
            "atk": 5,
            "def": 3,
            "hp": 6,
        },
        {
            "id": "woa-016",
            "tier": "Uncommon",
            "name": "Barrow-wight",
            "atk": 4,
            "def": 2,
            "hp": 6,
        },
        {
            "id": "woa-017",
            "tier": "Uncommon",
            "name": "Haradrim Serpent-Caller",
            "atk": 4,
            "def": 3,
            "hp": 5,
        },
        {
            "id": "woa-018",
            "tier": "Uncommon",
            "name": "Watcher in the Woods",
            "atk": 3,
            "def": 3,
            "hp": 7,
        },
        {
            "id": "woa-019",
            "tier": "Uncommon",
            "name": "Stone-giant Thrower",
            "atk": 5,
            "def": 2,
            "hp": 7,
        },
        {
            "id": "woa-020",
            "tier": "Uncommon",
            "name": "Eregion Forgemaster",
            "atk": 2,
            "def": 4,
            "hp": 5,
        },
        {
            "id": "woa-021",
            "tier": "Rare",
            "name": "Captain of Gondor",
            "atk": 6,
            "def": 5,
            "hp": 8,
        },
        {
            "id": "woa-022",
            "tier": "Rare",
            "name": "Elven Lord of the West",
            "atk": 7,
            "def": 4,
            "hp": 7,
        },
        {
            "id": "woa-023",
            "tier": "Rare",
            "name": "Dwarven Runekeeper",
            "atk": 5,
            "def": 6,
            "hp": 9,
        },
        {
            "id": "woa-024",
            "tier": "Rare",
            "name": "Cavern Drake",
            "atk": 7,
            "def": 3,
            "hp": 8,
        },
        {
            "id": "woa-025",
            "tier": "Rare",
            "name": "Black Uruk Commander",
            "atk": 7,
            "def": 4,
            "hp": 8,
        },
        {
            "id": "woa-026",
            "tier": "Rare",
            "name": "Mountain Troll Chieftain",
            "atk": 6,
            "def": 5,
            "hp": 9,
        },
        {
            "id": "woa-027",
            "tier": "Rare",
            "name": "Shadow Wraith",
            "atk": 6,
            "def": 4,
            "hp": 7,
        },
        {
            "id": "woa-028",
            "tier": "Rare",
            "name": "Eagle of the Peaks",
            "atk": 5,
            "def": 3,
            "hp": 7,
        },
        {
            "id": "woa-029",
            "tier": "Legendary",
            "name": "Ur-Ghash, the Mountain's Heart",
            "atk": 9,
            "def": 7,
            "hp": 12,
        },
        {
            "id": "woa-030",
            "tier": "Legendary",
            "name": "Thraknar, the Black Calamity",
            "atk": 10,
            "def": 6,
            "hp": 11,
        },
    ],
}


class Card:
    """Represents a single card, with its stats and current state."""

    def __init__(self, card_data):
        self.id = card_data["id"]
        self.name = card_data["name"]
        self.base_atk = card_data["atk"]
        self.base_def = card_data["def"]
        self.base_hp = card_data["hp"]

        # In-game state
        self.current_hp = self.base_hp
        self.position = "ATK"  # "ATK" or "DEF"
        self.can_attack = False  # Cards can't attack the turn they are played

    def __repr__(self):
        return f"{self.name} ({self.position} {self.base_atk}/{self.base_def}/{self.current_hp}HP)"

    def take_damage(self, amount):
        """Applies damage to the card's HP."""
        self.current_hp -= amount
        return self.is_destroyed()

    def is_destroyed(self):
        """Checks if the card's HP is 0 or less."""
        return self.current_hp <= 0

    def is_atk(self):
        return self.position == "ATK"

    def is_def(self):
        return not self.is_atk()

    def get_atk(self):
        return self.base_atk

    def get_def(self):
        return self.base_def


class Player:
    """Represents a player (Human or AI) and their game state."""

    def __init__(self, name):
        self.name = name
        self.hp = GAME_DATA["gameRules"]["startingPlayerHP"]
        self.hand = []
        self.field = [None, None, None, None, None]  # 5 card slots
        self.graveyard = []

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}, Hand: {len(self.hand)})"

    def draw(self, deck):
        """Draws a card from the deck to the hand."""
        if deck:
            card = deck.pop()
            self.hand.append(card)
            print(f"{self.name} draws {card.name}.")
            return True
        print(f"{self.name} tries to draw, but the deck is empty!")
        return False

    def field_is_empty(self):
        """Checks if all field slots are None."""
        return all(slot is None for slot in self.field)

    def get_attackable_cards(self):
        """Returns a list of all cards on the field."""
        return [card for card in self.field if card is not None]

    def get_attacking_cards(self):
        """Returns cards that can attack (in ATK position and can_attack is True)."""
        return [
            card
            for card in self.field
            if card is not None and card.position == "ATK" and card.can_attack
        ]

    def set_cards_can_attack(self):
        """Sets all cards on the field to be able to attack (at start of turn)."""
        for card in self.field:
            if card:
                card.can_attack = True


class GameState:
    """
    Represents a complete snapshot of the game.
    This is the core object used by the Minimax algorithm.
    """

    def __init__(self, player1, player2, deck, turn_player, phase):
        self.players = {"p1": player1, "p2": player2}
        self.deck = deck
        self.current_turn_player = turn_player  # "p1" or "p2"
        self.phase = phase  # "DRAW", "MAIN", "BATTLE", "END"

        # Flags reset at the start of each turn
        self.has_played_card = False
        self.has_attacked = False

    def get_player(self, player_key):
        """Gets the specified player ("p1" or "p2")."""
        return self.players[player_key]

    def get_current_player(self):
        """Gets the player whose turn it is."""
        return self.players[self.current_turn_player]

    def get_opponent_player(self):
        """Gets the player who is *not* having their turn."""
        opponent_key = "p2" if self.current_turn_player == "p1" else "p1"
        return self.players[opponent_key]

    def is_game_over(self):
        """Checks if either player's HP is 0 or less."""
        return self.players["p1"].hp <= 0 or self.players["p2"].hp <= 0

    def get_winner(self):
        """Determines the winner."""
        if self.players["p1"].hp <= 0:
            return self.players["p2"].name
        elif self.players["p2"].hp <= 0:
            return self.players["p1"].name
        return None

    def get_all_possible_moves(self):
        """
        Generates a list of all possible "next" GameState objects from the current state.
        This is the heart of the Minimax tree search.
        """
        moves = []
        current_player = self.get_current_player()
        opponent_player = self.get_opponent_player()

        if self.phase == "DRAW":
            # Only one move: draw a card and move to MAIN phase
            new_state = self.deep_copy_state()
            new_player = new_state.get_current_player()
            new_player.draw(new_state.deck)
            new_player.set_cards_can_attack()  # Cards on field can now attack
            new_state.phase = "MAIN"
            moves.append(("DRAW", new_state))

        elif self.phase == "MAIN":
            # 1. Option to play a card
            if not self.has_played_card:
                for i, card_in_hand in enumerate(current_player.hand):
                    for j, field_slot in enumerate(current_player.field):
                        if field_slot is None:
                            # Try playing in ATK
                            state_atk = self.deep_copy_state()
                            player_atk = state_atk.get_current_player()
                            card_to_play = player_atk.hand.pop(i)
                            card_to_play.position = "ATK"
                            card_to_play.can_attack = False  # Can't attack this turn
                            player_atk.field[j] = card_to_play
                            state_atk.has_played_card = True
                            moves.append(
                                (
                                    f"PLAY {card_to_play.name} in ATK slot {j + 1}",
                                    state_atk,
                                )
                            )

                            # Try playing in DEF
                            state_def = self.deep_copy_state()
                            player_def = state_def.get_current_player()
                            card_to_play_def = player_def.hand.pop(i)
                            card_to_play_def.position = "DEF"
                            card_to_play_def.can_attack = False
                            player_def.field[j] = card_to_play_def
                            state_def.has_played_card = True
                            moves.append(
                                (
                                    f"PLAY {card_to_play_def.name} in DEF slot {j + 1}",
                                    state_def,
                                )
                            )

            # 2. Option to pass (always available)
            state_pass = self.deep_copy_state()
            state_pass.phase = "BATTLE"
            moves.append(("PASS MAIN", state_pass))

        elif self.phase == "BATTLE":
            # Option to attack
            if not self.has_attacked:
                attacking_cards = list(enumerate(current_player.get_attacking_cards()))
                for i, attacker_card in attacking_cards:
                    attacker_slot_index = current_player.field.index(attacker_card)

                    # Attack opponent's cards
                    target_cards = list(
                        enumerate(opponent_player.get_attackable_cards())
                    )
                    if target_cards:
                        for j, target_card in target_cards:
                            target_slot_index = opponent_player.field.index(target_card)
                            state_attack_card = self.perform_attack(
                                attacker_slot_index, target_slot_index
                            )
                            moves.append(
                                (
                                    f"ATTACK {attacker_card.name} -> {target_card.name}",
                                    state_attack_card,
                                )
                            )

                    # Attack player directly if field is empty
                    else:
                        state_attack_player = self.perform_direct_attack(
                            attacker_slot_index
                        )
                        moves.append(
                            (
                                f"ATTACK {attacker_card.name} -> PLAYER",
                                state_attack_player,
                            )
                        )

            # Option to pass (always available)
            state_pass = self.deep_copy_state()
            state_pass.phase = "END"
            moves.append(("PASS BATTLE", state_pass))

        elif self.phase == "END":
            # Only one move: end the turn
            state_end = self.deep_copy_state()
            state_end.current_turn_player = (
                "p2" if self.current_turn_player == "p1" else "p1"
            )
            state_end.phase = "DRAW"
            state_end.has_played_card = False
            state_end.has_attacked = False
            moves.append(("END TURN", state_end))

        return moves

    def perform_attack(self, attacker_slot_idx, target_slot_idx):
        """Creates a new state resulting from a card-on-card attack."""
        new_state = self.deep_copy_state()
        attacker_player = new_state.get_current_player()
        target_player = new_state.get_opponent_player()

        attacker_card = attacker_player.field[attacker_slot_idx]
        target_card = target_player.field[target_slot_idx]

        damage = (
            attacker_card.get_atk() - target_card.get_def()
            if target_card.is_def()
            else attacker_card.get_atk() - target_card.get_atk()
        )

        if target_card.is_def():
            damage = attacker_card.get_atk() - target_card.get_def()
            if damage < 0:
                print(
                    f"  > {attacker_card.name} attacks {target_card.name}, but DEF holds!"
                )
                attacker_player.hp += damage
            else:
                print(
                    f"  > {attacker_card.name} attacks {target_card.name} for {damage} damage!"
                )
                if target_card.take_damage(damage):
                    print(f"  > {target_card.name} is destroyed!")
                    target_player.field[target_slot_idx] = None
                    target_player.graveyard.append(target_card)
        else:
            damage = attacker_card.get_atk() - target_card.get_atk()
            if damage < 0:
                if attacker_card.take_damage(abs(damage)):
                    print(
                        f"  > {attacker_card.name} attacks {target_card.name} but {target_card.name} holds!"
                    )
                    print(f"  > {attacker_card.name} is destroyed!")

                    attacker_player.field[attacker_slot_idx] = None
                    attacker_player.graveyard.append(attacker_card)
                    attacker_player.hp += attacker_card.current_hp
                    print(
                        f"  > {attacker_player.name} loses {abs(attacker_card.current_hp)} points!"
                    )
                else:
                    print(
                        f"  > {attacker_card.name} attacks {target_card.name} with damage {damage}, but card survives!"
                    )
            else:
                if target_card.take_damage(damage):
                    print(
                        f"  > {attacker_card.name} attacks {target_card.name} with damage {damage}!"
                    )
                    print(f"  > {target_card.name} is destroyed!")

                    target_player.field[target_slot_idx] = None
                    target_player.graveyard.append(target_card)
                    target_player.hp += target_card.current_hp
                    print(
                        f"  > {target_player.name} loses {abs(target_card.current_hp)} points!"
                    )
                else:
                    print(
                        f"  > {attacker_card.name} attacks {target_card.name} with damage {damage}, but card survives!"
                    )

        new_state.has_attacked = True
        return new_state

    def perform_direct_attack(self, attacker_slot_idx):
        """Creates a new state resulting from a direct attack on the player."""
        new_state = self.deep_copy_state()
        attacker_player = new_state.get_current_player()
        target_player = new_state.get_opponent_player()

        attacker_card = attacker_player.field[attacker_slot_idx]
        damage = attacker_card.get_atk()

        print(
            f"  > {attacker_card.name} attacks {target_player.name} directly for {damage} damage!"
        )
        target_player.hp -= damage

        new_state.has_attacked = True
        return new_state

    def deep_copy_state(self):
        """Creates a deep copy of the current game state for tree exploration."""
        return copy.deepcopy(self)


# Minimax AI Logic


class MinimaxAI:
    """AI agent that uses the Minimax algorithm to find the best move."""

    def __init__(self, ai_player_key, max_depth=3):
        self.ai_player_key = ai_player_key  # "p1" or "p2"
        self.opponent_player_key = "p2" if ai_player_key == "p1" else "p1"
        self.max_depth = max_depth

    def find_best_move(self, game_state):
        """
        Public method to find the best move.
        Returns (best_move_description, best_move_state).
        """
        print(f"AI is thinking (depth={self.max_depth})...")
        best_val, best_move = self.minimax(
            game_state,
            self.max_depth,
            -math.inf,
            math.inf,
            True,  # AI is the maximizing player
        )
        print(f"AI chose move: {best_move[0]} with score: {best_val}")
        return best_move[0], best_move[1]

    def minimax(self, state, depth, alpha, beta, is_maximizing_player):
        """
        Performs the Minimax algorithm with Alpha-Beta Pruning.
        """

        # Base cases: game over or max depth reached
        if depth == 0 or state.is_game_over():
            return self.evaluate(state), (None, None)

        if is_maximizing_player:
            max_eval = -math.inf
            best_move = (None, None)

            for move_desc, next_state in state.get_all_possible_moves():
                eval, _ = self.minimax(
                    next_state,
                    depth - 1,
                    alpha,
                    beta,
                    # Check if the turn *actually* switched
                    next_state.current_turn_player != self.ai_player_key,
                )

                if eval > max_eval:
                    max_eval = eval
                    best_move = (move_desc, next_state)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
            return max_eval, best_move

        else:  # Minimizing player
            min_eval = math.inf
            best_move = (None, None)

            for move_desc, next_state in state.get_all_possible_moves():
                eval, _ = self.minimax(
                    next_state,
                    depth - 1,
                    alpha,
                    beta,
                    # Check if the turn *actually* switched
                    next_state.current_turn_player == self.ai_player_key,
                )

                if eval < min_eval:
                    min_eval = eval
                    best_move = (move_desc, next_state)

                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
            return min_eval, best_move

    def evaluate(self, game_state):
        """
        Heuristic function to evaluate the "goodness" of a game state for the AI.
        This is the most important part of the AI's "intelligence".
        A positive score is good for the AI, negative is bad.
        """
        if game_state.is_game_over():
            winner = game_state.get_winner()
            if winner == game_state.get_player(self.ai_player_key).name:
                return 10000  # AI wins
            else:
                return -10000  # AI loses

        ai_player = game_state.get_player(self.ai_player_key)
        opponent_player = game_state.get_player(self.opponent_player_key)

        score = 0

        # Player HP (most important)
        score += (ai_player.hp - opponent_player.hp) * 10

        # Field presence (value of cards on field)
        ai_field_score = 0
        for card in ai_player.field:
            if card:
                # Value cards in ATK by their ATK, DEF by their DEF/HP
                if card.position == "ATK":
                    ai_field_score += card.get_atk() * 2 + card.current_hp
                else:
                    ai_field_score += card.get_def() + card.current_hp

        opponent_field_score = 0
        for card in opponent_player.field:
            if card:
                if card.position == "ATK":
                    opponent_field_score += card.get_atk() * 2 + card.current_hp
                else:
                    opponent_field_score += card.get_def() + card.current_hp

        score += (ai_field_score - opponent_field_score) * 5

        # Hand advantage (more options)
        score += (len(ai_player.hand) - len(opponent_player.hand)) * 2

        return score


# Main Game Loop
class Game:
    """Main class to control the game flow."""

    def __init__(self):
        self.deck = self.build_deck()
        random.shuffle(self.deck)

        player1 = Player("Human")
        player2 = Player("AI")

        # Deal starting hands
        for _ in range(GAME_DATA["gameRules"]["startingHandSize"]):
            player1.draw(self.deck)
            player2.draw(self.deck)

        self.game_state = GameState(player1, player2, self.deck, "p1", "DRAW")
        self.ai_agent = MinimaxAI(ai_player_key="p2", max_depth=3)  # AI is player 2

    def build_deck(self):
        """Creates Card objects from the database."""
        deck = []
        for card_data in GAME_DATA["cardDatabase"]:
            deck.append(Card(card_data))
        return deck

    def print_board(self):
        """Prints a text-based representation of the game state."""
        p1 = self.game_state.get_player("p1")
        p2 = self.game_state.get_player("p2")

        print("\n" + "=" * 50)
        print(f"AI: {p2.name} (HP: {p2.hp}, Hand: {len(p2.hand)})")
        print("AI FIELD:")
        for i, card in enumerate(p2.field):
            print(f"  {i + 1}: {card if card else 'EMPTY'}")

        print("-" * 50)

        print("PLAYER FIELD:")
        for i, card in enumerate(p1.field):
            print(f"  {i + 1}: {card if card else 'EMPTY'}")
        print(f"PLAYER: {p1.name} (HP: {p1.hp}, Hand: {len(p1.hand)})")
        print("=" * 50)

    def get_human_move(self):
        """Parses human input to make a move."""
        player = self.game_state.get_current_player()

        if self.game_state.phase == "DRAW":
            input("Press Enter to draw your card...")
            return (
                "DRAW",
                self.game_state.get_all_possible_moves()[0][1],
            )  # Only one draw move

        elif self.game_state.phase == "MAIN":
            while True:
                print("\n--- MAIN PHASE ---")
                print("Your Hand:")
                for i, card in enumerate(player.hand):
                    print(
                        f"  {i + 1}: {card.name} ({card.base_atk}/{card.base_def}/{card.base_hp})"
                    )
                print("\nOptions:")
                print(
                    "  play [hand_num] [field_slot] [atk/def]  (e.g., 'play 1 1 atk')"
                )
                print("  pass")

                choice = input("> ").lower().strip()

                if choice == "pass":
                    for (
                        move_desc,
                        next_state,
                    ) in self.game_state.get_all_possible_moves():
                        if move_desc == "PASS MAIN":
                            return ("PASS MAIN", next_state)

                if choice.startswith("play"):
                    parts = choice.split()
                    if len(parts) == 4:
                        try:
                            hand_idx = int(parts[1]) - 1
                            slot_idx = int(parts[2]) - 1
                            pos = parts[3].upper()

                            if not (0 <= hand_idx < len(player.hand)):
                                print("Invalid hand number.")
                                continue
                            if not (0 <= slot_idx < len(player.field)):
                                print("Invalid field slot.")
                                continue
                            if player.field[slot_idx] is not None:
                                print("That slot is already full.")
                                continue
                            if pos not in ["ATK", "DEF"]:
                                print("Position must be 'atk' or 'def'.")
                                continue

                            card_name = player.hand[hand_idx].name
                            move_desc = f"PLAY {card_name} in {pos} slot {slot_idx + 1}"

                            for (
                                desc,
                                next_state,
                            ) in self.game_state.get_all_possible_moves():
                                if desc == move_desc:
                                    return (desc, next_state)
                            print("Error finding that move.")  # Should not happen

                        except ValueError:
                            print("Invalid input format.")
                    else:
                        print("Invalid 'play' command format.")

        elif self.game_state.phase == "BATTLE":
            while True:
                print("\n--- BATTLE PHASE ---")
                attackers = list(enumerate(player.get_attacking_cards()))
                if not attackers:
                    print("You have no cards that can attack.")
                    input("Press Enter to pass...")
                    for (
                        move_desc,
                        next_state,
                    ) in self.game_state.get_all_possible_moves():
                        if move_desc == "PASS BATTLE":
                            return ("PASS BATTLE", next_state)

                print("Your Attackers:")
                for i, card in attackers:
                    print(f"  {i + 1}: {card.name}")

                print("\nOptions:")
                print("  attack [attacker_num] [target_num] (e.g., 'attack 1 1')")
                print("  attack [attacker_num] player")
                print("  pass")

                choice = input("> ").lower().strip()

                if choice == "pass":
                    for (
                        move_desc,
                        next_state,
                    ) in self.game_state.get_all_possible_moves():
                        if move_desc == "PASS BATTLE":
                            return ("PASS BATTLE", next_state)

                if choice.startswith("attack"):
                    parts = choice.split()
                    try:
                        attacker_idx = int(parts[1]) - 1
                        if not (0 <= attacker_idx < len(attackers)):
                            print("Invalid attacker number.")
                            continue

                        attacker_card = attackers[attacker_idx][1]

                        if parts[2] == "player":
                            # Direct attack
                            move_desc = f"ATTACK {attacker_card.name} -> PLAYER"
                            for (
                                desc,
                                next_state,
                            ) in self.game_state.get_all_possible_moves():
                                if desc == move_desc:
                                    return (desc, next_state)
                            print(
                                "You can't attack the player directly (field is not empty)."
                            )

                        else:
                            # Card attack
                            target_idx = int(parts[2]) - 1
                            targets = list(
                                enumerate(
                                    self.game_state.get_opponent_player().get_attackable_cards()
                                )
                            )

                            if not (0 <= target_idx < len(targets)):
                                print("Invalid target number.")
                                continue

                            target_card = targets[target_idx][1]
                            move_desc = (
                                f"ATTACK {attacker_card.name} -> {target_card.name}"
                            )
                            for (
                                desc,
                                next_state,
                            ) in self.game_state.get_all_possible_moves():
                                if desc == move_desc:
                                    return (desc, next_state)
                            print(
                                "Error finding that attack move."
                            )  # Should not happen

                    except (ValueError, IndexError):
                        print("Invalid input format.")

        elif self.game_state.phase == "END":
            input("Press Enter to end your turn...")
            return ("END TURN", self.game_state.get_all_possible_moves()[0][1])

        return (None, None)  # Fallback

    def run(self):
        """Starts and runs the main game loop."""
        print(f"Welcome to {GAME_DATA['gameInfo']['name']}!")

        while not self.game_state.is_game_over():
            self.print_board()

            player = self.game_state.get_current_player()
            print(f"\n--- {player.name}'s Turn - {self.game_state.phase} Phase ---")

            if self.game_state.current_turn_player == "p1":  # Human
                move_desc, next_state = self.get_human_move()
                if next_state:
                    self.game_state = next_state
                else:
                    print("Error: No valid move found. This should not happen.")

            else:  # AI
                # The AI will process its *entire turn* at once by finding
                # the best move for each phase.
                move_desc, next_state = self.ai_agent.find_best_move(self.game_state)
                if next_state:
                    self.game_state = next_state
                else:
                    print("Error: AI could not find a move.")
                    # This might happen if AI has no moves, force an END TURN
                    for desc, state in self.game_state.get_all_possible_moves():
                        if "END" in desc or "PASS" in desc:
                            self.game_state = state
                            break

            # This small pause makes the AI's turn readable
            if self.game_state.current_turn_player == "p2":
                import time

                time.sleep(1)

        # Game is over
        self.print_board()
        print("\n" + "=" * 50)
        print("GAME OVER!")
        print(f"The winner is: {self.game_state.get_winner()}")
        print("=" * 50)


if __name__ == "__main__":
    game = Game()
    game.run()
