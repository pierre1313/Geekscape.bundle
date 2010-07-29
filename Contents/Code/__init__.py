import PMS
from PMS import Plugin, Prefs, Log, XML, HTTP, JSON, RSS, Utils
from PMS.MediaXML import *
from PMS.Shorthand import _L, _R, _E, _D

def Start():
  Plugin.AddRequestHandler("/video/geekscape", HandleRequest, _L("Geekscape"), "icon-default.png", "art-default.png")
  Plugin.AddViewGroup("Menu", viewMode="InfoList", contentType="items")
  
def HandleRequest(pathNouns, count):
  if count == 0:
    dir = MediaContainer(title1=_L("Geekscape"), art="art-default.png", viewGroup="Menu")
    page = XML.ElementFromString(HTTP.GetCached("http://www.geekscape.net/podcasts/index.php", 7200), True)
    for episode in page.xpath("//div[@class='episode-list']"):
      title = episode.xpath("dl/dt/a")[0].text
      thumb = episode.xpath("img")[0].get("src")
      summary = episode.xpath("dl/dd[1]")[0].text
      url = episode.xpath("dl/dd/a[2]")[0].get("href")
      dir.AppendItem(VideoItem(url, title, summary, "", thumb))
    return dir.ToXML()