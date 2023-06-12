import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="AriaSoma_Sprite.ico")
]

cx_Freeze.setup(
    name = "CastlevaniaRiseOfSorrow",
    options = {
        "build_exe":{
            "packages": ["pygame"],
            "include_files": [
                "castle.png",
                "AriaSoma_Sprite.png"
            ]
        }
    } , executables = executables
)