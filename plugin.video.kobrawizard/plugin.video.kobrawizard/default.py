import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import shutil
import urllib2,urllib
import re, subprocess
import extract
import downloader
import time,base64
import plugintools
from addon.common.addon import Addon
from addon.common.net import Net


################################################################################
### THIS WIZARD HAS BEEN MODDED BY KOBRA...IT MAY BE SHIT...BUT IT WORKS :-) ###
################################################################################

#############################################################################
### IF YOU USE ANY PART OF THIS WIZARD PLEASE CREDIT THE ORIGINAL AUTHORS ###
#############################################################################

###################
### USEFUL SHIT ###
###################

#xbmc.executebuiltin('RestartApp')#
#if not os.path.exists('/data/data/com.rechild.advancedtaskkiller'):#
#remove the "not" to check if it does exist. The above will return true if it's not found#




USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
HOME = xbmc.translatePath('special://home/')
ADDONS = os.path.join(HOME,     'addons')
addon_id = 'plugin.video.kobrawizard'
ADDON = xbmcaddon.Addon(id=addon_id)
AddonID = 'plugin.video.kobrawizard'
AddonTitle = "[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]WIZARD[/B][/COLOR]"
AddonTitle2 = "[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE PACKAGE FILES[/B][/COLOR]"
AddonTitle3 = "[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]FILE CLEANER[/B][/COLOR]"
dialog = xbmcgui.Dialog()
net = Net()
U = ADDON.getSetting('User')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
VERSION = "0.0.1"
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "Kobra Wizard"
BASEURL = "http://bit.do"
BASEURL1 = "http://kobra24.com/builds"
BASEURL2 = "http://kobra24.com/test"
PACKAGES = os.path.join(ADDONS,   'packages')
H = 'http://'
#excludes for fresh start
EXCLUDES  = ['plugin.video.kobrawizard','script.module.addon.common','script.kobra.builds','plugin.program.kobra.notifications','repository.kobra','plugin.video.kobra.tube','program.kobra.app.installer']

###################
###### INTRO ######
###################

def INTRO():
    xbmc.executebuiltin( "PlayMedia(special://home/addons/plugin.video.kobrawizard/resources/intro/Groundbreaking HD.mp4)" )
    xbmc.sleep(4000)
    INDEX()

    

#################
### MAIN MENU ###
#################

def INDEX():
    addDir('[COLOR ghostwhite]KOBRA INSTALL AND UPDATES[/COLOR]',BASEURL,2,ART+'install1.png',FANART,'')
    addDir('[COLOR ghostwhite]KOBRA MAINTENANCE TOOLS[/COLOR]',BASEURL,3,ART+'maintenance1.png',FANART,'')
    addDir('[COLOR ghostwhite]CONTACT KOBRA BUILDS[/COLOR]',BASEURL,8,ART+'contact1.png',FANART,'')
    #addDir('KOBRA ANDROID ONLY BUILD',BASEURL,12,ART+'androidonly1.png',FANART,'')
    addDir('[COLOR ghostwhite]KOBRA H24 ICON PACKS[/COLOR]',BASEURL,16,ART+'iconpacks1.png',FANART,'')
    addDir('[COLOR ghostwhite]KOBRA H24 HOME MENU PACKS[/COLOR]',BASEURL,99,ART+'homemenupacks1.png',FANART,'')
    addDir('[COLOR ghostwhite]KOBRA H24 BACKGROUND PACKS[/COLOR]',BASEURL,24,ART+'backgroundpacks1.png',FANART,'')
    addDir('[COLOR ghostwhite]KOBRA H24 THEME PACKS[/COLOR]',BASEURL,26,ART+'themepacks1.png',FANART,'')
    addDir('[COLOR ghostwhite]KOBRA APP INSTALLER[/COLOR]',BASEURL,28,ART+'appinstaller1.png',FANART,'')
    addDir('[COLOR ghostwhite]TWEAKS AND FIXES[/COLOR]',BASEURL,99,ART+'tweaksandfixes1.png',FANART,'')
    addDir('[COLOR ghostwhite]PREVIEW VIDEOS[/COLOR]',BASEURL,30,ART+'previewvideos1.png',FANART,'')
    addDir('[COLOR ghostwhite]UNINSTALL KILLER APP[/COLOR]',BASEURL,32,ART+'uninstallapp.png',FANART,'')
    addDir('[COLOR dodgerblue]MQ7 PIMPED By PAULSK2[/COLOR]',BASEURL,33,ART+'sk2.png',FANART,'')
    setView('movies', 'MAIN')

