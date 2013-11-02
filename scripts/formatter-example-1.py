import formatter
import htmllib

w = formatter.AbstractWriter()
f = formatter.AbstractFormatter(w)

file = open("samples/sample.htm")

p = htmllib.HTMLParser(f)
p.feed(file.read())
p.close()

file.close()

## send_paragraph(1)
## new_font(('h1', 0, 1, 0))
## send_flowing_data('A Chapter.')
## send_line_break()
## send_paragraph(1)
## new_font(None)
## send_flowing_data('Some text. Some more text. Some')
## send_flowing_data(' ')
## new_font((None, 1, None, None))
## send_flowing_data('emphasised')
## new_font(None)
## send_flowing_data(' text. A')
## send_flowing_data(' link')
## send_flowing_data('[1]')
## send_flowing_data('.')
