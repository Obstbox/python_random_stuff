from tinyhtml import html, h

html_content = html(lang="en")(
    h("head")(
        (h("h1")("hello geeks!")),
        ),
    ).render()

print(html_content)
