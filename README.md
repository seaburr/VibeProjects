# VibeProjects

A collection of poorly conceived, even more poorly prompted projects generated by AI. 
The goal is very little if any massaging of the code once it's generated. Also very little effort over all.

`~~no tests just vibes~~`

## ColoringBook

Generates simplistic black and white line art suited for coloring pages. Prompts user for input text before generating 
image, displaying it, and saving it to disk with a timestamped filename.

**NOTE:** Works better with DALLE3 (although it overshoots the complexity IMO however cost is \$0.05/image vs. \$0.02/image with DALLE2).

Expects `OPENAI_API_KEY` environment variable when running.

## TracingWorksheet

An attempt to generate letter/number tracing worksheets. Big fail. Bigger fail once I toggled DALLE3 off. Then I tried
to get it to render the image without AI. It still failed (see V2).

## DrawAndGuessShape

A failed attempt to build a game in Python. ChatGPT pushed me to the one below.

## DrawAndGuessGameV2

A HTML+JS single page game that draws some number of random shapes and asks the play to click on the matching one.