###################
### COMING SOON ###
###################

def COMINGSOON():
    addDir('COMING SOON...',BASEURL,0,ART+'comingsoon.png',FANART,'')
    setView('movies', 'MAIN')

##################
### ICONS MENU ###
##################

def ICONINDEX():
    addDir('COLOUR ICON PACKS',BASEURL,14,ART+'colourpacks1.png',FANART,'')
    addDir('MICELLANEOUS ICON PACKS',BASEURL,18,ART+'miscellaneous1.png',FANART,'')
    addDir('ANIMATED ICON PACKS (KODI-SPMC 16 OR ABOVE ONLY)',BASEURL,99,ART+'animatedicons1.png',FANART,'')
    addDir('USER SUBMITTED ICON PACKS',BASEURL,99,ART+'usersubmitted1.png',FANART,'')
    setView('movies', 'MAIN')


##################################
### BACKGROUNDS INSTALLER MENU ###
##################################

def BACKGROUNDSMENU():
    addDir('STANDARD',BASEURL,23,ART+'standard1.png',FANART,'')
    addDir('ANIMATED (KODI-SPMC 16 OR ABOVE ONLY)',BASEURL,99,ART+'animatedicons1.png',FANART,'')
    addDir('USER SUBMITTED PACKS',BASEURL,99,ART+'usersubmitted1.png',FANART,'')
    setView('movies', 'MAIN')


##########################
### APP INSTALLER MENU ###
##########################

def APPINSTALLERMENU():
    addDir('ANDROID APPS',BASEURL,21,ART+'androidapps.png',FANART,'')
    addDir('ADULT ADROID APPS',BASEURL,99,ART+'adultapps.png',FANART,'')
    setView('movies', 'MAIN')


############################
### KOBRA H24 BUILD MENU ###
############################


def BUILDMENU():
    addDir('KOBRA-H24 WITH ADULT CONTENT...ONLY USE ON A FRESH INSTALLATION OF KODI OR SPMC',BASEURL+'/cQLQi',5,ART+'adultfreshinstall.png',FANART,'')
    addDir('KOBRA-H24 WITH ADULT CONTENT UPDATE',BASEURL+'/cQLQD',5,ART+'adultupdate.png',FANART,'')
    addDir('KOBRA-H24 NO ADULT CONTENT...ONLY USE ON A FRESH INSTALLATION OF KODI OR SPMC',BASEURL+'/cQLQz',5,ART+'nonadultfreshinstall.png',FANART,'')
    addDir('KOBRA-H24 NO ADULT CONTENT UPDATE',BASEURL+'/cQLQH',5,ART+'nonadultupdate.png',FANART,'')
    addDir('!TEST AREA! DO NOT USE',BASEURL2+'/test.zip',5,ART+'testarea.png',FANART,'')
    setView('movies', 'MAIN')

######################################
######### ANDROID BUILDMENU ##########
######################################

def ANDROIDMENU():
    addDir('KOBRA-H24 ADULT. ANDROID ONLY!. USE ON A FRESH INSTALL',BASEURL+'',5,ART+'kobrah24android.png',FANART,'')
    addDir('KOBRA-H24 ADULT. ANDROID ONLY! UPDATE',BASEURL+'',5,ART+'kobrah24androidupdate.png',FANART,'')
    setView('movies', 'MAIN')

########################
### MAINTENANCE MENU ###
########################

def MAINTENANCE():
    addDir('DELETE CACHE','url',4,ART+'deletecache1.png',FANART,'')
    addDir('FRESH START','url',6,ART+'freshstart1.png',FANART,'')
    addDir('DELETE PACKAGES','url',7,ART+'deletepackages1.png',FANART,'')
    setView('movies', 'MAIN')

###########################
### BACKGROUNDINSTALLER ###
###########################

