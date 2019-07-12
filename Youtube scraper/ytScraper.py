import requests, bs4

res = requests.get('https://www.youtube.com/user/yogslive/videos')
type(res)

res.raise_for_status() # Raises an exception if the download is unsuccessful

# Opens a file and saves the html data inside
saveFile = open('webHtml.txt', 'wb') # Opens in binary mode
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
saveFile.close()

#parses html into the variable
htmlFile = open('webHtml.txt')
parsedHtml = bs4.BeautifulSoup(htmlFile.read(), features="html.parser")
selection = parsedHtml.select('h3 .yt-uix-sessionlink') #<h3> with an <a class="yt-uix-sessionlink">
type(selection)
htmlFile.close()

videoTitles = open('videoData.txt', 'w')
for videos in selection:
    # print(videos.attrs['title'] + ', Link: ' + videos.attrs['href'])
    videoTitles.write(videos.attrs['title'] + ', ' + videos.attrs['href'] + '\n')
videoTitles.close()
print('ytScraper executed successfully!')
