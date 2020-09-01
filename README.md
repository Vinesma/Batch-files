# Batch it up

A random assortment of batch files that I use.

## File Rename

Used to copy/move episodes of anime to a flash drive. Also renames them using a python script if the file follows this format:

[xx] Title - 01 [xx].mkv

Also works with .mp4

## Youtube Scraper (WIP)

Used to tell me if a new video from the Yogslive channel is from the Chilluminati or Dark Souls (WIP)

## Podcast Retriever

Stores the latest episode of a podcast I've listened to and copies X amount of episodes into my flash drive.

Works with any file that has the numbering pattern: #NN.NN where N = Number. As big of a number as you want, really. However if the number is below 10 then it's necessary to add a 0 before it or it messes with the ordering.

For example: "Podcast #3 - Title" Should be named "Podcast #03 - Title"

(Executables made with pyinstaller)

## Podcast Selector

Similar to the Retriever but designed to be automated easily with CRON.

It works by picking a set amount of random supported files and copying them over to the destination. In my use case, a folder synced to my phone. It stores the last picked files so that it doesn't pick them again in another go of the program.

Arguments are supported, pass -h for a list.