def BACKGROUNDINSTALLER(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]BACKGROUND PACK INSTALLER[/B][/COLOR]",description,"FOR USE ON KOBRA H24 BUILD ONLY!","WOULD YOU LIKE TO INSTALL THIS BACKGROUND PACK?","NO, GO BACK","YES, INSTALL"):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]BACKGROUND PACK INSTALLER[/B][/COLOR]","DOWNLOADING YOUR BACKGROUNDS... ",'', 'PLEASE WAIT...')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "EXTRACTING YOUR BACKGROUNDS...PLEASE WAIT...")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP()
    dialog.ok("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]BACKGROUND PACK INSTALLATION COMPLETE[/B][/COLOR]]", '                  BROUGHT TO YOU BY KOBRA BUILDS.', '                       CLICK [COLOR grey][B]OK[/B][/COLOR] TO RELOAD THE SKIN.')
    xbmc.executebuiltin('UnloadSkin()')
    xbmc.executebuiltin('ReloadSkin()')


#########################
### BACKGROUND WIZARD ###
#########################

def BACKGROUNDWIZARD():
    link = OPEN_URL('http://kobracustombuilds.com/tools/backgrounds/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,22,iconimage,fanart,description)
    setView('list', 'MAIN')
	
def SK2WIZARD():
    link = OPEN_URL('http://kobracustombuilds.com/sk2/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('list', 'MAIN')

#######################################
###### COLOR ICON PACK INSTALLER ######
#######################################

def ICONPACKINSTALLER(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]ICON PACK INSTALLER[/B][/COLOR]",description,"FOR USE ON KOBRA H24 BUILD ONLY!","WOULD YOU LIKE TO INSTALL THIS ICON PACK?","NO, GO BACK","YES, INSTALL"):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]ICON PACK INSTALLER[/B][/COLOR]","DOWNLOADING YOUR ICONS... ",'', 'PLEASE WAIT...')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "EXTRACTING YOUR ICONS...PLEASE WAIT...")
    time.sleep(2)
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP()
    dialog.ok("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]ICON PACK INSTALLATION COMPLETE[/B][/COLOR]", '                  BROUGHT TO YOU BY KOBRA BUILDS.', '                       CLICK [COLOR grey][B]OK[/B][/COLOR] TO RELOAD THE SKIN.')
    xbmc.executebuiltin('UnloadSkin()')
    xbmc.executebuiltin('ReloadSkin()')

#############################
###### THEME INSTALLER ######
#############################

def THEMEINSTALLER(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]THEME INSTALLER[/B][/COLOR]",description,"FOR USE ON KOBRA H24 BUILD ONLY!","WOULD YOU LIKE TO INSTALL THIS THEME?","NO, GO BACK","YES, INSTALL"):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]THEME INSTALLER[/B][/COLOR]","DOWNLOADING YOUR THEME... ",'', 'PLEASE WAIT...')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "EXTRACTING YOUR THEME...PLEASE WAIT...")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP()
    dialog.ok("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]THEME INSTALLATION COMPLETE[/B][/COLOR]", '                  BROUGHT TO YOU BY KOBRA BUILDS.', '                       CLICK [COLOR grey][B]OK[/B][/COLOR] TO RELOAD THE SKIN.')
    xbmc.executebuiltin('UnloadSkin()')
    xbmc.executebuiltin('ReloadSkin()')

###############################################
########### ANDROID APPS INSTALLER ############
###############################################

