class script(object):
    START_TXT = """๐ท๐ด๐ป๐พ {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>, ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐, ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ด๐ฝ๐น๐พ๐ ๐"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โฏ ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>
โฏ ๐ป๐ธ๐ฑ๐๐ฐ๐๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
โฏ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
โฏ ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
โฏ ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐ท๐ด๐๐พ๐บ๐
โฏ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: v1.0.1 [ ๐ฑ๐ด๐๐ฐ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
-Mแดสแดสแดส ษชs แด แดสแดsแดแด แดแดแดษด sแดแดสแดแด แดสแดษชแดแดแด 
- Bแดsแด Sแดแดสแดแด แดแดแดแด - https://github.com/EvamariaTG/EvaMaria  

<b><u>DEVS:</u></b>
- <a href=https://t.me/Xrsirx5>Xrsirx5</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Fษชสแดแดส ษชs แดสแด าแดแดแดแดสแด แดกแดสแด แดsแดสs แดแดษด sแดแด แดแดแดแดแดแดแดแดแด สแดแดสษชแดs าแดส แด แดแดสแดษชแดแดสแดส แดแดสแดกแดสแด แดษดแด แดแดสแดสแดส แดกษชสส สแดsแดแดษดแด แดกสแดษดแดแด แดส แด แดแดสแดกแดสแด ษชs าแดแดษดแด แดสแด แดแดssแดษขแด

<b>NOTE:</b>
๐ท. Mแดสแดสแดส sสแดแดสแด สแดแด แด แดแดแดษชษด แดสษชแด ษชสสแดษขแด.
๐ธ. แดษดสส แดแดแดษชษดs แดแดษด แดแดแด าษชสแดแดสs ษชษด แด แดสแดแด.
๐น. แดสแดสแด สแดแดแดแดษดs สแดแด แด แด สษชแดษชแด แดา ๐ผ๐บ แดสแดสแดแดแดแดสs.

<b>Commands and Usage:</b>
โข /filter - <b>add a filter in chat</b>
โข /filters - <b>list all the filters of a chat</b>
โข /del - <b>delete a specific filter in chat</b>
โข /delall - <b>delete the whole filters in a chat (chat owner only)</b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
๐ท. Mแดแดแด แดแด แดสแด แดแดแดษชษด แดา สแดแดส แดสแดษดษดแดส ษชา ษชแด's แดสษชแด แดแดแด.
๐ธ. แดแดแดแด sแดสแด แดสแดแด สแดแดส แดสแดษดษดแดส แดแดแดs ษดแดแด แดแดษดแดแดษชษดs แดแดแดสษชแดs, แดแดสษด แดษดแด าแดแดแด าษชสแดs.
๐น. Fแดสแดกแดสแด แดสแด สแดsแด แดแดssแดษขแด แดแด แดแด แดกษชแดส วซแดแดแดแดs.
 I'สส แดแดแด แดสส แดสแด าษชสแดs ษชษด แดสแดแด แดสแดษดษดแดส แดแด แดส แดส."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Usแดแด แดแด แดแดษดษดแดแดแด สแดแด แดแด PM าแดส แดแดษดแดษขษชษดษข าษชสแดแดสs 
- ษชแด สแดสแดs แดแด แดแด แดษชแด sแดแดแดแดษชษดษข ษชษด ษขสแดแดแดs.

<b>NOTE:</b>
๐ท. Oษดสส แดแดแดษชษดs แดแดษด แดแดแด แด แดแดษดษดแดแดแดษชแดษด.
๐ธ. Sแดษดแด <code>/แดแดษดษดแดแดแด</code> าแดส แดแดษดษดแดแดแดษชษดษข แดแด แดแด แดส PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
