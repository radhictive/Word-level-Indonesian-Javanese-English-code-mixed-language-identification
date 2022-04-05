import regex

__all__ = ['STANDARD_EMOTICON_UNICODE', 'NON_STANDARD_EMOTICON_UNICODE', 'get_emoticon_regexp']

STANDARD_EMOTICON_LISTS = {
    u'xD': u'xD',
    u':DD': u':DD',
    u':D': u':D',
    u':v': u':v',
    u'.////.': u'.////.',
    u'<3': u'<3',
    u'o:)': u'o:)',
    u'o:-)': u'o:-)',
    u'O:)': u'O:)',
    u'O:-)': u'O:-)',
    u'<;;)': u'<;;)',
    u';;)': u';;)',
    u';)': u';)',
    u';-)': u';-)',
    u':-D': u':-D',
    u':))))))))))))))))))))': u':))))))))))))))))))))',
    u':)))))))))))))))))))': u':)))))))))))))))))))',
    u':))))))))))))))))))': u':))))))))))))))))))',
    u':)))))))))))))))))': u':)))))))))))))))))',
    u':))))))))))))))))': u':))))))))))))))))',
    u':)))))))))))))))': u':)))))))))))))))',
    u':))))))))))))))': u':))))))))))))))',
    u':)))))))))))))': u':)))))))))))))',
    u':))))))))))))': u':))))))))))))',
    u':)))))))))))': u':)))))))))))',
    u':))))))))))': u':))))))))))',
    u':)))))))))': u':)))))))))',
    u':))))))))': u':))))))))',
    u':)))))))': u':)))))))',
    u':))))))': u':))))))',
    u':)))))': u':)))))',
    u':))))': u':))))',
    u':)))': u':)))',
    u':))': u':))',
    u':)': u':)',
    u':/': u':/',
    u':-)': u':-)',
    u':o': u':o',
    u':O': u':O',
    u'@_@': u'@_@',
    u'o.O': u'o.O',
    u'O.o': u'O.o',
    u'o_O': u'o_O',
    u'O_o': u'O_o',
    u':-P': u':-P',
    u':-p': u':-p',
    u'>:-(': u'>:-(',
    u'>:o': u'>:o',
    u'@-)': u'@-)',
    u'>:-o': u'>:-o',
    u':-*': u':-*',
    u'^_^': u'^_^',
    u'^__^': u'^__^',
    u'^___^': u'^___^',
    u'>:(': u'>:(',
    u':|]': u':|]',
    u'/:)': u'/:)',
    u'>:P': u'>:P',
    u'>:p': u'>:p',
    u':O)': u':O)',
    u':o)': u':o)',
    u':-|': u':-|',
    u'<:-p': u'<:-p',
    u'<:-P': u'<:-P',
    u':-q': u':-q',
    u'<):)': u'<):)',
    u'8-|': u'8-|',
    u'T^T': u'T^T',
    u'TT_TT': u'TT_TT',
    u'TTT_TTT': u'TTT_TTT',
    u'T_T': u'T_T',
    u':-B': u':-B',
    u':((((((((((((((((((((': u':((((((((((((((((((((',
    u':(((((((((((((((((((': u':(((((((((((((((((((',
    u':((((((((((((((((((': u':((((((((((((((((((',
    u':(((((((((((((((((': u':(((((((((((((((((',
    u':((((((((((((((((': u':((((((((((((((((',
    u':(((((((((((((((': u':(((((((((((((((',
    u':((((((((((((((': u':((((((((((((((',
    u':(((((((((((((': u':(((((((((((((',
    u':((((((((((((': u':((((((((((((',
    u':(((((((((((': u':(((((((((((',
    u':((((((((((': u':((((((((((',
    u':(((((((((': u':(((((((((',
    u':((((((((': u':((((((((',
    u':(((((((': u':(((((((',
    u':((((((': u':((((((',
    u':(((((': u':(((((',
    u':((((': u':((((',
    u':(((': u':(((',
    u':((': u':((',
    u':(': u':(',
    u';(': u';(',
    u':-((': u':-((',
    u':-(': u':-(',
    u':\')': u':\')',
    u'(y)': u'(y)',
    u'3:)': u'3:)',
    u'3:-)': u'3:-)',
    u'>:3': u'>:3',
    u'(:|': u'(:|',
    u'--"': u'--"',
    u':*': u':*',
    u'._.': u'._.',
    u'.__.': u'.__.',
    u'.___.': u'.___.',
    u'.____.': u'.____.',
    u':3': u':3',
    u':s': u':s',
    u':S': u':S',
    u':|': u':|',
    u":'(((": u":'(((",
    u":'((": u":'((",
    u":'(": u":'(",
    u'=\'(': u'=\'(',
    u'(Y)': u'(Y)',
    u'-_-"': u'-_-"',
    u'-__-"': u'-__-"',
    u'-___-"': u'-___-"',
    u'-____-"': u'-____-"',
    u'-_____-"': u'-_____-"',
    u'-______-"': u'-______-"',
    u'-_-': u'-_-',
    u'-__-': u'-__-',
    u'-___-': u'-___-',
    u'-____-': u'-____-',
    u'-_____-': u'-_____-',
    u'-______-': u'-______-',
    u'>:D': u'>:D',
    u':-]': u':-]',
    u':]': u':]',
    u':-/': u':-/',
    u':-o': u':-o',
    u';\'D': u';\'D',
    u':’)': u':\u2019)',
    u':">': u':">',
    u':")': u':")',
    u'X(': u'X(',
    u':P': u':P',
    u':p': u':p',
    u';p': u';p',
    u';P': u';P',
    u';D': u';D',
    u'=((': u'=((',
    u':>': u':>',
    u'B)': u'B)',
    u':-S': u':-S',
    u'>:)': u'>:)',
    u'=))': u'=))',
    u':-&': u':-&',
    u'=D>': u'=D>',
    u'#-o': u'#-o',
    u':-?': u':-?',
    u':-<': u':-<',
    u':-bd': u':-bd',
    u':-"': u':-"',
    u'X))': u'X))',
    u'X)': u'X)',
    u':9': u':9',
    u'<~3': u'<~3',
    u'</3': u'</3',
    u';))': u';))',
    u'X_X': u'X_X',
    u'x_x': u'x_x',
    u'(:': u'(:',
    u'[-(': u'[-(',
    u'-,-': u'-,-',
    u'>_<': u'>_<',
    u'>_<"': u'>_<"',
}