#def ANDROIDAPPSINSTALLER(name,url,description):
   #confirm=xbmcgui.Dialog()
   #if confirm.yesno("[COLOR grey2][B]ANDROID APP INSTALLER[/B][/COLOR]",name,"","WOULD YOU LIKE TO DOWNLOAD THIS APP?","NO, GO BACK","YES, DOWNLOAD"):
    ###Testing on windows###
    #downloadpath = xbmc.translatePath(os.path.join('c:/users/andy/desktop'))
    #downloadpath = xbmc.translatePath(os.path.join('/storage/emulated/0/download/'))#
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR grey2][B]KOBRA APP INSTALLER[/B][/COLOR]","DOWNLOADING YOUR APP",'', 'PLEASE WAIT...')
    #lib=os.path.join(downloadpath, name+'.apk')
    #downloader.download(url, lib, dp)
    #addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    #choice = xbmcgui.Dialog().yesno('APP DOWNLOAD COMPLETE', 'WOULD YOU LIKE TO INSTALL THE APP?', 'PLEASE NOTE, TO INSTALL THIS APPLICATION YOU WILL NEED [COLOR blue]ES FILE EXPLORER FILE MANAGER[/COLOR] INSTALLED ON YOUR DEVICE. THIS CAN BE DOWNLOADED FROM GOOGLE PLAY OR THE AMAZON STORE.', nolabel='CLOSE',yeslabel='INSTALL  APP')
    #if choice == 0:
    #   return
    #elif choice == 1:
    #   pass
    #xbmc.executebuiltin("StartAndroidActivity(com.estrongs.android.pop)")



###############################################
###### MICELLANEOUS ICON PACK INSTALLER #######
###############################################

def MICELLANEOUSICONPACKINSTALLER(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]ICON PACK INSTALLER[/B][/COLOR]",description,"FOR USE ON KOBRA H24 BUILD ONLY!","WOULD YOU LIKE TO INSTALL THIS ICON PACK?","NO, GO BACK","YES, INSTALL"):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]ICON PACK INSTALLER[/B][/COLOR]","DOWNLOADING YOUR ICONS... ",'', 'PLEASE WAIT...')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "EXTRACTING YOUR ICONS...PLEASE WAIT...")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP()
    dialog.ok("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]ICON PACK INSTALLATION COMPLETE[/B][/COLOR]", '                  BROUGHT TO YOU BY KOBRA BUILDS.', '                       CLICK [COLOR grey][B]OK[/B][/COLOR] TO RELOAD THE SKIN.')
    xbmc.executebuiltin('UnloadSkin()')
    xbmc.executebuiltin('ReloadSkin()')

####################
### THEME WIZARD ###
####################

