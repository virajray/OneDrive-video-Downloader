<h1>OneDrive-video-Downloader</h1>

<p>OneDrive-video-Downloadet is open-source Python-based software available on GitHub that you can download Onedrive videos and Microsoft Teams recordings that has no download option and are hidden to other downloaders.</p>

<h2>How to Find required link</h2>

<p>01. first clone the repo into your machine and run <a href="requiredpkgs.sh">requiredpkgs.sh</a> download all the required packages and files required</p>
<p>02. Go to the recording/Video URL. Now you can view the video but you have no option to download the video.</p>
<p>03. open dev tools in the browser and go to the Network tab.</p>
<p>04. In the network tab, search the following command using the search area.

<code>videomanifest?provider</code></p>
![image](https://github.com/virajray/OneDrive-video-Downloader/assets/36956604/1444d28f-e3a0-4ada-9e40-96c13a4ddeff)


<p>Then reload the webpage again.</p>

<p>click on the highlighted area and you can see the right panel is viewing some contents like this.</p>

![image](https://github.com/virajray/OneDrive-video-Downloader/assets/36956604/f74d6edf-2374-4aba-a5f9-cd88b9f08edf)



<p>Now you can find the URL under Request URL and Copy that entire URL.</p>






<h2>To run this software you need to have the following packages installed on your computer</h2>
(these installations are automated in <a href="requiredpkgs.sh">requiredpkgs.sh</a> for your easy ness. However, if you face any difficulty with it, you can download it manually from the links below)
<ul>
<li><a href="https://www.ffmpeg.org/download.html">FFMPEG</a></li>
<li><a href="https://www.python.org/downloads/release/python-3120/">Python3</a></li>
</ul>
