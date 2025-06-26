full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Markdown to HTML</title>
    <style>
        :root {{
            --bg: #f5f7fa;
            --text: #2e2e2e;
            --accent: #007acc;
            --code-bg: #f0f0f0;
            --code-dark: #272822;
            --code-text: #f8f8f2;
        }}
        * {{
            box-sizing: border-box;
        }}
        body {{
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            padding: 2rem;
            line-height: 1.7;
        }}
        h1, h2, h3 {{
            color: #1e1e1e;
            margin-top: 1.5em;
            border-bottom: 1px solid #ddd;
            padding-bottom: 0.3em;
        }}
        a {{
            color: var(--accent);
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul {{
            padding-left: 1.5rem;
            margin-top: 0.5rem;
        }}
        code {{
            background: var(--code-bg);
            padding: 2px 6px;
            border-radius: 5px;
            font-family: monospace;
            font-size: 0.95em;
        }}
        pre {{
            background-color: var(--code-dark);
            color: var(--code-text);
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            margin-top: 1rem;
        }}
        blockquote {{
            border-left: 4px solid #ccc;
            padding-left: 1rem;
            color: #666;
            margin: 1rem 0;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ccc;
            margin: 2rem 0;
        }}
        img {{
            max-width: 100%;
            border-radius: 10px;
        }}
    </style>
</head>
<body>
<main>
{html_content}
</main>
</body>
</html>"""
