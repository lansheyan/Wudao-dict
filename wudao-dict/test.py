from JsonReader import JsonReader
from CommandDraw import CommandDraw
from UserHistory import UserHistory

query = 'ass'

rd = JsonReader()
paint = CommandDraw()
uh = UserHistory()

wi = rd.get_word_info(query)
if wi is None:
    pass
else:
    uh.add_item(query)
    paint.draw_text(wi)