def THEMEWIZARD():
    link = OPEN_URL('http://kobracustombuilds.com/tools/themes/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,27,iconimage,fanart,description)
    setView('list', 'MAIN')

################################
### ANDROID APPS CATERGORIES ###
################################

def ANDROIDAPPSWIZARD():
    link = OPEN_URL('http://kobracustombuilds.com/apks/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,20,iconimage,fanart,description)
    setView('list', 'MAIN')

########################
### COLOUR ICONS URL ###
########################

def ICONCATEGORIES():
    link = OPEN_URL('http://kobracustombuilds.com/tools/iconpacks/colourpacks/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,15,iconimage,fanart,description)
    setView('list', 'MAIN')

##############################
### MICELLANEOUS ICONS URL ###
##############################

def MICELLANEOUSICONCATEGORIES():
    link = OPEN_URL('http://kobracustombuilds.com/tools/iconpacks/miscellaneous/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,17,iconimage,fanart,description)
    setView('list', 'MAIN')

################
### OPEN URL ###
################

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link


#################################
####### POPUP TEXT BOXES ########
#################################

def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()

####################
### SOCIAL MEDIA ###
####################

def CONTACT():
    xbmc.executebuiltin("RunAddon(plugin.program.kobra.notifications)")

#####################
### VIDEO PREVIEW ###
#####################

def VIDEOPREVIEW():
    xbmc.executebuiltin("RunAddon(plugin.video.kobra.tube)")

#####################
### APP INSTALLER ###
#####################

def APPINSTALLER():
    xbmc.executebuiltin("RunAddon(program.kobra.app.installer)")
	


	
#####################
### APP UNINSTALL ###
#####################

def APPUNINSTALL():
    xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.DELETE","","package:com.robbzkiill3r.iint3liig3ncii")')
    INDEX()
    #xbmc.executebuiltin('StartAndroidActivity(,android.intent.action.VIEW,,url:http://kodi.tv)')
	#xbmc.executebuiltin('StartAndroidActivity(com.android.apphere,android.intent.action.VIEW,,http://pathhere/)')
	#os.system('am start --user 0 -a android.intent.action.VIEW -d http://kodi.tv -n com.estrongs.android.pop/.view.FileExplorerActivity')


#####################
### BUILD INSTALL ###
#####################

def WIZARD(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]WIZARD INSTALLER[/B][/COLOR]",name,"WOULD YOU LIKE TO INSTALL?","","NO, GO BACK","YES, INSTALL"):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    download(url, lib)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.create("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]WIZARD INSTALLER[/B][/COLOR]","INSTALLING BUILD",'', 'PLEASE WAIT...')
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    CLEANUP()
    dialog.ok("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]WIZARD INSTALLER[/B][/COLOR]", "TO SAVE CHANGES YOU NOW NEED TO FORCE CLOSE KODI-SPMC, PRESS OK TO CLOSE KODI-SPMC")
    killxbmc()



################################
####### DELETE PACKAGES ########
#### THANKS GUYS @ XUNITY ######
#### MODIFIED BY AFTERMATH #####
################################

def DELETEPACKAGES():
    if os.path.exists(PACKAGES):
        try:
            for root, dirs, files in os.walk(PACKAGES):
                file_count = 0
                file_count += len(files)
                # Count files and give option to delete
                if file_count > 0:
                    if dialog.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE PACKAGE FILES[/B][/COLOR]", str(file_count) + " FILES FOUND", "WOULD YOU LIKE TO DELETE THEM?", nolabel='NO, CANCEL',yeslabel='YES, REMOVE'):
                        for f in files: os.unlink(os.path.join(root, f))
                        for d in dirs: shutil.rmtree(os.path.join(root, d))
                        dialog.ok(AddonTitle2,'CLEAR PACKAGES: [COLOR green] SUCCESS[/COLOR]!')
                else: dialog.ok(AddonTitle2,'CLEAR PACKAGES: [COLOR red]NONE FOUND[/COLOR]!')
        except: dialog.ok(AddonTitle2,'CLEAR PACKAGES: [COLOR red] ERROR[/COLOR]!')
    else: dialog.ok(AddonTitle2,'CLEAR PACKAGES: [COLOR red] NONE FOUND[/COLOR]!')

################################
###### CLEAN UP PACKAGES #######
##### THANKS GUYS @ XUNITY #####
################################

def CLEANUP():
    if os.path.exists(PACKAGES):
        try:
            for root, dirs, files in os.walk(PACKAGES):
                file_count = 0
                file_count += len(files)
                # Count files and give option to delete
                if file_count > 0:
                    if dialog.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]FILE CLEANER[/B][/COLOR]", str(file_count) + " FILES FOUND", "WOULD YOU LIKE TO DELETE THEM?", nolabel='NO, CANCEL',yeslabel='YES, REMOVE'):
                        for f in files: os.unlink(os.path.join(root, f))
                        for d in dirs: shutil.rmtree(os.path.join(root, d))
                        dialog.ok(AddonTitle3,'CLEAN UP FILES: [COLOR green] SUCCESS[/COLOR]!')
                else: dialog.ok(AddonTitle3,'CLEAN UP FILES: [COLOR red]NONE FOUND[/COLOR]!')
        except: dialog.ok(AddonTitle3,'CLEAN UP FILES: [COLOR red] ERROR[/COLOR]!')
    else: dialog.ok(AddonTitle3,'CLEAN UP FILES: [COLOR red] NONE FOUND[/COLOR]!')



################################
######## DELETE CACHE ##########
##### THANKS GUYS @ XUNITY######
################################

def deletecachefiles(url):
    print '############################################################       DELETING STANDARD CACHE             ###############################################################'
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
    if os.path.exists(xbmc_cache_path)==True:
        for root, dirs, files in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE CACHE FILES[/B][/COLOR]", str(file_count) + " FILES FOUND", "DO YOU WANT TO DELETE THEM?"):

                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass

            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')

        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)

            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')

        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)

            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass
              # Set path to Cydia Archives cache files


    # Set path to What th Furk cache files
    wtf_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.whatthefurk/cache'), '')
    if os.path.exists(wtf_cache_path)==True:
        for root, dirs, files in os.walk(wtf_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete WTF Cache Files", str(file_count) + " files found", "Do you want to delete them?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass

                # Set path to 4oD cache files
    channel4_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.4od/cache'), '')
    if os.path.exists(channel4_cache_path)==True:
        for root, dirs, files in os.walk(channel4_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete 4oD Cache Files", str(file_count) + " files found", "Do you want to delete them?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass

                # Set path to BBC iPlayer cache files
    iplayer_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache'), '')
    if os.path.exists(iplayer_cache_path)==True:
        for root, dirs, files in os.walk(iplayer_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete BBC iPlayer Cache Files", str(file_count) + " files found", "Do you want to delete them?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass


                # Set path to Simple Downloader cache files
    downloader_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.module.simple.downloader'), '')
    if os.path.exists(downloader_cache_path)==True:
        for root, dirs, files in os.walk(downloader_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE SIMPLE DOWNLOADER CACHE FILES[/B][/COLOR]", str(file_count) + " FILES FOUND", "DO YOU WANT TO DELETE THEM?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass

                # Set path to ITV cache files
    itv_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.itv/Images'), '')
    if os.path.exists(itv_cache_path)==True:
        for root, dirs, files in os.walk(itv_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE ITV CACHE FILES[/B][/COLOR]", str(file_count) + " FILES FOUND", "DO YOU WANT TO DELETE THEM?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass

                # Set path to temp cache files
    temp_cache_path = os.path.join(xbmc.translatePath('special://home/temp'), '')
    if os.path.exists(temp_cache_path)==True:
        for root, dirs, files in os.walk(temp_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE TEMP DIR CACHE FILES[/B][/COLOR]", str(file_count) + " FILES FOUND", "DO YOU WANT TO DELETE THEM?"):

                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

            else:
                pass


    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]DELETE CACHE FILES[/B][/COLOR]", "ALL CACHE FILES HAVE BEEN REMOVED","", "BROUGHT TO YOU BY KOBRA WIZARD")


def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

###############################################################
###### FORCE CLOSE KODI - ANDROID ONLY WORKS IF ROOTED ########
################# LEE @ COMMUNITY BUILDS ######################
###############################################################

def killxbmc():
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close Kodi-SPMC [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close Kodi-SPMC [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android
        print "############   try android force close  #################"

########################
#### ][NT3L][G3NC][ ####
########################

        if 'com.robbzkiill3r.iint3liig3ncii' not in iiNT3LiiAPK():
            xbmcgui.Dialog().ok("[COLOR grey][B]INSTALL APPLICATION[/B][/COLOR]", "[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]","[COLOR grey]THERE IS A NEW APP TO FORCE CLOSE KODI AND SPMC![/COLOR]","[COLOR grey]WHEN PROMPTED, PLEASE INSTALL THE APP. PLEASE CLICK OK TO CONTINUE[/COLOR]")
            path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
            lib=os.path.join(path, 'iiNT3LiiKiiLL3R.apk')
            link = OPEN_URL(iiNT3LiiBrothers('WVVoU01HTkViM1pNTW5SMldXNUthRmt6Vm5wa1J6bDBXVzVXY0dKSFVucE1iVTUyWWxNNWFHTkhkSHBNTTJSd1pXMUdlVnBET1doalIzTjFaRWhvTUVOblBUMD0=')).replace('\n','').replace('\r','')
            regex = r'name=".+?".+?rl="(.+?com.robbzkiill3r.iint3liig3ncii.apk)"'
            iiNT3LiiKiiLL3R = re.search(regex,link)
            urllib.urlretrieve(iiNT3LiiKiiLL3R.group(1), lib)
            xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
            time.sleep(5)
            xbmcgui.Dialog().ok("[COLOR cyan][B]][[/B]NT3L[B]][[/B]G3NC[B]][[/B][/COLOR]","","[COLOR grey]OPERATION COMPLETED! PLEASE CLICK OK TO FORCE CLOSE AND RESTART KODI-SPMC[/COLOR]","")

        os.system('am start --user 0 -a android.intent.action.MAIN -c android.intent.category.HOME')
        iiNT3LiiHOME = xbmc.translatePath('special://home')
        iiNT3LiiPATH = xbmc.translatePath(iiNT3LiiHOME).split("/")
        iiNT3LiiGOT = False
        if 188==188:
            i = 0
            for iiNT3LiiDIR in iiNT3LiiPATH:
                if iiNT3LiiDIR.count('.') >= 2:
                    iiNT3LiiGOT = True
                    break
                else:
                    i+=1
            if iiNT3LiiGOT == True:
                iiNT3LiiWHAT = iiNT3LiiPATH[i]

        if "org.xbmc.kodi" in iiNT3LiiWHAT:
            os.system('am start --user 0 -n com.robbzkiill3r.iint3liig3ncii/.iiNT3LiiStopGoKodii &')

        else:
            os.system('am start --user 0 -n com.robbzkiill3r.iint3liig3ncii/.iiNT3LiiStopGoSPMC &')
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close Kodi-SPMC [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close Kodi-SPMC [COLOR=lime]DO NOT[/COLOR] exit via the menu.","iOS detected.  Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo.")

##########################
### DETERMINE PLATFORM ###
##########################

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


########################
#### ][NT3L][G3NC][ ####
########################

def iiNT3LiiAPK():
    InstalledAPK = subprocess.Popen(['exec ''/system/bin/pm list packages -3'''], executable='/system/bin/sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].rstrip('\n').splitlines()
    for i in range(len(InstalledAPK)):
        InstalledAPK[i] = InstalledAPK[i].partition(':')[2]
    return InstalledAPK


def iiNT3LiiBrothers(url):
    Jose = url
    Mathews = base64.b64decode(Jose)
    iiNT3LiiG3NCii = base64.b64decode(Mathews)
    Robb = base64.b64decode(iiNT3LiiG3NCii)
    return Robb

def download(url, dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]WIZARD INSTALLER[/B][/COLOR]","DOWNLOADING YOUR BUILD ",'', '')
    dp.update(0)
    oneTime=time.time()
    urllib.urlretrieve(url, dest, lambda numblocks,blocksize,filesize: _pbhook(numblocks,blocksize,filesize,dp,oneTime))


def _pbhook(numblocks,blocksize,filesize,dp,oneTime):
    try:
        percent = min(numblocks * blocksize * 100 / filesize, 100)
        currently_downloaded = float(numblocks) * blocksize / (1024 * 1024)
        kbps_speed = numblocks * blocksize / (time.time() - oneTime)
        if kbps_speed > 0:
            eta = (filesize - numblocks * blocksize) / kbps_speed
        else:
            eta = 0
        kbps_speed = kbps_speed / 1024
        total = float(filesize) / (1024 * 1024)
        mblocksize = '[COLOR grey]Progress:[/COLOR] [COLOR red]%.02f MB[/COLOR] [COLOR grey]of[/COLOR] [COLOR red]%.02f MB[/COLOR]' % (currently_downloaded, total)
        theETA = '[COLOR grey]Eta:[/COLOR] [COLOR red]%02d:%02d[/COLOR]  ' % divmod(eta, 60)
        theETA += '  [COLOR grey]Speed:[/COLOR] [COLOR red]%.02f [/COLOR][COLOR grey]Kb/s[/COLOR]' % kbps_speed
        precent = '[COLOR red]'+str(percent)+'[/COLOR]'
        dp.update(percent, theETA, mblocksize)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled():
        dp.close()

############################
####### FRESH START ########
#### THANKS TO TVADDONS ####
############################

def FRESHSTART(params):
    plugintools.log("freshstart.main_list "+repr(params)); yes_pressed=plugintools.message_yes_no("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]FRESH START[/B][/COLOR]","DO YOU WISH TO RESTORE YOUR KODI-SPMC CONFIGURATION TO DEFAULT SETTINGS? [COLOR red][B]WARNING [/B][/COLOR]ALL YOUR DATA WILL BE LOST AND NOT RECOVERABLE. [COLOR red][B]PROCEED?[/B][/COLOR]")
    if yes_pressed:
        addonPath=xbmcaddon.Addon(id=AddonID).getAddonInfo('path'); addonPath=xbmc.translatePath(addonPath);
        xbmcPath=os.path.join(addonPath,"..",".."); xbmcPath=os.path.abspath(xbmcPath); plugintools.log("freshstart.main_list xbmcPath="+xbmcPath); failed=False
        try:
            for root, dirs, files in os.walk(xbmcPath,topdown=True):
                dirs[:] = [d for d in dirs if d not in EXCLUDES]
                for name in files:
                    try: os.remove(os.path.join(root,name))
                    except:
                        if name not in ["Addons15.db","MyVideos75.db","Textures13.db","xbmc.log"]: failed=True
                        plugintools.log("Error removing "+root+" "+name)
                for name in dirs:
                    try: os.rmdir(os.path.join(root,name))
                    except:
                        if name not in ["Database","userdata"]: failed=True
                        plugintools.log("Error removing "+root+" "+name)
            if not failed: plugintools.log("freshstart.main_list All user files removed, you now have a clean install"); plugintools.message(AddonTitle,"The process is complete, you're now back to a fresh Kodi-SPMC configuration with Kobra Wizard!","Please reboot your system or restart Kodi-SPMC in order for the changes to be applied.")
            else: plugintools.log("freshstart.main_list User files partially removed"); plugintools.message("[COLOR grey2][B]FRESH START[/B][/COLOR]","THE PROCESS IS COMPLETE, YOU ARE NOW BACK TO A FRESH KODI-SPMC CONFIGURATION.","PLEASE REBOOT YOUR SYSTEM OR RESTART KODI-SPMC FOR THE CHANGES TO BE APPLIED.")
        except: plugintools.message(AddonTitle,"Problem found","Your settings has not been changed"); import traceback; plugintools.log(traceback.format_exc()); plugintools.log("freshstart.main_list NOT removed")
        plugintools.add_item(action="",title="Now Exit Kodi",folder=False)
    else: plugintools.message("[COLOR red][B][I]KOBRA[/I][/B][/COLOR][COLOR grey] [B]FRESH START[/B][/COLOR]","YOUR SETTINGS HAVE NOT BEEN CHANGED."); plugintools.add_item(action="",title="DONE",folder=False)


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param

N = base64.decodestring('')
T = base64.decodestring('L2FkZG9ucy50eHQ=')
B = base64.decodestring('')
F = base64.decodestring('')
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==4 or mode==5 or mode==7 or mode==8 or mode==15 or mode==17 or mode==20 or mode==22 or mode==27 or mode==28 or mode==30 or mode==31:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok



params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass


print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='false':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )


if mode==None or url==None or len(url)<1:
                INTRO()

elif mode==2:	BUILDMENU()
       
elif mode==3:	MAINTENANCE()
        
elif mode==4:	deletecachefiles(url)
     
elif mode==5:	WIZARD(name,url,description)

elif mode==6:	FRESHSTART(params)

elif mode==7:	DELETEPACKAGES()

elif mode==8:	CONTACT()

elif mode==11:	DELETEIVUEDB()

elif mode==12:	ANDROIDMENU()

elif mode==13:	ICONPACKINSTALLER(name,url,description)

elif mode==14:	ICONCATEGORIES()

elif mode==15:	ICONPACKINSTALLER(name,url,description)

elif mode==16:	ICONINDEX()

elif mode==17:	MICELLANEOUSICONPACKINSTALLER(name,url,description)

elif mode==18:	MICELLANEOUSICONCATEGORIES()

elif mode==19:	APPINSTALLERMENU()

elif mode==20:	ANDROIDAPPSINSTALLER(name,url,description)

elif mode==21:	ANDROIDAPPSWIZARD()

elif mode==22:	BACKGROUNDINSTALLER(name,url,description)

elif mode==23:	BACKGROUNDWIZARD()

elif mode==24:	BACKGROUNDSMENU()

elif mode==25:	THEMEMENU()

elif mode==26:	THEMEWIZARD()

elif mode==27:	THEMEINSTALLER(name,url,description)

elif mode==28:	APPINSTALLER()

elif mode==29:	VIDEOMENU()

elif mode==30:	VIDEOPREVIEW()
		
elif mode==31:	INTRO()

elif mode==32:	APPUNINSTALL()
		
elif mode==33:	SK2WIZARD()

elif mode==99:	COMINGSOON()



xbmcplugin.endOfDirectory(int(sys.argv[1]))