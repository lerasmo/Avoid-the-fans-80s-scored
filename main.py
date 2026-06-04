def on_overlap_tile(sprite, location):
    global instrumentos_restantes
    tiles.set_tile_at(location, assets.tile("""
        transparency16
        """))
    info.change_score_by(1)
    instrumentos_restantes += -1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument4
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite7, location7):
    tiles.set_tile_at(location7, assets.tile("""
        transparency16
        """))
    info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        fan3
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite4, location4):
    tiles.set_tile_at(location4, assets.tile("""
        transparency16
        """))
    info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        fan2
        """),
    on_overlap_tile3)

def on_overlap_tile4(sprite8, location8):
    if instrumentos_restantes == 0:
        info.change_score_by(int(info.countdown()))
        game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        exit
        """),
    on_overlap_tile4)

def on_overlap_tile5(sprite6, location6):
    global instrumentos_restantes
    tiles.set_tile_at(location6, assets.tile("""
        transparency16
        """))
    info.change_score_by(1)
    instrumentos_restantes += -1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument0
        """),
    on_overlap_tile5)

def on_overlap_tile6(sprite5, location5):
    tiles.set_tile_at(location5, assets.tile("""
        transparency16
        """))
    info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        fan1
        """),
    on_overlap_tile6)

def on_overlap_tile7(sprite3, location3):
    global instrumentos_restantes
    tiles.set_tile_at(location3, assets.tile("""
        transparency16
        """))
    info.change_score_by(1)
    instrumentos_restantes += -1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument1
        """),
    on_overlap_tile7)

def on_overlap_tile8(sprite2, location2):
    global instrumentos_restantes
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
        """))
    info.change_score_by(1)
    instrumentos_restantes += -1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument3
        """),
    on_overlap_tile8)

instrumentos_restantes = 0
scene.set_background_color(13)
tiles.set_tilemap(tilemap("""
    level1
    """))
mySprite = sprites.create(assets.image("""
    rockstar
    """), SpriteKind.player)
tiles.place_on_random_tile(mySprite, assets.tile("""
    transparency16
    """))
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
info.start_countdown(30)
instrumentos_restantes = 6