"""
CMSC 14200, Spring 2026
Homework 4, Phase 1 Tests

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from task1 import PrecomputedWordGraph
from task2 import variations
from task3 import shortest_path
from task4 import PseudoWordGraph


def test_task1_smallwords_T0() -> None:
    g = PrecomputedWordGraph("smallwords", 3)
    assert g.is_valid_word("abc") == False
    assert g.is_valid_word("cat") == True
    assert g.adjacent_words("cat") == {"bat", "cap"}
    assert g.degree("cat") == 2


def test_task1_web2_T1() -> None:
    g = PrecomputedWordGraph("web2", 4)
    assert g.is_valid_word("abcd") == False
    assert g.is_valid_word("code") == True
    expected = {
        "bode",
        "cade",
        "cede",
        "coda",
        "codo",
        "coke",
        "cole",
        "come",
        "cone",
        "cope",
        "core",
        "cote",
        "coue",
        "cove",
        "coze",
        "dode",
        "gode",
        "lode",
        "mode",
        "node",
        "rode",
        "tode",
        "wode",
    }
    assert g.adjacent_words("code") == expected
    assert g.degree("code") == 23


def test_task2_smallwords_T0() -> None:
    g = PrecomputedWordGraph("smallwords", 3)
    assert variations(g, "cat", 0) == {"cat"}


def test_task2_smallwords_T1() -> None:
    g = PrecomputedWordGraph("smallwords", 3)
    assert variations(g, "cat", 0) == {"cat"}
    assert variations(g, "cat", 1) == {"bat", "cap"}
    assert variations(g, "cat", 2) == {
        "bad",
        "bag",
        "bet",
        "cop",
        "gap",
        "map",
        "sap",
    }
    assert variations(g, "cat", 3) == {"bed", "bug", "gab", "man", "mop", "sip"}
    assert variations(g, "cat", 4) == {
        "dip",
        "dug",
        "fan",
        "men",
        "pan",
        "ran",
        "tab",
        "tan",
    }
    assert variations(g, "cat", 5) == {"dig", "dog", "fun", "pen", "ram", "run"}
    assert variations(g, "cat", 6) == {"fig", "fog", "rim"}
    assert variations(g, "cat", 7) == {"rib"}
    assert variations(g, "cat", 8) == {"rob"}
    assert variations(g, "cat", 9) == {"rod"}
    assert variations(g, "cat", 10) == set()
    assert variations(g, "cat", 11) == set()


def test_task2_web_T0() -> None:
    g = PrecomputedWordGraph("web2", 3)
    actual = variations(g, "xyz", 4)
    assert len(actual) == 0


def test_task2_web_T1() -> None:
    g = PrecomputedWordGraph("web2", 3)
    actual = variations(g, "map", 0)
    expected = {"map"}
    assert actual == expected


def test_task2_web2_T2() -> None:
    g = PrecomputedWordGraph("web2", 3)
    actual = variations(g, "win", 1)
    expected = {
        "bin",
        "din",
        "fin",
        "gin",
        "hin",
        "jin",
        "kin",
        "lin",
        "min",
        "pin",
        "sin",
        "tin",
        "yin",
        "wan",
        "wen",
        "won",
        "wun",
        "wyn",
        "wid",
        "wig",
        "wim",
        "wir",
        "wis",
        "wit",
        "wiz",
    }

    assert actual == expected


def test_task2_web2_T3() -> None:
    g = PrecomputedWordGraph("web2", 3)
    actual = variations(g, "my", 2)
    expected = {
        "am",
        "nu",
        "pa",
        "za",
        "eh",
        "fo",
        "wu",
        "em",
        "ao",
        "at",
        "da",
        "er",
        "al",
        "ga",
        "en",
        "do",
        "ak",
        "te",
        "fa",
        "yr",
        "pu",
        "bu",
        "ta",
        "ca",
        "ab",
        "ne",
        "yo",
        "no",
        "ha",
        "li",
        "ur",
        "na",
        "ax",
        "as",
        "so",
        "wa",
        "tu",
        "de",
        "be",
        "ye",
        "ba",
        "ji",
        "ra",
        "ju",
        "oe",
        "ar",
        "di",
        "hu",
        "go",
        "jo",
        "ti",
        "he",
        "ro",
        "xi",
        "re",
        "lo",
        "ed",
        "ea",
        "wi",
        "ho",
        "ya",
        "el",
        "es",
        "an",
        "vu",
        "fi",
        "or",
        "we",
        "ex",
        "io",
        "la",
        "fe",
        "bo",
        "ko",
        "ah",
        "se",
        "ni",
        "zo",
        "pi",
        "ie",
        "ai",
        "hi",
        "lu",
        "to",
        "ce",
        "wo",
        "si",
        "aw",
        "ae",
        "po",
        "aa",
        "ge",
        "fu",
        "sa",
        "ka",
        "ad",
        "gi",
        "eu",
    }

    assert actual == expected


def test_task2_web2_T4() -> None:
    g = PrecomputedWordGraph("web2", 3)
    actual = variations(g, "who", 3)
    expected = {
        "moi",
        "cos",
        "row",
        "cow",
        "god",
        "abu",
        "alk",
        "hon",
        "dey",
        "lwo",
        "tog",
        "mar",
        "aku",
        "now",
        "lod",
        "sok",
        "bey",
        "voe",
        "uru",
        "neo",
        "ara",
        "fey",
        "foy",
        "mel",
        "gob",
        "sad",
        "joy",
        "wye",
        "ana",
        "hoe",
        "tav",
        "aru",
        "sab",
        "sny",
        "nog",
        "stu",
        "wae",
        "mab",
        "yon",
        "sma",
        "wan",
        "abe",
        "hay",
        "bop",
        "sue",
        "pea",
        "goi",
        "goy",
        "ure",
        "maw",
        "tye",
        "alt",
        "urn",
        "ala",
        "tue",
        "ssu",
        "ron",
        "dob",
        "son",
        "aka",
        "rid",
        "try",
        "noy",
        "rog",
        "nay",
        "ava",
        "met",
        "tua",
        "mat",
        "spa",
        "khu",
        "awa",
        "sog",
        "doe",
        "aba",
        "rip",
        "cor",
        "cee",
        "sac",
        "goa",
        "luo",
        "cob",
        "wad",
        "tor",
        "ssi",
        "tox",
        "may",
        "sah",
        "pot",
        "don",
        "gey",
        "waw",
        "sri",
        "ast",
        "gor",
        "bon",
        "lop",
        "arm",
        "how",
        "tal",
        "urs",
        "wei",
        "tat",
        "mal",
        "not",
        "mew",
        "ido",
        "gol",
        "dop",
        "tol",
        "rea",
        "bow",
        "twi",
        "wah",
        "wes",
        "pod",
        "wyn",
        "tom",
        "poe",
        "roy",
        "sob",
        "dao",
        "sie",
        "fod",
        "mob",
        "taj",
        "wet",
        "coz",
        "hop",
        "kop",
        "sly",
        "hob",
        "sap",
        "lao",
        "are",
        "pow",
        "gio",
        "dhu",
        "wab",
        "blo",
        "yea",
        "ark",
        "top",
        "cop",
        "lox",
        "nob",
        "soy",
        "yao",
        "aly",
        "cue",
        "wig",
        "con",
        "ihi",
        "dow",
        "rod",
        "kon",
        "ale",
        "eon",
        "wer",
        "gon",
        "oft",
        "bay",
        "dog",
        "gog",
        "sla",
        "ibo",
        "ake",
        "coe",
        "sia",
        "tau",
        "urd",
        "aga",
        "fou",
        "apa",
        "fog",
        "roe",
        "spy",
        "alf",
        "tou",
        "rix",
        "mow",
        "uri",
        "tae",
        "ski",
        "pon",
        "apt",
        "olm",
        "wac",
        "meg",
        "gos",
        "wag",
        "alp",
        "poi",
        "mem",
        "moy",
        "rit",
        "tad",
        "bom",
        "sal",
        "jot",
        "zoa",
        "arn",
        "act",
        "vod",
        "rib",
        "got",
        "fob",
        "dot",
        "was",
        "toy",
        "bod",
        "wap",
        "ego",
        "low",
        "psi",
        "bot",
        "upo",
        "mog",
        "yot",
        "col",
        "jon",
        "bos",
        "wed",
        "yeo",
        "ama",
        "pob",
        "cot",
        "boa",
        "arx",
        "tod",
        "tot",
        "win",
        "edo",
        "tax",
        "wun",
        "tie",
        "coy",
        "tow",
        "ave",
        "sod",
        "ion",
        "tee",
        "kay",
        "man",
        "sai",
        "geo",
        "mah",
        "fay",
        "rig",
        "pay",
        "hod",
        "ura",
        "fox",
        "mag",
        "taa",
        "rot",
        "kra",
        "twa",
        "mot",
        "wid",
        "moe",
        "pry",
        "ree",
        "sky",
        "mae",
        "aft",
        "ary",
        "ria",
        "max",
        "wut",
        "pop",
        "dod",
        "sak",
        "wen",
        "sag",
        "agy",
        "ata",
        "tai",
        "wud",
        "ant",
        "sey",
        "war",
        "lou",
        "see",
        "saj",
        "kob",
        "all",
        "yoe",
        "cod",
        "toa",
        "tap",
        "log",
        "lot",
        "cay",
        "rok",
        "sty",
        "sow",
        "flo",
        "tan",
        "abb",
        "age",
        "ady",
        "alb",
        "fot",
        "for",
        "cox",
        "loa",
        "mon",
        "fra",
        "mop",
        "yoy",
        "bob",
        "ayu",
        "sot",
        "sam",
        "yok",
        "rie",
        "san",
        "hey",
        "fry",
        "suu",
        "saw",
        "taw",
        "lay",
        "add",
        "vow",
        "toe",
        "sou",
        "wit",
        "jow",
        "iao",
        "soe",
        "cog",
        "waf",
        "boy",
        "mam",
        "foe",
        "yow",
        "rue",
        "pau",
        "urf",
        "rob",
        "hao",
        "tag",
        "joe",
        "rik",
        "cry",
        "mor",
        "bor",
        "hot",
        "wup",
        "art",
        "koa",
        "kua",
        "job",
        "ada",
        "arc",
        "vog",
        "udo",
        "non",
        "jay",
        "key",
        "ade",
        "map",
        "wat",
        "mer",
        "wem",
        "sye",
        "mou",
        "dry",
        "web",
        "ait",
        "sea",
        "bog",
        "toi",
        "tra",
        "ric",
        "mac",
        "adz",
        "aln",
        "kea",
        "mes",
        "ory",
        "bea",
        "fop",
        "nod",
        "wax",
        "gay",
        "tay",
        "tab",
        "poy",
        "sat",
        "fon",
        "zea",
        "hoy",
        "jog",
        "wee",
        "mod",
        "ley",
        "men",
        "off",
        "rye",
        "saa",
        "ton",
        "tam",
        "nea",
        "tea",
        "sui",
        "mau",
        "ito",
        "hog",
        "day",
        "tar",
        "lob",
        "mas",
        "loy",
        "mad",
        "amt",
        "lof",
        "mev",
        "say",
        "lea",
        "leo",
        "sop",
        "sax",
        "sar",
        "rim",
        "fow",
        "swa",
        "ray",
        "oam",
        "asa",
        "aby",
    }

    assert actual == expected


def test_task3_smallwords_T0() -> None:
    g = PrecomputedWordGraph("smallwords", 3)
    assert shortest_path(g, "cat", "cat") == ["cat"]
    assert shortest_path(g, "cat", "abc") == None


def test_task3_smallwords_T1() -> None:
    g = PrecomputedWordGraph("smallwords", 3)
    assert shortest_path(g, "cat", "bat") == ["cat", "bat"]
    assert shortest_path(g, "cat", "dog") == [
        "cat",
        "bat",
        "bag",
        "bug",
        "dug",
        "dog",
    ]


def test_task3_web2_T1() -> None:
    g = PrecomputedWordGraph("web2", 4)
    actual = shortest_path(g, "cite", "molt")
    allowable = [
        ["cite", "mite", "mitt", "mott", "molt"],
        ["cite", "mite", "mitt", "milt", "molt"],
        ["cite", "mite", "mile", "mole", "molt"],
        ["cite", "mite", "mile", "milt", "molt"],
        ["cite", "mite", "mote", "mole", "molt"],
        ["cite", "mite", "mote", "mott", "molt"],
        ["cite", "cote", "cole", "mole", "molt"],
        ["cite", "cote", "cole", "colt", "molt"],
        ["cite", "cote", "mote", "mole", "molt"],
        ["cite", "cote", "mote", "mott", "molt"],
    ]
    assert actual in allowable


def test_task3_web2_T2() -> None:
    g = PrecomputedWordGraph("web2", 4)
    actual = shortest_path(g, "done", "here")
    allowable = [["done", "dene", "dere", "here"]]
    assert actual in allowable


# This test will likely require more than 30 seconds, which
# is the timeout value configured in pytest.ini.
#
# def test_task3_web2_T3() -> None:
#     g = PrecomputedWordGraph("web2", 5)
#     actual = shortest_path(g, "long", "path")
#     allowable = [
#         ["long", "lone", "lote", "pote", "pate", "path"],
#         ["long", "lone", "lote", "late", "lath", "path"],
#         ["long", "lone", "lote", "late", "pate", "path"],
#         ["long", "lone", "lane", "pane", "pate", "path"],
#         ["long", "lone", "lane", "late", "lath", "path"],
#         ["long", "lone", "lane", "late", "pate", "path"],
#         ["long", "lone", "pone", "pote", "pate", "path"],
#         ["long", "lone", "pone", "pane", "pate", "path"],
#         ["long", "pong", "pone", "pote", "pate", "path"],
#         ["long", "pong", "pone", "pane", "pate", "path"],
#         ["long", "pong", "pang", "pane", "pate", "path"],
#         ["long", "tong", "tang", "tanh", "tath", "path"],
#     ]
#     assert actual in allowable


def test_task4_T0() -> None:
    g = PseudoWordGraph("web2")
    actual = g.adjacent_words("z")
    expected = {
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
    }
    assert actual == expected


def test_task4_T1() -> None:
    g = PseudoWordGraph("web2")
    actual = g.adjacent_words("yz")
    expected = set()
    lc = "abcdefghijklmnopqrstuvwxyz"
    for a in lc:
        for b in lc:
            if a + b != "yz" and (a == "y" or b == "z"):
                expected.add(a + b)
    assert actual == expected


def test_task4_T2() -> None:
    g = PseudoWordGraph("web2")
    actual = g.adjacent_words("xyz")
    expected = set()
    lc = "abcdefghijklmnopqrstuvwxyz"
    for a in lc:
        for b in lc:
            for c in lc:
                if a + b + c != "xyz" and (
                    (a == "x" and b == "y")
                    or (a == "x" and c == "z")
                    or (b == "y" and c == "z")
                ):
                    expected.add(a + b + c)
    assert actual == expected


def test_task4_T3() -> None:
    g = PseudoWordGraph("web2")
    actual = g.adjacent_words("an")
    expected = set()
    lc = "abcdefghijklmnopqrstuvwxyz"
    for a in lc:
        for b in lc:
            if a + b != "an" and (a == "a" or b == "n"):
                expected.add(a + b)
    assert actual == expected


def test_task4_T4() -> None:
    g = PseudoWordGraph("web2")
    actual = g.degree("z")
    expected = 25
    assert actual == expected


def test_task4_T5() -> None:
    g = PseudoWordGraph("web2")
    actual = g.degree("yz")
    expected = 25 + 25
    assert actual == expected


def test_task4_T6() -> None:
    g = PseudoWordGraph("web2")
    actual = g.degree("xyz")
    expected = 25 + 25 + 25
    assert actual == expected


def test_task4_T7() -> None:
    g = PseudoWordGraph("web2")
    actual = g.degree("an")
    expected = 25 + 25
    assert actual == expected


def test_task4_T8() -> None:
    g = PseudoWordGraph("web2")
    actual = g.is_valid_word("an")
    expected = True
    assert actual == expected


def test_task4_T9() -> None:
    g = PseudoWordGraph("web2")
    actual = g.is_valid_word("yz")
    expected = False
    assert actual == expected


def test_task4_variations_smallwords_aat_0() -> None:
    g = PseudoWordGraph("smallwords")
    assert variations(g, "aat", 0) == set()


def test_task4_variations_smallwords_aat_1() -> None:
    g = PseudoWordGraph("smallwords")
    assert variations(g, "aat", 1) == {"bat", "cat"}


def test_task4_variations_smallwords_aat_2() -> None:
    g = PseudoWordGraph("smallwords")
    assert variations(g, "aat", 2) == {
        "bad",
        "bag",
        "bet",
        "cap",
        "fan",
        "gab",
        "gap",
        "man",
        "map",
        "pan",
        "ram",
        "ran",
        "sap",
        "tab",
        "tan",
    }


def test_task4_variations_smallwords_aat_3() -> None:
    g = PseudoWordGraph("smallwords")
    assert variations(g, "aat", 3) == {
        "bed",
        "bug",
        "cop",
        "dig",
        "dip",
        "dog",
        "dug",
        "fig",
        "fog",
        "fun",
        "men",
        "mop",
        "pen",
        "rib",
        "rim",
        "rob",
        "rod",
        "run",
        "sip",
    }


def test_task4_variations_smallwords_aat_4() -> None:
    g = PseudoWordGraph("smallwords")
    assert variations(g, "aat", 4) == set()


def test_task4_variations_web2_yello_0() -> None:
    g = PseudoWordGraph("web2")
    assert variations(g, "yello", 0) == set()


def test_task4_variations_web2_yello_1() -> None:
    g = PseudoWordGraph("web2")
    assert variations(g, "yello", 1) == {"cello", "hello"}


def test_task4_variations_web2_yello_2() -> None:
    g = PseudoWordGraph("web2")
    assert variations(g, "yello", 2) == {
        "bella",
        "belle",
        "belly",
        "callo",
        "cella",
        "della",
        "felly",
        "gelly",
        "helio",
        "helly",
        "hollo",
        "jelly",
        "kella",
        "kelly",
        "nelly",
        "nullo",
        "rollo",
        "sella",
        "selli",
        "selly",
        "tellt",
        "uhllo",
        "welly",
        "yalla",
        "yesso",
    }


def test_task4_variations_web2_qbcde_2() -> None:
    g = PseudoWordGraph("web2")
    assert variations(g, "qbcde", 2) == {"abide", "abode"}
