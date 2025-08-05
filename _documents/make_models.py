import os

def main():
  makeHangingModelSet("eg_sign_blocks", "minecraft:entity/signs/hanging/acacia", "minecraft:block/stripped_acacia_log", "eg_sign_blocks:block/acacia/hanging")
  makeNormalModelSet("eg_sign_blocks", "minecraft:entity/signs/acacia", "minecraft:block/acacia_planks", "eg_sign_blocks:block/acacia/normal")
  makeBlockstates("eg_sign_blocks:block/acacia/normal", "minecraft:acacia_sign", "minecraft:acacia_wall_sign", "eg_sign_blocks:block/acacia/hanging", "minecraft:acacia_hanging_sign", "minecraft:acacia_wall_hanging_sign")

def getScriptRelativePath():
  return os.path.dirname(os.path.realpath(__file__)) + "/"

def contains(str: str, containsStr: str):
    return (not (containsStr not in str.lower()))

def addMinecraftNamespaceIfAbsent(str: str):
  if(contains(str, ":")):
    return str
  return "minecraft:" + str

def makeFiles(baseModelsPath: str, destPath: str, signTexture: str, particleTexture: str, template: str, templateNamespace: str):
  for subdir, dirs, files in os.walk(getScriptRelativePath() + baseModelsPath):
    subdir = subdir + "\\"

    for fileName in files:
      print("Making model for: ", fileName)
      fullDestPath = getScriptRelativePath() + destPath
      if(not os.path.exists(fullDestPath)):
        os.makedirs(fullDestPath)

      fullDestPath = fullDestPath + "/" + fileName
      print("dest: " + fullDestPath)

      with open(fullDestPath, "w") as f:
        signTexLocation = addMinecraftNamespaceIfAbsent(signTexture).split(":")
        particleTexLocation = addMinecraftNamespaceIfAbsent(particleTexture).split(":")
        f.write(template.format(signTex = signTexLocation[1], signTexNamespace = signTexLocation[0], particleTexNamespace = particleTexLocation[0], particleTex = particleTexLocation[1], template = fileName.replace(".json", ""), namespace = templateNamespace))

def makeHangingModelSet(templateNamespace: str, signTexture: str, particleTexture: str, modelDest: str):
  hangingSignModels = f"../assets/{templateNamespace}/models/block/template/hanging"
  modelDestLocation = addMinecraftNamespaceIfAbsent(modelDest).split(":")
  hangingSignDest = f"../assets/{modelDestLocation[0]}/models/{modelDestLocation[1]}"
  hangingSignTemplate = """{{
  "parent": "{namespace}:block/template/hanging/{template}",
  "textures": {{
    "sign": "{signTexNamespace}:{signTex}",
    "particle": "{particleTexNamespace}:{particleTex}"
  }}
}}"""

  makeFiles(hangingSignModels, hangingSignDest, signTexture, particleTexture, hangingSignTemplate, templateNamespace)
  
def makeNormalModelSet(templateNamespace: str, signTexture: str, particleTexture: str, modelDest: str):
  signModels = f"../assets/{templateNamespace}/models/block/template/normal"
  modelDestLocation = addMinecraftNamespaceIfAbsent(modelDest).split(":")
  signDest = f"../assets/{modelDestLocation[0]}/models/{modelDestLocation[1]}"
  signTemplate = """{{
  "parent": "{namespace}:block/template/normal/{template}",
  "textures": {{
    "sign": "{signTexNamespace}:{signTex}",
    "particle": "{particleTexNamespace}:{particleTex}"
  }}
}}"""

  makeFiles(signModels, signDest, signTexture, particleTexture, signTemplate, templateNamespace)
  
