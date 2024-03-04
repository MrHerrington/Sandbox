class HtmlTag:
    level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        if not self.inline:
            print(f"{'  ' * HtmlTag.level}<{self.tag}>")
            HtmlTag.level += 1
        else:
            print(f"{'  ' * HtmlTag.level}<{self.tag}>", end='')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.inline:
            HtmlTag.level -= 1
            print(f"{'  ' * HtmlTag.level}</{self.tag}>")

    def print(self, text):
        if self.inline:
            print(f'{text}</{self.tag}>')
        else:
            print('  ' * HtmlTag.level + text)


# Test №1
with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды DUNGEON')

# Test №2
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды DUNGEON')

# Test №3
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')
