import os

def getScriptRelativePath():
  return os.path.dirname(os.path.realpath(__file__)) + "/"

def main():
  baseModelsPath = "../assets/eg_sign_blocks/models/block/template/hanging"
  destPath = "../assets/eg_sign_blocks/models/block/oak/hanging"
  signTexture = "hanging/oak"
  particleTexture = "stripped_oak_log"
  template = """{{
  "parent": "eg_sign_blocks:block/template/hanging/{template}",
  "textures": {{
    "sign": "minecraft:entity/signs/{signTex}",
    "particle": "minecraft:block/{particleTex}"
  }}
}}"""

  failedImgs = []

  for subdir, dirs, files in os.walk(getScriptRelativePath() + baseModelsPath):
    subdir = subdir + "\\"

    for fileName in files:
      print("Found file: ", fileName)
      print("dest: " + getScriptRelativePath() + destPath + "/" + fileName)

      with open(getScriptRelativePath() + destPath + "/" + fileName, "a") as f:
        f.write(template.format(signTex = signTexture, particleTex = particleTexture, template = fileName.replace(".json", "")))



if __name__ == "__main__":
  main()