def makeBlockstates(normalModelsPath: str, normalBlockstate: str, normalWallBlockstate: str, hangingModelsPath: str, hangingDest: str, hangingWallDest: str):
  blockstateLocation = addMinecraftNamespaceIfAbsent(normalBlockstate).split(":")
  wallBlockstateLocation = addMinecraftNamespaceIfAbsent(normalWallBlockstate).split(":")
  normalModelsPathLocation = addMinecraftNamespaceIfAbsent(normalModelsPath).split(":")
  signTemplate = f"""{{
  "variants": {{
    "rotation=0": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign"
    }},
    "rotation=1": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_22.5"
    }},
    "rotation=2": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_45"
    }},
    "rotation=3": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_-22.5",
      "y": 90
    }},
    "rotation=4": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign",
      "y": 90
    }},
    "rotation=5": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_22.5",
      "y": 90
    }},
    "rotation=6": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_45",
      "y": 90
    }},
    "rotation=7": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_-22.5",
      "y": 180
    }},
    "rotation=8": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign",
      "y": 180
    }},
    "rotation=9": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_22.5",
      "y": 180
    }},
    "rotation=10": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_45",
      "y": 180
    }},
    "rotation=11": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_-22.5",
      "y": 270
    }},
    "rotation=12": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign",
      "y": 270
    }},
    "rotation=13": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_22.5",
      "y": 270
    }},
    "rotation=14": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_45",
      "y": 270
    }},
    "rotation=15": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/sign_-22.5",
      "y": 0
    }}
  }}
}}"""
  wallSignTemplate = f"""{{
  "variants": {{
    "facing=north": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/wall_sign"
    }},
    "facing=east": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/wall_sign",
      "y": 90
    }},
    "facing=south": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/wall_sign",
      "y": 180
    }},
    "facing=west": {{
      "model": "{normalModelsPathLocation[0]}:{normalModelsPathLocation[1]}/wall_sign",
      "y": 270
    }}
  }}
}}"""

  writeBlockstateFile(f"../assets/{blockstateLocation[0]}/blockstates", blockstateLocation[1], signTemplate)
  writeBlockstateFile(f"../assets/{wallBlockstateLocation[0]}/blockstates", wallBlockstateLocation[1], wallSignTemplate)

  hangingBlockstateLocation = addMinecraftNamespaceIfAbsent(hangingDest).split(":")
  hangingWallBlockstateLocation = addMinecraftNamespaceIfAbsent(hangingWallDest).split(":")
  hangingModelsPathLocation = addMinecraftNamespaceIfAbsent(hangingModelsPath).split(":")
  hangingSignTemplate = f"""{{
  "multipart": [
    {{
      "when": {{
        "rotation": "0"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "1"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_22.5",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "2"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_45",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "3"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_-22.5",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "4"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "5"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_22.5",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "6"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_45",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "7"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_-22.5"
      }}
    }},
    {{
      "when": {{
        "rotation": "8"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board"
      }}
    }},
    {{
      "when": {{
        "rotation": "9"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_22.5"
      }}
    }},
    {{
      "when": {{
        "rotation": "10"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_45"
      }}
    }},
    {{
      "when": {{
        "rotation": "11"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_-22.5",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "12"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "13"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_22.5",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "14"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_45",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "15"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board_-22.5",
        "y": 180
      }}
    }},

    {{
      "when": {{
        "rotation": "0",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "1",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_22.5",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "2",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_45",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "3",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_-22.5",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "4",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "5",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_22.5",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "6",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_45",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "7",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_-22.5"
      }}
    }},
    {{
      "when": {{
        "rotation": "8",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point"
      }}
    }},
    {{
      "when": {{
        "rotation": "9",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_22.5"
      }}
    }},
    {{
      "when": {{
        "rotation": "10",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_45"
      }}
    }},
    {{
      "when": {{
        "rotation": "11",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_-22.5",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "12",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "13",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_22.5",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "14",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_45",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "15",
        "attached": "true"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_point_-22.5",
        "y": 180
      }}
    }},

    {{
      "when": {{
        "rotation": "0",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "1",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_22.5",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "2",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_45",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "rotation": "3",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_-22.5",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "4",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "5",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_22.5",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "6",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_45",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "rotation": "7",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_-22.5"
      }}
    }},
    {{
      "when": {{
        "rotation": "8",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight"
      }}
    }},
    {{
      "when": {{
        "rotation": "9",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_22.5"
      }}
    }},
    {{
      "when": {{
        "rotation": "10",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_45"
      }}
    }},
    {{
      "when": {{
        "rotation": "11",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_-22.5",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "12",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "13",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_22.5",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "14",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_45",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "rotation": "15",
        "attached": "false"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight_-22.5",
        "y": 180
      }}
    }}
  ]
}}"""
  wallHangingSignTemplate = f"""{{
  "multipart": [
    {{
      "when": {{
        "facing": "north"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/plank"
      }}
    }},
    {{
      "when": {{
        "facing": "north"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board"
      }}
    }},
    {{
      "when": {{
        "facing": "north"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight"
      }}
    }},

    {{
      "when": {{
        "facing": "east"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/plank",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "facing": "east"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board",
        "y": 90
      }}
    }},
    {{
      "when": {{
        "facing": "east"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight",
        "y": 90
      }}
    }},

    {{
      "when": {{
        "facing": "south"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/plank",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "facing": "south"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board",
        "y": 180
      }}
    }},
    {{
      "when": {{
        "facing": "south"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight",
        "y": 180
      }}
    }},

    {{
      "when": {{
        "facing": "west"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/plank",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "facing": "west"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/board",
        "y": 270
      }}
    }},
    {{
      "when": {{
        "facing": "west"
      }},
      "apply": {{
        "model": "{hangingModelsPathLocation[0]}:{hangingModelsPathLocation[1]}/chains_straight",
        "y": 270
      }}
    }}
  ]
}}"""

  writeBlockstateFile(f"../assets/{hangingBlockstateLocation[0]}/blockstates", hangingBlockstateLocation[1], hangingSignTemplate)
  writeBlockstateFile(f"../assets/{hangingWallBlockstateLocation[0]}/blockstates", hangingWallBlockstateLocation[1], wallHangingSignTemplate)
    

def writeBlockstateFile(dest: str, filename: str, contents: str):
  hangingFullFolderPath = getScriptRelativePath() + "/" + dest
  hangingFullDestPath = hangingFullFolderPath + "/" + filename + ".json"
  if(not os.path.exists(hangingFullFolderPath)):
    os.makedirs(hangingFullFolderPath)

  print("Making blockstate file: " + hangingFullDestPath)

  with open(hangingFullDestPath, "w") as f:
    f.write(contents)

if __name__ == "__main__":
  main()
