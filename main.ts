scene.onOverlapTile(SpriteKind.Player, assets.tile`instrument4`, function (sprite, location) {
    tiles.setTileAt(location, assets.tile`transparency16`)
    info.changeScoreBy(1)
    instrumentos_restantes += -1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`fan3`, function (sprite7, location7) {
    tiles.setTileAt(location7, assets.tile`transparency16`)
    info.changeScoreBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`fan2`, function (sprite4, location4) {
    tiles.setTileAt(location4, assets.tile`transparency16`)
    info.changeScoreBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`exit`, function (sprite8, location8) {
    if (instrumentos_restantes == 0) {
        info.changeScoreBy(Math.trunc(info.countdown()))
        game.gameOver(true)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`instrument0`, function (sprite6, location6) {
    tiles.setTileAt(location6, assets.tile`transparency16`)
    info.changeScoreBy(1)
    instrumentos_restantes += -1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`fan1`, function (sprite5, location5) {
    tiles.setTileAt(location5, assets.tile`transparency16`)
    info.changeScoreBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`instrument1`, function (sprite3, location3) {
    tiles.setTileAt(location3, assets.tile`transparency16`)
    info.changeScoreBy(1)
    instrumentos_restantes += -1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`instrument3`, function (sprite2, location2) {
    tiles.setTileAt(location2, assets.tile`transparency16`)
    info.changeScoreBy(1)
    instrumentos_restantes += -1
})
let instrumentos_restantes = 0
scene.setBackgroundColor(13)
tiles.setTilemap(tilemap`level1`)
let mySprite = sprites.create(assets.image`rockstar`, SpriteKind.Player)
tiles.placeOnRandomTile(mySprite, assets.tile`transparency16`)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
info.startCountdown(30)
instrumentos_restantes = 6