NON_STANDARD_EMOTICON_LISTS = {
    u'o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(｡❛ᴗ❛｡)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡': u'o\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u256e(\uff61\u275b\u1d17\u275b\uff61)\u256do\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361\u0361', # noqa
    u'❀⃙⃕⃠⃝⃘⃚౪❀⃙⃕⃠⃝⃘⃚': u'\u2740\u20d9\u20d5\u20e0\u20dd\u20d8\u20da\u0c6a\u2740\u20d9\u20d5\u20e0\u20dd\u20d8\u20da',
    u'☆ﾟ･*:｡.:(ﾟ∀ﾟ)ﾟ･*:..:☆': u'\u2606\uff9f\uff65*:\uff61.:(\uff9f\u2200\uff9f)\uff9f\uff65*:..:\u2606',
    u'☆*✲ﾟ*｡(((´♡‿♡`+)))｡*ﾟ✲*☆': u'\u2606*\u2732\uff9f*\uff61(((\xb4\u2661\u203f\u2661`+)))\uff61*\uff9f\u2732*\u2606',
    u'☆*･゜ﾟ･*(^O^)/*･゜ﾟ･*☆': u'\u2606*\uff65\u309c\uff9f\uff65*(^O^)/*\uff65\u309c\uff9f\uff65*\u2606',
    u"*\('-')/*_(._.)_*\('-')/*_(._.)_*\('-')/*": u"*\('-')/*_(._.)_*\('-')/*_(._.)_*\('-')/*",
    u'(^O^)': u'(^O^)',
    u'(^o^)': u'(^o^)',
    u'♥': '\u2665',
    u'\☺/': u'\\\u263a/',
    u'ƪ(‾▿‾)┐': u'\u01aa(\u203e\u25bf\u203e)\u2510',
    u'ƪ(‾.‾“)┐': u'\u01aa(\u203e.\u203e\u201c)\u2510',
    u'ƪ(ˇ▼ˇ)¬': u'\u01aa(\u02c7\u25bc\u02c7)\xac',
    u'("•˘з˘•)': u'("\u2022\u02d8\u0437\u02d8\u2022)',
    u'(˘⌣˘)': u'(\uf8e7\u02d8\u2323\u02d8\uf8e7)',
    u'(‾⌣‾)': u'(\u203e\u2323\u203e)',
    u'☉̴͡ ̯☉̴͡': u'\u2609\u0361\u0334 \u032f\u2609\u0361\u0334',
    u'ƪ(˚▽°")ʃ': u'\u01aa(\u02da\u25bd\xb0")\u0283',
    u'\(^▽^)/': u'\(^\u25bd^)/',
    u'\(^⌣^)/': u'\(^\u2323^)/',
    u'(•ˆ⌣ˆ‎​​​​•)': u'(\u2022\u02c6\u2323\u02c6\u200e\u200b\u200b\u200b\u200b\u2022)',
    u'ƪ(˘⌣˘)┐': u'\u01aa(\u02d8\u2323\u02d8)\u2510',
    u'(˘⌣˘)': u'(\u02d8\u2323\u02d8)',
    u'ƪ(•˘⌣˘)┐': u'\u01aa(\u2022\u02d8\u2323\u02d8)\u2510',
    u'ƪ(˘⌣˘)ʃ': u'\u01aa(\u02d8\u2323\u02d8)\u0283',
    u'┌(˘⌣˘)': u'\u250c(\u02d8\u2323\u02d8)',
    u'┌(˘⌣˘)ʃ': u'\u250c(\u02d8\u2323\u02d8)\u0283',
    u'┌(˘⌣˘•)ʃ': u'\u250c(\u02d8\u2323\u02d8\u2022)\u0283',
    u'(˘⌣˘•)': u'(\u02d8\u2323\u02d8\u2022)',
    u'ƪ(‾,‾")┐': u'\u01aa(\u203e,\u203e")\u2510',
    u'┌("‾,‾)ʃ': u'\u250c("\u203e,\u203e)\u0283',
    u'\(´△`")/': u'\(\xb4\u25b3`")/',
    u'(ˇ▼ˇ)': u'(\u02c7\u25bc\u02c7)',
    u'‎​ƪ(◦ϖ◦)ʃ': u'\u200e\u200b\u01aa(\u25e6\u03d6\u25e6)\u0283',
    u'Щ(¯Д¯"щ)': u'\u0429(\xaf\u0414\xaf"\u0449)',
    u'(¯―¯٥)': u'(\xaf\u2015\xaf\u0665)',
    u'ƪ(‾ε‾")ʃ': u'\u01aa(\u203e\u03b5\u203e")\u0283',
    u'ƪ(‾ε‾“)ʃ': u'\u01aa(\u203e\u03b5\u203e\u201c)\u0283',
    u'(˘ε˘\'!l)': u'(\u02d8\u03b5\u02d8\'!l)',
    u'(っ￣з￣)っ': u'(\u3063\uffe3\u0437\uffe3)\u3063',
    u'ƪ(♥o♥)ʃ': u'\u200e\u200b\u200b\u200b\u01aa(\u2665o\u2665)\u0283',
    u'♥⌣♥': u'\u2665\u2323\u2665',
    u'ƪ♥ε♥ʃ': u'\u01aa\u2665\u03b5\u2665\u0283',
    u'(˘ﻬ˘)': u'(\uf8e7\u02d8\ufeec\u02d8\uf8e7)',
    u'(˘⌣˘)ε˘`)': u'(\u02d8\u2323\u02d8)\u03b5\u02d8`)',
    u'ƪ(‾̣̣̣﹏‾̣̣̣̣̣̣")ʃ': u'\u01aa(\u203e\u0323\u0323\u0323\ufe4f\u203e\u0323\u0323\u0323\u0323\u0323\u0323")\u0283',
    u'(╥﹏╥)': u'(\u2565\ufe4f\u2565)',
    u'(˘3˘)--c<ˇ_ˇ)': u'(\u02d83\u02d8)--c<\u02c7_\u02c7)',
    u"~('▽'~)(~'▽')~": u"~('\u25bd'~)(~'\u25bd')~",
    u'ƪ(°͡▿▿▿▿▿▿°")͡ƪ': u'\u01aa(\xb0\u0361\u25bf\u25bf\u25bf\u25bf\u25bf\u25bf\xb0")\u0361\u01aa',
    u"(¬.¬)ƪ_(˘з˘')": u"(\xac.\xac)\u01aa_(\u02d8\u0437\u02d8')",
    u'~(^.^~)(~^.^)~': u'~(^.^~)(~^.^)~',
    u'ː̗̀(☉_☉)ː̖́': u'\u02d0\u0317\u0300(\u2609_\u2609)\u02d0\u0316\u0301',
    u'(˘ﻬ(˘⌣˘)': u'(\uf8e7\u02d8\ufeec(\u02d8\u2323\u02d8)',
    u'(¬_¬")': u'(\xac_\xac")',
    u'\(´▽`)/': u'\(\xb4\u25bd`)/',
    u'(⌣́_⌣̀)': u'(\u2323\u0301_\u2323\u0300)',
    u'(♒˙⌣˙♒)': u'(\u2652\u02d9\u2323\u02d9\u2652)',
    u'(˘̩̩̩.˘̩ƪ)': u'(\u02d8\u0329\u0329\u0329.\u02d8\u0329\u01aa)',
    u'(˘̩̩̩-˘̩̩̩ƪ)': u'(\u02d8\u0329\u0329\u0329-\u02d8\u0329\u0329\u0329\u01aa)',
    u'(-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)': u'(-\u0329\u0329\u0329-\u0329\u0329\u0329_-\u0329\u0329\u0329-\u0329\u0329\u0329)',
    u"(-___-')": u"(-___-')",
    u'\(^u^)/': u'\(^u^)/',
    u'(^^^)': u'(^^^)',
    u'(✿◠‿◠)': u'(\u273f\u25e0\u203f\u25e0)',
    u'(˘_˘\\")': u'(\u02d8_\u02d8\\")',
    u'(\\"`▽´)-σ': u'(\\"`\u25bd\xb4)-\u03c3',
    u'd(^_^)b': u'd(^_^)b',
    u'ƪ(♥ε♥)ʃ': u'\u01aa(\u2665\u03b5\u2665)\u0283',
    u'(☉_☉)': u'(\u2609_\u2609)',
    u'♥‿♥': u'\u2665\u203f\u2665',
    u'ƗƗɐƗƗɐƗƗɐ': u'\u0197\u0197\u0250\u0197\u0197\u0250\u0197\u0197\u0250',
    u'(¬_¬)--o(✗_✗)': u'(\xac_\xac)--o(\u2717_\u2717)',
    u'(¬_¬)': u'(\xac_\xac)',
    u'┌П┐(►_◄)┌П┐': u'\u250c\u041f\u2510(\u25ba_\u25c4)\u250c\u041f\u2510',
    u'┌П┐(►_◄")': u'\u250c\u041f\u2510(\u25ba_\u25c4")',
    u'(ʃ˘̩̩̩_˘̩̩̩ƪ)': u'(\u0283\u02d8\u0329\u0329\u0329_\u02d8\u0329\u0329\u0329\u01aa)',
    u'(´•_•`)': u'(\xb4\u2022_\u2022`)',
    u'♣♦♥♠': u'\u2663\u2666\u2665\u2660',
    u'¬_¬': u'\xac_\xac',
    u'(╯︵╰,)': u'(\u256f\ufe35\u2570,)',
    u'\(‾▿‾\)┌(_o_)┐(/‾▿‾)/': u'\(\u203e\u25bf\u203e\)\u250c(_o_)\u2510(/\u203e\u25bf\u203e)/',
    u'•°˚\\☺/˚°•': u'\u2022\xb0\u02da\\\u263a/\u02da\xb0\u2022',
    u'(˘̩̩̩ε˘̩̩̩ƪ)': u'(\u02d8\u0329\u0329\u0329\u03b5\u02d8\u0329\u0329\u0329\u01aa)',
    u'B-)': u'B-)',
    u'(˘̩̩̩~˘̩̩̩ƪ)': u'(\u02d8\u0329\u0329\u0329~\u02d8\u0329\u0329\u0329\u01aa)',
    u'┌П┐(•͡˛˘•͡")┌П┐': u'\u250c\u041f\u2510(\u2022\u0361\u02db\u02d8\u2022\u0361")\u250c\u041f\u2510',
    u'♬': u'\u266c',
    u'(˘_˘")': u'(\u02d8_\u02d8")',
    u'(¯`O´¯)': u'(\xaf`O\xb4\xaf)',
    u'ː̗̀(☉,☉)ː̖́': u'\u02d0\u0317\u0300(\u2609,\u2609)\u02d0\u0316\u0301',
    u'(ˇ_ˇ")': u'(\u02c7_\u02c7")',
    u'┌П┐': u'\u250c\u041f\u2510',
    u'w(>,<)w': u'w(>,<)w',
    u'┌П┐(►˛◄)┌П┐': u'\u250c\u041f\u2510(\u25ba\u02db\u25c4)\u250c\u041f\u2510',
    u'(っ˘з˘)っ': u'(\u3063\u02d8\u0437\u02d8)\u3063',
    u'~(‾▿‾~)': u'~(\u203e\u25bf\u203e~)',
    u'~(‾▿‾)~': u'~(\u203e\u25bf\u203e)~',
    u'(~‾▿‾)~': u'(~\u203e\u25bf\u203e)~',
    u'\(‾▿‾\)': u'\(\u203e\u25bf\u203e\)',
    u'┌(_o_)┐': u'\u250c(_o_)\u2510',
    u'(/‾▿‾)/': u'(/\u203e\u25bf\u203e)/',
    u'\(^▿^)/': u'\(^\u25bf^)/',
    u'(^▿^)': u'(^\u25bf^)',
    u'‎​(•˘з˘•)': u'(\u2022\u02d8\u0437\u02d8\u2022)',
    u'(^.^)': u'(^.^)',
    u'ƪ(˘ڡ˘)ʃ': u'\u01aa(\u02d8\u06a1\u02d8)\u0283',
    u'(╥_╥)': u'(\u2565_\u2565)',
    u'(-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩___-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩)': u'(-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329___-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329)', # noqa
    u'(-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩___-̩̩̩-̩̩̩-̩̩̩-̩̩̩)': u'(-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329___-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329-\u0329\u0329\u0329)', # noqa
    u'(*^_^)': u'(*^_^)',
    u'(✖╭╮✖)': u'(\u2716\u256d\u256e\u2716)',
    u'(-_*)': u'(-_*)',
    u'(-‿◕)': u'(-\u203f\u25d5)',
    u'╰(◣﹏◢)╯': u'\u2570(\u25e3\ufe4f\u25e2)\u256f',
    u'ƪ_(☉▿▿▿▿▿▿☉)_ʃ': u'\u01aa_(\u2609\u25bf\u25bf\u25bf\u25bf\u25bf\u25bf\u2609)_\u0283',
    u'°~=))••°wk.wk.wk°••=))~°': u'\xb0~=))\u2022\u2022\xb0wk.wk.wk\xb0\u2022\u2022=))~\xb0',
    u'（＾_＾）': u'\uff08\uff3e_\uff3e\uff09',
    u'(>_<)>': u'(>_<)>',
    u'(>_<)': u'(>_<)',
    u'(^_^;)': u'(^_^;)',
    u'(ToT)': u'(ToT)',
    u'(^^;)': u'(^^;)',
    u'（￣ー￣）': u'\uff08\uffe3\u30fc\uffe3\uff09',
    u'(≧∇≦)/': u'(\u2267\u2207\u2266)/',
    u'(≧∇≦)': u'(\u2267\u2207\u2266)',
    u'（￣□￣；）': u'\uff08\uffe3\u25a1\uffe3\uff1b\uff09',
    u'(#^.^#)': u'(#^.^#)',
    u'（*´▽｀*）': u'\uff08*\xb4\u25bd\uff40*\uff09',
    u'(ーー;)': u'(\u30fc\u30fc;)',
    u'(*^▽^*)': u'(*^\u25bd^*)',
    u'(＾▽＾)': u'(\uff3e\u25bd\uff3e)',
    u'(´･ω･`)': u'(\xb4\uff65\u03c9\uff65`)',
    u'（・∀・）': u'\uff08\u30fb\u2200\u30fb\uff09',
    u'(Ｔ▽Ｔ)': u'(\uff34\u25bd\uff34)',
    u'(*￣m￣)': u'(*\uffe3m\uffe3)',
    u'（　´∀｀）': u'\uff08\u3000\xb4\u2200\uff40\uff09',
    u'（⌒▽⌒）': u'\uff08\u2312\u25bd\u2312\uff09',
    u'（＾ｖ＾）': u'\uff08\uff3e\uff56\uff3e\uff09',
    u'ヽ（´ー｀）┌': u'\u30fd\uff08\xb4\u30fc\uff40\uff09\u250c',
    u'（’-’*)': u'\uff08\u2019-\u2019*)',
    u'(’A`)': u'(\u2019A`)',
    u'（゜◇゜）': u'\uff08\u309c\u25c7\u309c\uff09',
    u'(*°∀°)=3': u'(*\xb0\u2200\xb0)=3',
    u'\m/': u'\m/',
    u'\:D/': u'\:D/',
    u'*__*': u'*__*',
    u'*___*': u'*___*',
    u'*____*': u'*____*',
    u'*_____*': u'*_____*',
    u'*______*': u'*______*',
    u'(*__*")': u'(*__*")',
    u'(*___*")': u'(*___*")',
    u'(*____*")': u'(*____*")',
    u'(*_____*")': u'(*_____*")',
    u'o(^^o) (o^^)o': u'o(^^o)\xa0(o^^)o',
    u'Sε♏âΩ9aT': u'S\u03b5\u264f\xe2\u03a99aT',
    u'ƗƗɐƗƗɐ': u'\u0197\u0197\u0250\u0197\u0197\u0250',
    u'(⌒▽⌒)': u'(\u2312\u25bd\u2312)',
    u'(≧ロ≦)': u'(\u2267\u30ed\u2266)',
    u'(￣ー￣)': u'(\uffe3\u30fc\uffe3)',
    u'(=_=)': u'(=_=)',
    u'(ˇ_ˇ\'!l)': u'(\u02c7_\u02c7\'!l)',
    u'( ¬͡͡˛ ¬͡͡")': u'( \xac\u0361\u0361\u02db \xac\u0361\u0361")',
    u'(–˛ — º)': u'(\u2013\u02db \u2014 \xba)',
    u'∩( ・ω・)∩': u'\u2229( \u30fb\u03c9\u30fb)\u2229',
    u'( ・ω・)': u'( \u30fb\u03c9\u30fb)',
    u'm(_ _)m': u'm(_ _)m',
    u'(_ _’)': u'(_ _\u2019)',
    u'(_ _")': u'(_ _")',
    u'(_ _\')': u'(_ _\')',
    u'（　ﾟ Дﾟ）': u'\uff08\u3000\uff9f \u0414\uff9f\uff09',
    u'HOoº°°ºoOam ((˘O˘"),,': u'HOo\xba\xb0\xb0\xbaoOam ((\u02d8O\u02d8"),,',
    u'ヽ( ･∀･)ﾉ┌┛Σ(ノ `Д´)ノ': u'\u30fd( \uff65\u2200\uff65)\uff89\u250c\u251b\u03a3(\u30ce `\u0414\xb4)\u30ce',
    u'(>ˆ▽ˆ)> ωªªκªªκªª <(ˆ▽ˆ<)': u'(>\u02c6\u25bd\u02c6)> \u03c9\xaa\xaa\u03ba\xaa\xaa\u03ba\xaa\xaa <(\u02c6\u25bd\u02c6<)',   # noqa
    u'=D˘•˘=)) нªª˘°˘нªª˘°˘нªª˘°˘ =))˘•˘=D': u'=D\u02d8\u2022\u02d8=)) \u043d\xaa\xaa\u02d8\xb0\u02d8\u043d\xaa\xaa\u02d8\xb0\u02d8\u043d\xaa\xaa\u02d8\xb0\u02d8 =))\u02d8\u2022\u02d8=D', # noqa
    u'ε=ε=┏( >_<)┛': u'\u03b5=\u03b5=\u250f( >_<)\u251b',
    u'(⌒˛⌒ )': u'(\u2312\u02db\u2312 )',
    u'( ^.^)╱d□☆□b╲(^.^ )': u'( ^.^)\u2571d\u25a1\u2606\u25a1b\u2572(^.^ )',
    u'(´▽`) - c<ˇ εˇ)': u'(\xb4\u25bd`) - c<\u02c7 \u03b5\u02c7)',
    u"(\" `з´ )_,/\"(>_<')": u"(\" `\u0437\xb4 )_,/\"(>_<')",
    u'( ⌣ ́_ ⌣ ̀)': u'( \u2323 \u0301_ \u2323 \u0300)',
    u"(˘̶ِ̀ ˘̶́')": u"(\u02d8\u0336\u0300\u0650 \u02d8\u0336\u0301')",
    u'(´̩ε `̩ )': u'(\xb4\u0329\u03b5 `\u0329 )',
    u'(⌣_⌣ ")': u'(\u2323_\u2323 ")',
    u'⌣́.⌣̀': u'\u2323\u0301.\u2323\u0300',
    u'(⌣́.⌣̀)': u'(\u2323\u0301.\u2323\u0300)',
    u'( ˘͡ .˘͡)': u'( \u02d8\u0361 .\u02d8\u0361)',
    u'(ɔˇ ³ ˇ)ɔ': u'(\u0254\u02c7 \xb3 \u02c7)\u0254',
    u'(ʃ˘̩̩̩.˘̩̩̩ƪ)\\(•_• )': u'(\u0283\u02d8\u0329\u0329\u0329.\u02d8\u0329\u0329\u0329\u01aa)\\(\u2022_\u2022 )',
    u'¬ -̮ ¬': u'\xac -\u032e \xac',
    u'(^_^)/~~  (~o~)': u'(^_^)/~~  (~o~)',
    u'╋╋ム ╋╋ム ╋╋ム': u'\u254b\u254b\u30e0 \u254b\u254b\u30e0 \u254b\u254b\u30e0',
    u"┐('⌣'┐)  (┌'⌣')┌": u"\u2510('\u2323'\u2510)  (\u250c'\u2323')\u250c",
    u"(˘̶ِ̀ ˘̶́ ')": u"(\u02d8\u0336\u0300\u0650 \u02d8\u0336\u0301 ')",
    u'¯\_(ツ)_/¯': u'\xaf\_(\u30c4)_/\xaf',
    u'ƪ(‾⌣‾ )ʃ': u'\u01aa(\u203e\u2323\u203e )\u0283',
    u'ƪ(‾⌣‾♥)ʃ': u'\u01aa(\u203e\u2323\u203e\u2665)\u0283',
    u'ƪ_(☉__☉")_ʃ': u'\u01aa_(\u2609__\u2609")_\u0283',
    u'ƪ_(☉ __ ☉")_ʃ': u'\u01aa_(\u2609 __ \u2609")_\u0283',
    u'\(‾▿‾\) ┌(_o_)┐ (/‾▿‾)/': u'\(\u203e\u25bf\u203e\) \u250c(_o_)\u2510 (/\u203e\u25bf\u203e)/',
    u'(˘̩̩̩⌣˘̩̩̩ )': u'(\u02d8\u0329\u0329\u0329\u2323\u02d8\u0329\u0329\u0329 )',
    u'┐(‾.‾)┐ ┌(‾.‾)┌': u'\u2510(\u203e.\u203e)\u2510 \u250c(\u203e.\u203e)\u250c',
    u'┐(˘▿˘┐) (┌˘▿˘)┌': u'\u2510(\u02d8\u25bf\u02d8\u2510) (\u250c\u02d8\u25bf\u02d8)\u250c',
    u'‎​(•͡ε˘•͡ )': u'\u200e\u200b(\u2022\u0361\u03b5\u02d8\u2022\u0361 )',
    u'◎(￣^￣)====◎)>_<")': u'\u25ce(\uffe3^\uffe3)====\u25ce)>_<")',
    u'Ơ̴̴̴̴̴̴͡.̮Ơ̴̴͡': u'\u01a0\u0361\u0334\u0334\u0334\u0334\u0334\u0334.\u032e\u01a0\u0361\u0334\u0334',
    u'(•̯͡.•̯͡)': u'(\u2022\u0361\u032f.\u2022\u0361\u032f)',
    u'ƪ(‾▿‾)ʃ‎​': u'\u01aa(\u203e\u25bf\u203e)\u0283 \u200e\u200b',
    u'ƪ(― ε ―")ʃ': u'\u01aa(\u2015 \u03b5 \u2015")\u0283',
    u'ƪ( ‾ ⌣ ‾" )ʃ': u'\u01aa( \u203e \u2323 \u203e" )\u0283',
    u'-(‾▿‾)/ \(‾▿‾)-': u'\uf8e7-(\u203e\u25bf\u203e)/\uf8e7 \uf8e7\(\u203e\u25bf\u203e)-\uf8e7',
    u'(" `з´ )9': u'(" `\u0437\xb4 )9',
    u"\('-'\) (/'-')/": u"\('-'\) (/'-')/",
    u'(-̩̩̩-͡ ̗--̩̩̩͡ )': u'(-\u0329\u0329\u0329-\u0361 \u0317--\u0329\u0361\u0329\u0329 )',
    u'(X_X")': u'(X_X")',
    u'(X__X")': u'(X__X")',
    u'(X___X")': u'(X___X")',
    u'(X____X")': u'(X____X")',
    u'(X______________________X")': u'(X______________________X")',
}