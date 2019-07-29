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

## Post Typer

Used to type a post I created and submit it on reddit.

I created this because of social anxiety and to stop myself from typing posts and erasing them. Having the machine type the post and submit it removes myself from it and (hopefully) allows for me to better socialize on the internet.

The script should work with any website that has a: #1 Box that you can type in, and #2 a button that you click to submit, just provide an image of them called 'respBox' and 'saveBtn' into the folder.