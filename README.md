<p align="center">
  <img src = "https://i.imgur.com/MLXNeHQ.png" />
</p>

## Why do we need a decetralized storage network?

Why not use Google Drive/Apple Cloud etc. ?

1. We cannot depend on centralized networks for privacy (http://bgr.com/2017/03/24/iphone-icloud-hack-threat-is-real/).
2. Faster access to data due to geographically more proximate nodes.

# What does ShatterDrive do?

ShatterDrive lets you do 2 things.

1) Host data on your computer (becoming a node on the Shatterverse)
2) Store data on the Shatterverse

Currently ShatterDrive works on a volunteer based model -- where users voluntarily give up local disk space to the network -- after ShatterDrive has been fully implemented we will be switching over to a Barter based model where you recieve X bytes of data for every Y bytes of space you give up -- in the future there might be an option to buy/sell data as well.

# Current Status

- Shamir's secret sharing Algorithm Implementation is complete.
- Adpatation of Algorithm to files in progress
- MiniGoal - Split and reconstruct a file.
- Improvements - add dynamic compression/extraction.

# RoadMap

- ~Implement file splitting/reconstruction Algorithm.~
- Enable real-time compression during splitting and decompression during reconstruction. --> In Progress
- Set up network so people can sign up as nodes.
- Work on distrubution of data and generating hash to retrieve the data.
- Move over the data storage structure to a MerkleDag.
