# PMS plugin framework
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

####################################################################################################

VIDEO_PREFIX = "/video/geekscape"

NAME = L('Title')

# make sure to replace artwork with what you want
# these filenames reference the example files in
# the Contents/Resources/ folder in the bundle
ART           = 'art-default.png'
ICON          = 'icon-default.png'

####################################################################################################

def Start():
    Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, L('Title'), ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)


def VideoMainMenu():

  dir = MediaContainer(title1="Geekscape", art=R(ART), viewGroup="List")
  page = XML.ElementFromURL("http://pod.geekscape.tv/Geekscape-Video.xml",cacheTime=7200)
  for episode in page.xpath("//item"):
    title = episode.xpath("title")[0].text
    summary = episode.xpath("description")[0].text
    url = episode.xpath("enclosure")[0].get("url")
    dir.Append(VideoItem(url, title, summary, "", thumb=R(ICON)))
  return dir
