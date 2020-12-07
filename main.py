import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:

    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity( int( screen_width / 2 ), int( screen_height / 2 ), "@", ( 255, 255, 255 ) )

    game_map = generate_dungeon(
        max_rooms = max_rooms,
        room_min_size = room_min_size,
        room_max_size = room_max_size,
        map_width = map_width,
        map_height = map_height,
        max_monsters_per_room = max_monsters_per_room,
        player = player,
    )

    engine = Engine( event_handler = event_handler, game_map = game_map, player = player )

    # With is basically C#'s using statement
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Yet Another Roguelike Tutorial",
        vsync = True,
    ) as context:
        root_console = tcod.Console( screen_width, screen_height, order = "F" )
        while True: # Main game loop?
            engine.render( console = root_console, context = context )
            
            # Waits for user input
            events = tcod.event.wait()

            # Sends the events to the engine
            engine.handle_events( events )

if __name__ == "__main__":
    main()
